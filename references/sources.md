# 来源、许可证与取舍

核查日期：2026-11-05。以下为阅读原始文档后提炼的自包含指南，不是安装四个外部技能；未执行其脚本。不依赖原项目路径、服务或工具别名，不修改其他技能和绘本成品。

| 来源 | 已读及采用 | 不直接继承 |
| --- | --- | --- |
| [Picture Book Generator](https://github.com/kangqiang1996-bot/picture-book-generator/tree/abaa8be97a1ac06e9968b1313258a1dc314e32b7) | SKILL、角色连续性参考；故事因果、图文契约、场景锚点、道具状态、最小修复 | 固定年龄/页数、强制MVP/商业发布、默认三语底条、固定HTML交付、封面必须由模型写字 |
| [Kids Book Writer](https://github.com/jamesrochabrun/skills/tree/2482c176372299c92af01f8414a67172f324e8db/skills/kids-book-writer) | SKILL和年龄指南相关段落；先故事后押韵、自然朗读、重复互动、具体动作 | 英语词数、phonics和音步不当中文要求；年龄能力表和注意力数字不当发展诊断或硬性规则 |
| [Font Aesthetics](https://github.com/Greatbeing/font-aesthetics) | 公开SKILL、LICENSE；含义/情绪到笔触、形态、材料及视觉层级，主要供封面 | 不套概念海报文字占比、强制字形变形或禁用普通字体；正文仍用统一真实授权字体 |
| [CJK Layout](https://github.com/sichengchen/cjk-layout-skills) | cjk-layout/SKILL、Chinese Layout、Standards Map、LICENSE；地区、字形覆盖、中文标点断行、真实渲染验证 | 不强制网页CSS、悬挂标点、日文/韩文习惯或拼音，不把清单通过当作符合全部标准 |

前两项本机下载记录为仅下载未安装；本次核对SKILL哈希与记录吻合，并读取固定修订的公开原文：

- Picture Book Generator SHA256：75a17c3f96069256583e5b3847b9955f7dae516e749c6333a396ed6d65665a38。
- Kids Book Writer SHA256：82747ab51c17e5eae2ed234c6600fc7edbc9bc2b66bf0b30cc8b894eeb7de834。

Font Aesthetics为master，CJK Layout为main，正文与LICENSE均已读取；提交ID接口未取到结果，故记录分支及日期，不虚构固定提交，也不宣称读过全部扩展模块。

四项实际LICENSE均为MIT；版权与完整许可正文保存在[Picture Book Generator许可](licenses/picture-book-generator.txt)、[Kids Book Writer许可](licenses/kids-book-writer.txt)、[字体排版来源许可](licenses/typography-sources.txt)。不随本技能分发第三方字体、插画、照片或可执行程序；各素材授权须按项目核实。

中文规则原始依据为[W3C中文排版需求CLReq](https://www.w3.org/TR/clreq/)，按实际需求阅读字体与字形、行首行尾禁则、不可分标点和混排相关章节，区分规范、地区习惯与渲染器支持。

本技能以儿童绘本目标协调冲突：自然留白优先于默认文字条，正文可编辑与可校对优先于逐页生字，身份连续性不冻结情绪，用户当前范围优先于整本流水线。四个来源是参考，不是假称已经可调用的依赖。
