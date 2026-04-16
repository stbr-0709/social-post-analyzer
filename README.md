markdown
# 社媒帖子分析工具

> 一款面向游戏运营/社媒运营的 AI 文案分析工具，自动评估帖子互动潜力、推荐话题标签与发布平台。

## 🎯 项目背景

在海外社媒运营工作中，每天需要产出大量帖子。这个工具可以帮助运营同学：
- 快速判断帖子互动潜力
- 获得标签与平台建议
- 发现文案优化方向

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 📈 互动率预测 | 高/中/低三档评估 + 原因分析 |
| 🏷️ 标签推荐 | 自动生成 5 个相关话题标签 |
| 📱 平台建议 | TikTok / Instagram / Twitter / Facebook 适配建议 |
| 💡 优化建议 | 1-2 条具体可执行的改进方向 |

## 🛠️ 技术栈

- Python 3.14+
- DeepSeek API（兼容 OpenAI SDK）
- 支持 HTTP 代理（国内网络友好）

## 📦 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/你的用户名/social-post-analyzer.git
cd social-post-analyzer
2. 安装依赖
bash
pip install openai
3. 配置 API Key
访问 DeepSeek Platform 注册并获取 API Key

在 post_analyzer.py 中替换 API_KEY 变量

4. 运行
bash
python post_analyzer.py
📝 使用示例
输入：

text
新英雄「影刃」明日上线！首周抽卡概率UP，评论晒图抽3张月卡~
输出：

text
【互动率预测】高
原因：包含“新英雄”、“抽卡UP”、“抽奖”等高互动关键词

【推荐话题标签】
1. #新英雄
2. #抽卡UP
3. #游戏福利
4. #月卡抽奖
5. #明日上线

【建议平台】
- TikTok：推荐
- Instagram：推荐
- Twitter：推荐
- Facebook：推荐

【优化建议】
1. 加上具体时间（如“明早10点”），制造紧迫感
2. 增加 UGC 引导，如“评论区晒出你的阵容”
🔧 代理配置（国内用户）
如遇网络问题，在 PowerShell 中设置：

powershell
$env:HTTP_PROXY="http://127.0.0.1:你的端口"
$env:HTTPS_PROXY="http://127.0.0.1:你的端口"
📂 文件结构
text
social-post-analyzer/
├── post_analyzer.py    # 主程序
└── README.md           # 项目说明
👤 关于我
我是刘艺璇，游戏运营 / 海外社媒运营方向，擅长用 AI 和数据分析提升运营效率。

📁 作品集网站

📧 liuyixuan20240225@163.com

🐙 GitHub: [你的用户名]

📄 许可证
MIT License

text

---

## 使用步骤：

1. 打开你的 GitHub 仓库 `social-post-analyzer`
2. 点击 **Add a README** 或点击 **README.md** 旁边的铅笔图标 ✏️
3. **删除**默认内容，**粘贴**上面的代码
4. 把 `你的用户名` 改成你的真实 GitHub 用户名
5. 点击 **Commit changes**（绿色按钮）

---

## 同时更新你的个人主页 README

把你之前个人主页（`liuyixuan` 仓库）的 README 表格里的项目链接补上：

```markdown
| [社媒帖子分析工具](https://github.com/你的用户名/social-post-analyzer) | AI 分析互动率、推荐标签 | Python + DeepSeek API |
