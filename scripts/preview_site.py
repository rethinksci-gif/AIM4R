"""Build a local, approximate preview of the GitHub Pages site without Jekyll.

Renders docs/ with python-liquid and Python-Markdown, implementing only the
Jekyll features this site uses (layouts, includes, site.posts, site.data,
relative_url, where, date_to_xmlschema, seo). It is a preview aid, not a
Jekyll replacement: GitHub Pages remains the reference build.

Usage (preview-only dependencies are not project dependencies):

    uv run --with "python-liquid<2" --with pyyaml python scripts/preview_site.py \
        --out /tmp/aim4r-site --gh-pages-posts --extra-posts docs/_previews \
        --data docs/_previews/aim4r_history.sample.json
    python -m http.server -d /tmp/aim4r-site 8000   # open http://localhost:8000/AIM4R/
"""

import argparse
import datetime as dt
import html
import json
import re
import shutil
import subprocess
from pathlib import Path

import markdown
import yaml
from liquid import Environment, FileSystemLoader
from liquid.ast import Node
from liquid.parse import expect
from liquid.stream import TokenStream
from liquid.tag import Tag
from liquid.token import TOKEN_EOF, TOKEN_TAG

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
POST_NAME = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")


def split_front_matter(text: str) -> tuple[dict, str]:
    if text.startswith("---"):
        _, front, body = text.split("---", 2)
        return yaml.safe_load(front) or {}, body.lstrip("\n")
    return {}, text


def as_datetime(value) -> dt.datetime:
    if isinstance(value, dt.datetime):
        return value
    if isinstance(value, dt.date):
        return dt.datetime(value.year, value.month, value.day)
    return dt.datetime.fromisoformat(str(value))


class SeoNode(Node):
    def __init__(self, tok):
        self.tok = tok

    def render_to_output(self, context, buffer):
        page = context.resolve("page")
        site = context.resolve("site")
        title = page.get("title") or site.get("title")
        buffer.write(f"<title>{html.escape(str(title))}</title>")


class SeoTag(Tag):
    name = "seo"
    block = False

    def parse(self, stream: TokenStream) -> Node:
        expect(stream, TOKEN_TAG, value=self.name)
        return SeoNode(stream.current)


def build_env(baseurl: str, site_url: str) -> Environment:
    env = Environment(loader=FileSystemLoader(str(DOCS / "_includes")))
    env.add_tag(SeoTag)
    env.add_filter("relative_url", lambda value: baseurl + str(value))
    env.add_filter("absolute_url", lambda value: site_url + baseurl + str(value))
    env.add_filter("date_to_xmlschema", lambda value: as_datetime(value).strftime("%Y-%m-%dT%H:%M:%S+00:00"))
    env.add_filter(
        "where",
        lambda items, key, value: [item for item in (items or []) if str(item.get(key)) == str(value)],
    )
    return env


def render_markdown(body: str) -> str:
    return markdown.markdown(body, extensions=["tables", "md_in_html", "attr_list"])


def load_posts(sources: list[Path], env: Environment, site: dict) -> list[dict]:
    posts = []
    for path in sources:
        match = POST_NAME.match(path.name)
        if not match:
            continue
        year, month, day, slug = match.groups()
        front, body = split_front_matter(path.read_text(encoding="utf-8"))
        front["date"] = as_datetime(front.get("date") or f"{year}-{month}-{day}")
        content = render_markdown(env.from_string(body).render(site=site, page=front))
        first_paragraph = re.search(r"<p>(.*?)</p>", content, re.S)
        posts.append(
            {
                **front,
                "url": f"/{year}/{month}/{day}/{slug}.html",
                "content": content,
                "excerpt": first_paragraph.group(0) if first_paragraph else "",
                "_path": path,
            }
        )
    return sorted(posts, key=lambda post: post["date"], reverse=True)


def gh_pages_posts(target: Path) -> list[Path]:
    target.mkdir(parents=True, exist_ok=True)
    names = subprocess.run(
        ["git", "ls-tree", "--name-only", "origin/gh-pages", "_posts/"],
        cwd=ROOT, check=True, capture_output=True, text=True,
    ).stdout.split()
    paths = []
    for name in names:
        text = subprocess.run(
            ["git", "show", f"origin/gh-pages:{name}"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout
        path = target / Path(name).name
        path.write_text(text, encoding="utf-8")
        paths.append(path)
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", required=True)
    parser.add_argument("--gh-pages-posts", action="store_true", help="include posts published on origin/gh-pages")
    parser.add_argument("--extra-posts", action="append", default=[], help="directory of extra posts (e.g. previews)")
    parser.add_argument("--data", help="history JSON exposed as site.data.aim4r_history")
    args = parser.parse_args()

    config = yaml.safe_load((DOCS / "_config.yml").read_text())
    baseurl = config.get("baseurl", "")
    out = Path(args.out)
    shutil.rmtree(out, ignore_errors=True)
    site_root = out / baseurl.strip("/")
    site_root.mkdir(parents=True)

    env = build_env(baseurl, config.get("url", ""))
    data = {}
    if args.data:
        data["aim4r_history"] = json.loads(Path(args.data).read_text())
    site = {**config, "data": data, "time": dt.datetime.now(), "posts": []}

    sources = sorted((DOCS / "_posts").glob("*.md"))
    if args.gh_pages_posts:
        sources += gh_pages_posts(out / "_gh_pages_posts")
    for directory in args.extra_posts:
        sources += sorted(Path(directory).glob("*.md"))
    by_name = {path.name: path for path in sources}  # later sources win
    site["posts"] = load_posts(list(by_name.values()), env, site)

    layout_source = (DOCS / "_layouts" / "default.html").read_text(encoding="utf-8")
    # Jekyll accepts unquoted include names; Liquid proper needs a string.
    layout_source = re.sub(r"{%\s*include\s+([\w.-]+)\s*%}", r"{% include '\1' %}", layout_source)
    layout_template = env.from_string(layout_source)

    def write_page(rel_url: str, page: dict, content_html: str) -> None:
        rendered = layout_template.render(site=site, page=page, content=content_html)
        target = site_root / rel_url.lstrip("/")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8")

    for post in site["posts"]:
        write_page(post["url"], post, post["content"])

    for name in ("index.md", "method.md"):
        front, body = split_front_matter((DOCS / name).read_text(encoding="utf-8"))
        page = {**front, "url": "/" + name.replace(".md", ".html")}
        content = env.from_string(body).render(site=site, page=page)
        content = content if front.get("page_kind") == "home" else render_markdown(content)
        write_page(page["url"], page, content)

    for feed in ("feed-zh.xml", "feed-en.xml"):
        _, body = split_front_matter((DOCS / feed).read_text(encoding="utf-8"))
        (site_root / feed).write_text(env.from_string(body).render(site=site), encoding="utf-8")

    shutil.copytree(DOCS / "assets", site_root / "assets")
    print(f"Preview built: {site_root} ({len(site['posts'])} posts)")


if __name__ == "__main__":
    main()
