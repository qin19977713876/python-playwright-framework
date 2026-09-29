import os


class Config:
    """全局配置，所有环境相关的参数都从这里取。"""

    # 被测系统地址
    BASE_URL = os.getenv("BASE_URL", "https://www.bing.com")
    API_BASE = os.getenv("API_BASE", "https://jsonplaceholder.typicode.com")

    # 浏览器
    BROWSER = os.getenv("BROWSER", "chromium")
    HEADLESS = os.getenv("CI") == "true"
    SLOW_MO = 0

    # 超时（毫秒）
    TIMEOUT = 10000
    API_TIMEOUT = 15000