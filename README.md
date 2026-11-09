# 郑卓 · Zhuo Zheng

个人主页：<https://zhuozheng2006.github.io/>

## 页面

- `index.html`：中文首页。
- `en.html`：英文首页，内容与中文保持同步。
- `assets/style.css`：响应式布局、字体与配色。
- `assets/banner.js`：12 位人物肖像的无缝横向循环、暂停与播放控制；遵循系统减少动态效果偏好。
- `photo.jpg`：个人照片。
- `assets/portraits/`：顶部哲学家与文学家肖像，随站点保存，来源记录见该目录的 `ATTRIBUTIONS.md`。
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
