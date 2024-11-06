import llm_client
from config import TARGET_FILE_PATH
import code_runner

if __name__ == "__main__":
    # 调用 LLM 生成代码
    prompt = "# 请为我生成一个Python函数来计算斐波那契数列"
    generated_code = llm_client.complete_code(prompt)

    # 将生成的代码写入目标文件
    if generated_code:
        with open(TARGET_FILE_PATH, "w") as f:
            f.write(generated_code)
        print("Code generated and saved to", TARGET_FILE_PATH)

        # 执行生成的代码
        code_runner.run_code(TARGET_FILE_PATH)
    else:
        print("Failed to generate code.")
