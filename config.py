from openai import OpenAI

# OpenAI API 配置
API_KEY = "Your_Apikey"
BASE_URL = "Your_Url"
MODEL_NAME = "Your_model"

# 初始化 OpenAI 客户端
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 监控的目标文件路径
TARGET_FILE_PATH = "target_code.py"
