# 郑卓 · Zhuo Zheng

个人主页：<https://zhuozheng2006.github.io/>

## 页面

- `index.html`：中文首页。
- `en.html`：英文首页，内容与中文保持同步。
- `assets/style.css`：响应式布局、字体与配色。
- `assets/banner.js`：肖像每次载入时随机排序，以 42px/s 无缝横向循环；遵循系统减少动态效果偏好。
- `photo.jpg`：个人照片。
- `assets/portraits/`：顶部哲学家、文学家与科学家肖像，随站点保存，来源记录见该目录的 `ATTRIBUTIONS.md`。
- `credits.html`：图片作者、年代与原始来源。
- `404.html`：找不到页面时的引导。
- `sitemap.xml`、`robots.txt`：搜索引擎索引。

这是一个无需构建的静态网站。公式使用浏览器原生 MathML，字体使用系统字体，不依赖第三方脚本、字体或公式 CDN。

## 本地预览

```sh
python3 -m http.server 8000
```

访问 <http://localhost:8000>。修改个人介绍或项目时，请同时更新中英文页面。

## 发布

GitHub 仓库的 **Settings → Pages** 使用 **Deploy from a branch**，分支为 **main**，目录为 **/(root)**。`.nojekyll` 使静态文件直接发布。以后提交到 `main` 后，GitHub Pages 会自动更新网站。

新增论文或其他成果时，再加入对应栏目，避免显示空白栏目或未经核实的占位信息。

## 肖像维护

横幅使用已选定的 49 位哲学家、文学家与科学家（含哥德尔、庞加莱，以及保留的奥古斯丁、阿奎那、哈贝马斯、伽罗瓦、希尔伯特、格罗滕迪克）。
`assets/portraits/portraits.json` 保存名单、来源、许可与图片尺寸；更新后运行 `python3 scripts/update_portraits.py` 同步中英文页面和署名。
图片按显示需求压缩，首屏优先加载，其余在接近可视区时加载；无 JavaScript 时显示静态肖像。
