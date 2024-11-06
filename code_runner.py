import subprocess

def run_code(file_path: str):
    """执行指定路径的代码文件"""
    try:
        result = subprocess.run(["python", file_path], capture_output=True, text=True)
        if result.stderr:
            print("Execution Error:", result.stderr)
        else:
            print("Execution Result:", result.stdout)
    except Exception as e:
        print("Error executing code:", e)
