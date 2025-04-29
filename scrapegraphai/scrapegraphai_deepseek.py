from scrapegraphai.graphs import SmartScraperGraph

# 配置DeepSeek模型
# https://github.com/ScrapeGraphAI/ScrapegraphLib-Examples/tree/main/deepseek

DEEPSEEK_APIKEY = "your-api-key-here"  # 替换为实际API密钥
graph_config = {
    "llm": {
        "api_key": "sk-bf62f9a952f2479d9d87788605b23189",
        "model": "deepseek-chat",  # 根据实际模型名称调整
        "temperature": 0.3
        #"base_url": "https://api.deepseek.com/v1"  # 官方API端点
    },
    "verbose": True,
    "headless": True,
    "timeout": 30
}

# 创建抓取管道
smart_scraper = SmartScraperGraph(
    prompt="提取页面所有文章标题和摘要，用中文输出",
    source="https://perinim.github.io/projects/",
    config=graph_config
)

# 执行抓取并打印结果
try:
    result = smart_scraper.run()
    print(result)
except Exception as e:
    print(f"抓取失败: {str(e)}")