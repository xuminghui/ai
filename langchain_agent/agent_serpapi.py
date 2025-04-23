#注意在安装google-search-results包时，遇到了一个问题：提示需要pip install google-search-results
#但我已经安装了这个包，但是还是提示需要pip install google-search-results
#最后我pip uninstall google-search-results，然后再pip install google-search-results就可以了,原因是google-search-results包的版本问题

from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI
#from langchain.agents import load_tools 
# 和 from langchain_community.agent_toolkits.load_tools import load_tools 
# 的变更是在 LangChain 的 0.0.200 版本中引入的。这个变更是为了将社区贡献的工具和功能模块化，并移入独立的 langchain_community 模块中，以更好地组织代码。
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_community.utilities import SerpAPIWrapper
from langchain_core.tools import Tool
from langchain_community.utilities import SerpAPIWrapper



import os
load_dotenv()
# 初始化 ZhipuAI LLM
llm = ChatOpenAI(
    temperature=0.1,
    model="glm-4",
    openai_api_key=os.getenv("ZHIPU_API_KEY"),
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/",
    max_retries=2,  # 显式设置重试次数
    metadata={"response_format": {"type": "json_object"}}
)

# 初始化 SerpAPI 工具
# 确保在项目根目录下有一个.env 文件，其中包含 SERPAPI_API_KEY=your_serpapi_api_key
# 这种方式的好处是：
# 1. 安全：敏感信息（如 API 密钥）不会暴露在代码中。
# 2. 可维护：环境变量的管理变得更加集中和易于管理。
# 3. 可扩展性：可以轻松地在不同环境中切换 API 密钥，而无需修改代码。
# 4. 环境隔离：不同的环境（如开发、测试、生产）可以使用不同的环境变量。
# 5. 版本控制：.env 文件可以安全地添加到版本控制中，避免将敏感信息暴露在代码库中。
#tools = load_tools(["serpapi"])  # 直接加载已配置的SerpAPI工具

# You can create the tool to pass to an agent
params = {
    "engine": "google", # or bing
    "gl": "us",
    "hl": "en",
}
search = SerpAPIWrapper(params=params)
# 修改工具初始化部分（第43-51行）
# 原错误代码：
# tools = Tool(
#     name="web search",
#     description="Search the web for information",
#     func=search.run,
# )

# 正确写法：
tools = [
    Tool(
        name="web_search",
        func=search.run,
        description="用于搜索网络信息的工具"
    )
]

# 初始化 Agent
agent = initialize_agent(
    tools, 
    llm, 
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True)

# 新增代码：打印提示词模板
print("=== ReAct提示词模板 ===")
print(agent.agent.llm_chain.prompt.template)
print(agent.agent.llm_chain.prompt.input_variables)
print("======================")

# 用户提问
query = "今天北京朝阳区天气如何？"

result = agent.invoke(query)
print(f"SerpAPI Result: {result}")