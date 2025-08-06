import os

def load_env():
    # 加载环境变量
    for line in open(".env"):
        key, value = line.strip().split("=")
        os.environ[key] = value

def getenv(key, default=None):
    # 获取环境变量
    return os.getenv(key, default)