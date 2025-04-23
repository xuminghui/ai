#使用google serpapi搜索工具
from langchain_community.utilities import SerpAPIWrapper

params = {
    "engine": "google",
    "gl": "us",
    "hl": "en",
}
search = SerpAPIWrapper(params=params)
search_result=search.run("2025年4月，有两国总统同天抵达北京，是哪两国的总统")
print(search_result)   

