# 郑卓 · Zhuo Zheng

个人网站，包含个人介绍、项目与学习笔记，提供中英文版本。

[中文主页](https://zhuozheng2006.github.io/) · [English](https://zhuozheng2006.github.io/en.html)

## 本地预览

无需构建或安装依赖，在仓库目录运行：

```sh
python3 -m http.server 8000
```

打开 <http://localhost:8000>。

## 维护

- 页面内容：`index.html` 和 `en.html`，修改时同步两个语言版本。
- 样式与交互：`assets/style.css` 和 `assets/banner.js`。
- 肖像：名单与来源保存在 `assets/portraits/portraits.json`；运行 `python3 scripts/update_portraits.py` 同步页面与署名。
- 公式：运行 `python3 scripts/build_formulas.py` 重新生成 SVG，需要 LaTeX 和 dvisvgm。

网站通过 GitHub Pages 从 `main` 分支根目录发布，提交后自动更新。

## 图片来源

肖像作者、许可与原始来源见 [图片署名](assets/portraits/ATTRIBUTIONS.md)。
