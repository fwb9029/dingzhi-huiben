# 定制绘本

用于定制儿童绘本的故事、逐页分镜、角色连续插画、中文排版和成品检查。它把不同公开 Skill 中适用的方法整理为一套可独立阅读的工作指南，也可以只处理故事、单页修改或已有绘本审查。

## 使用方式

下载完整目录，按照所用 AI 助手的技能导入方式添加 `picture-book`。保留 `SKILL.md` 与 `references/`、`scripts/`、`agents/` 的相对结构；无需另外安装来源中列出的四个外部 Skill。

可以从这样的需求开始：

```text
请使用 picture-book 帮我制作一本中文两岁生日绘本。
主角、家人称呼和想留下的小事由我提供。
先给故事与逐页文字、画面安排，再确定人物和画风。
确认后先试做一页无字插画，再单独排中文。
```

也可以只要求“修改这两页的字体，保留插画和原文”，或“审查现有绘本，先列问题”。具体家庭信息和单本故事留在各自项目资料中。

## 方法与取舍

- 故事以年龄、共读场景和真实定制信息为依据，保留自然朗读、具体动作和互动；不直接套用英语词数或固定页数。
- 通过人物、场景、动作及道具状态保持连续性，表情和构图随情节变化。
- 优先制作无字插画，在自然留白处独立排中文；修改文字时尽量复用合格插画。
- 封面字体配合故事情绪，正文首先清晰、协调、可修改；导出后检查实际页面。

## 文件

```text
SKILL.md
agents/openai.yaml
references/
  story-and-continuity.md
  typography.md
  project-and-qa.md
  sources.md
  licenses/
scripts/check_book_manifest.py
```

故事与分镜可以只输出文字。生成插画、排字和渲染文件需要使用环境具备相应能力；本仓库不包含图像生成服务、第三方字体或家庭素材。

## 可选检查脚本

检查脚本只用 Python 3 标准库，读取绘本项目中的清单文件：

```bash
python scripts/check_book_manifest.py path/to/book-manifest.json
python scripts/check_book_manifest.py path/to/book-manifest.json --complete
```

清单格式和检查范围见 [工程与验收](references/project-and-qa.md)。脚本核对文件、字体引用、记录与导出声明，不代替逐页目检，也不验证字形覆盖或自动证明素材授权。

## 来源与许可记录

参考来源、采用的方法与未继承的要求见 [来源与取舍](references/sources.md)。随附的第三方许可正文保存在 [references/licenses](references/licenses/) 中。

本目录仅包含 Skill 指南、参考资料和检查脚本，不包含绘本成品、儿童照片、实际字体文件或登录凭据。
