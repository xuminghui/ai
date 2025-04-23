from dotenv import load_dotenv
from langchain.agents import initialize_agent
from langchain_openai import ChatOpenAI
#from langchain.agents import load_tools 
# 和 from langchain_community.agent_toolkits.load_tools import load_tools 
# 的变更是在 LangChain 的 0.0.200 版本中引入的。这个变更是为了将社区贡献的工具和功能模块化，并移入独立的 langchain_community 模块中，以更好地组织代码。
from langchain_community.agent_toolkits.load_tools import load_tools
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
tools = load_tools(["serpapi"])  # 直接加载已配置的SerpAPI工具

# 初始化 Agent
agent = initialize_agent(
    tools, 
    llm, 
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True)
    #通过增加容错能力，
    # 使得 AgentExecutor 能够更好地处理 LLM 输出和工具调用中的问题，
    # 从而提高代码的健壮性和执行成功率

# 用户提问
query = "神舟二十号任务是哪一天完成发射前最后一次全区合练？"
result = agent.run(query)
print(f"SerpAPI Result: {result}")