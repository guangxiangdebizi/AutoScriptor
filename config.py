from openai import OpenAI

# OpenAI API 配置
API_KEY = "962da72c3cb62b09521923cfefabafc6.oyAzeB72sEIJpWDr"
BASE_URL = "https://open.bigmodel.cn/api/paas/v4/"
MODEL_NAME = "GLM-4-flash"

# 初始化 OpenAI 客户端
client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# 监控的目标文件路径
TARGET_FILE_PATH = "target_code.py"
