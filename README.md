# AutoScriptor
这个项目可以自动化写代码并运行
# 项目名称: LLM-Based Code Generation Tool

## 简介

该项目是一个基于大型语言模型（LLM）的代码生成工具。通过接口调用 LLM（例如 GLM-4-flash 模型），用户可以生成 Python 代码片段并将其保存到指定的文件中，同时也能够自动执行生成的代码。这个工具非常适合想要通过 AI 来快速编写代码的开发者。

## 目录结构

```
project-root/
├── main.py                # 主脚本，调用 LLM API 生成代码并保存到目标文件
├── llm_client.py          # 调用 LLM API 的客户端模块，用于生成代码
├── code_runner.py         # 负责执行生成的代码
├── config.py              # 配置文件，管理 API 密钥、文件路径和其他参数
└── requirements.txt       # Python 依赖文件
```

## 文件说明

- **`main.py`**: 主入口脚本，通过调用 LLM API 生成代码，将其保存到指定文件，并执行生成的代码。
- **`llm_client.py`**: 封装了与 LLM API 的交互逻辑，处理代码生成请求。
- **`code_runner.py`**: 用于执行生成的 Python 代码，并返回执行结果。
- **`config.py`**: 存储 API 密钥、基础 URL、模型名称以及目标文件路径等配置。
- **`requirements.txt`**: 包含项目所需的 Python 库依赖。

## 使用说明

### 1. 克隆项目

首先，克隆此 GitHub 项目到本地：

```bash
git clone https://github.com/your_username/LLM-Code-Generation-Tool.git
cd LLM-Code-Generation-Tool
```

### 2. 安装依赖

使用以下命令安装所需的 Python 库依赖：

```bash
pip install -r requirements.txt
```

### 3. 配置 API 密钥

在 `config.py` 中设置你的 API 密钥和基础 URL：

```python
# config.py
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://open.bigmodel.cn/api/paas/v4/"
MODEL_NAME = "GLM-4-flash"
```

确保将 `API_KEY` 替换为你的有效 API 密钥。

### 4. 运行主脚本

使用以下命令运行主脚本 `main.py`，它会调用 LLM 生成代码并将其保存到目标文件中：

```bash
python main.py
```

运行脚本后，代码将被生成并保存在目标文件 `target_code.py` 中，同时会自动执行生成的代码并在控制台显示结果。

## 示例

假设在 `main.py` 中的提示词是 `# 请为我生成一个Python函数来计算斐波那契数列`，运行后，生成的代码可能如下：

```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci(10))
```

控制台将输出斐波那契数列的结果：

```
Execution Result: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

## 注意事项

1. **API 调用限制**: 请注意使用 LLM API 时的调用次数和速率限制，避免过度使用导致 API 被限流。
2. **错误处理**: 如果 API 调用失败，程序会输出错误信息。请确保 API 密钥和配置正确，且网络连接稳定。

## 贡献

欢迎任何形式的贡献！如果你有任何改进建议或发现问题，可以提交 issue 或创建 pull request。

## 许可证

本项目使用 MIT 许可证。详见 [LICENSE](./LICENSE) 文件。

## 联系方式

如果有任何问题，请联系项目作者：
- GitHub: [guangxiangdebizi](https://github.com/guangxiangdebizi)
- Email: guangxiangdebizi@gmail.com

