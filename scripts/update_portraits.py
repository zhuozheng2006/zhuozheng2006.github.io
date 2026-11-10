#!/usr/bin/env python3
"""Regenerate the bilingual portrait markup and credits from the selected roster."""

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PORTRAITS = json.loads((ROOT / "assets/portraits/portraits.json").read_text())
VERSION = "20261110-selected-math"


def esc(value):
    return html.escape(str(value), quote=True)


def figure(person, english=False, deferred=True, indent="          "):
    name = person["en" if english else "zh"]
    alt = f"{name} portrait" if english else f"{name}肖像"
    attribute = "data-src" if deferred else "src"
    return (
        f'{indent}<figure class="banner__portrait banner__portrait--{esc(person["id"])}">\n'
        f'{indent}  <img {attribute}="{esc(person["file"])}" alt="{esc(alt)}" '
        f'width="{person["width"]}" height="{person["height"]}" decoding="async">\n'
        f'{indent}</figure>'
    )


fallback_ids = {"spinoza", "kant", "hegel", "nietzsche"}
for filename, english in [("index.html", False), ("en.html", True)]:
    page = ROOT / filename
    source = page.read_text()
    start = source.index('    <div class="banner__portraits">')
    end = source.index('    <div class="banner__shade"', start)
    figures = "\n".join(figure(person, english) for person in PORTRAITS)
    fallback = "\n".join(
        figure(person, english, deferred=False)
        for person in PORTRAITS if person["id"] in fallback_ids
    )
    markup = (
        '    <div class="banner__portraits">\n'
        '      <div class="banner__track">\n'
        '        <div class="banner__group">\n'
        f'{figures}\n'
        '        </div>\n'
        '      </div>\n'
        '      <noscript>\n'
        '        <div class="banner__fallback">\n'
        f'{fallback}\n'
        '        </div>\n'
        '      </noscript>\n'
        '    </div>\n'
    )
    source = source[:start] + markup + source[end:]
    import re
    source = re.sub(r"assets/(style\.css|banner\.js)\?v=[^\"]+", rf"assets/\1?v={VERSION}", source)
    page.write_text(source)

items = []
for person in PORTRAITS:
    kind = {"sculpture": "雕像照片 / Sculpture photograph", "imagined": "后世画像 / Later imagined portrait"}.get(person.get("kind"), "")
    detail = f"<br>{kind}" if kind else ""
    if person.get("note"):
        detail += f'<br>{esc(person["note"])}'
    items.append(
        f'      <li><strong>{esc(person["zh"])} / {esc(person["en"])}</strong><br>'
        f'{esc(person["creator"])}{detail}<br>'
        f'<a href="{esc(person["licenseUrl"])}">{esc(person["license"])}</a> · '
        f'<a href="{esc(person["source"])}">原始来源 / Source</a></li>'
    )

(ROOT / "credits.html").write_text('''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>肖像来源 · Image credits · Zhuo Zheng</title>
  <meta name="description" content="首页肖像的作者、许可与图片来源。">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="assets/style.css?v=''' + VERSION + '''">
</head>
<body>
  <main class="credits-page">
    <a href="./">← 中文主页</a> · <a href="en.html" lang="en">English homepage</a>
    <h1>肖像来源 <span lang="en">/ Image credits</span></h1>
    <p>首页横幅按下列来源所列许可使用肖像，图片已缩放与压缩，通过 CSS 统一灰度与显示范围。古代人物的后世画像、雕像照片在各条目中注明。</p>
    <p lang="en">Portraits are used under the licenses listed below. Images are resized and compressed; grayscale and framing are applied with CSS. Later imagined portraits and photographs of sculptures are identified individually.</p>
    <ol class="credits-list">
''' + "\n".join(items) + '''
    </ol>
  </main>
</body>
</html>
''')

lines = [
    "# Selected portrait credits", "",
    f"The homepage displays these {len(PORTRAITS)} selected people in a new random order on each load.",
    "Images are resized and WebP-compressed; grayscale and framing are applied with CSS.",
    "", "| File | Subject | Creator | License | Source | Type |",
    "| --- | --- | --- | --- | --- | --- |",
]
for person in PORTRAITS:
    lines.append(
        f'| {Path(person["file"]).name} | {person["zh"]} / {person["en"]} | '
        f'{person["creator"]} | [{person["license"]}]({person["licenseUrl"]}) | '
        f'[Commons]({person["source"]}) | {person.get("kind", "portrait")}; {person.get("note", "")} |'
    )
(ROOT / "assets/portraits/ATTRIBUTIONS.md").write_text("\n".join(lines) + "\n")
print(f"Updated bilingual pages and credits for {len(PORTRAITS)} portraits.")
