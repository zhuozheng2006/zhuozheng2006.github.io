# 郑卓 · Zhuo Zheng

个人网站，包含个人介绍、项目与学习笔记，提供中英文版本。

[中文主页](https://zhuozheng2006.github.io/) · [English](https://zhuozheng2006.github.io/en.html)

## 本地预览

无需构建或安装依赖，在仓库目录运行：

```sh
python3 -m http.server 8000
```

打开 <http://localhost:8000>。

要同时预览经纬纪，先运行 `git submodule update --init meridian-atlas` 下载站点锁定的图集版本，再打开 <http://localhost:8000/meridian-atlas/>。

## 维护

- 页面内容：`index.html` 和 `en.html`，修改时同步两个语言版本。
- 样式与交互：`assets/style.css` 和 `assets/banner.js`。
- 肖像：名单与来源保存在 `assets/portraits/portraits.json`；运行 `python3 scripts/update_portraits.py` 同步页面与署名。
- 公式：运行 `python3 scripts/build_formulas.py` 重新生成 SVG，需要 LaTeX 和 dvisvgm。

网站通过 GitHub Pages 从 `main` 分支根目录发布，提交后自动更新。

[经纬纪](https://zhuozheng2006.github.io/meridian-atlas/) 使用图集仓库 `atlas-pages` 分支的静态文件。更新上线版本时，在本站仓库运行 `git submodule update --init --remote meridian-atlas`，预览确认后提交 `meridian-atlas` 指针。

## 图片来源

肖像作者、许可与原始来源见 [图片署名](assets/portraits/ATTRIBUTIONS.md)。
