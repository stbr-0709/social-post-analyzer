# -*- coding: utf-8 -*-
import openai
import sys
import io

# 设置标准输出编码为 UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 配置 API
API_KEY = "sk-8bf021c3ab5d42fb94e6f281644ac161"  #
client = openai.OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

def analyze_post(post_content):
    prompt = f"""你是一个游戏行业的海外社媒运营专家。请分析下面的社媒帖子文案：

---
{post_content}
---

请按照以下格式输出：

【互动率预测】（高/中/低）
原因：

【推荐话题标签】（5个）
1. 
2. 
3. 
4. 
5. 

【建议平台】
- TikTok：
- Instagram：
- Twitter：
- Facebook：

【优化建议】
1.
2."""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是游戏行业社媒运营专家。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content

def main():
    print("=" * 50)
    print("社媒帖子分析工具 v1.0")
    print("输入帖子文案，输入 q 退出")
    print("=" * 50)
    
    while True:
        print("\n请输入帖子文案：")
        content = input("> ")
        
        if content.lower() == 'q':
            print("再见！")
            break
        
        if len(content.strip()) < 5:
            print("文案太短，再写多点吧")
            continue
        
        print("\n分析中...\n")
        try:
            result = analyze_post(content)
            print(result)
        except Exception as e:
            print(f"错误：{e}")

if __name__ == "__main__":
    main()