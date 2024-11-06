from config import client, MODEL_NAME

def complete_code(code: str) -> str:
    """调用 GLM-4-flash 模型生成代码补全"""
    prompt = code + "\n# 请补全代码"

    try:
        # 调用 GLM-4-flash 模型生成代码
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "你是一个资深的Python程序员，帮助补全用户给出的代码片段"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.5,
            stream=False
        )
        completed_code = response.choices[0].message.content.strip()
        return completed_code
    except Exception as e:
        print("Error calling LLM:", e)
        return ""
