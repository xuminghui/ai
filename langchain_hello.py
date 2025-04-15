from langchain_community.chat_models.zhipuai import ChatZhipuAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, Runnable
from dotenv import load_dotenv
import os

# 加载环境变量
# 确保在项目根目录下有一个 .env 文件，其中包含 ZHIPU_API_KEY=your_zhipu_api_key 
#使用 load_dotenv() 加载 .env 文件，例如：
# load_dotenv()  # 从 .env 文件加载环境变量
# 好处：
# 1. 安全：敏感信息（如 API 密钥）不会暴露在代码中。
# 2. 可维护：环境变量的管理变得更加集中和易于管理。
# 3. 可扩展性：可以轻松地在不同环境中切换 API 密钥，而无需修改代码。
# 4. 环境隔离：不同的环境（如开发、测试、生产）可以使用不同的环境变量。
# 5. 版本控制：.env 文件可以安全地添加到版本控制中，避免将敏感信息暴露在代码库中。
# 6. 跨平台：可以在不同的操作系统上使用相同的环境变量配置。
# 7. 简化部署：部署时只需提供 .env 文件，而无需手动设置环境变量。
# 8. 提高安全性：避免在代码中硬编码敏感信息。
# 9. 减少错误：避免在代码中硬编码敏感信息，减少错误的可能性。
# 10. 提高可读性：代码更易于阅读和理解。

load_dotenv() 


# 初始化智谱AI
# 如何这里换成 ChatOpenAI 会报错？
# 1. 确保你的环境中已经安装了 openai 库。
# 2. 确保你的环境变量中包含 OPENAI_API_KEY=your_openai_api_key
# 3. 确保你的代码中包含 import openai
# 4. 确保你的代码中包含 openai.api_key = os.getenv("OPENAI_API_KEY")        
# 5. 确保你的代码中包含 model_name="gpt-3.5-turbo"
# 6. 确保你的代码中包含 temperature=0.7
# 7. 确保你的代码中包含 api_key=os.getenv("OPENAI_API_KEY") 
llm = ChatZhipuAI(
    model_name="glm-4",  # 或 "glm-3-turbo"
    temperature=0.7,
    # 确保你的 .env 文件中包含 ZHIPU_API_KEY=your_zhipu_api_key
    # 为什么要使用 os.getenv("ZHIPU_API_KEY") 而不是直接使用 "your_zhipu_api_key"？
    # 1. 安全性：使用 os.getenv("ZHIPU_API_KEY") 可以确保敏感信息（如 API 密钥）不会暴露在代码中。 
    # 2. 可维护性：使用 os.getenv("ZHIPU_API_KEY") 可以将敏感信息从代码中分离出来，使代码更易于维护和更新。
    # 3. 可扩展性：使用 os.getenv("ZHIPU_API_KEY") 可以轻松地在不同环境中切换 API 密钥，而无需修改代码。
    # 4. 环境隔离：不同的环境（如开发、测试、生产）可以使用不同的环境变量。
    # 5. 版本控制：.env 文件可以安全地添加到版本控制中，避免将敏感信息暴露在代码库中。
    # 6. 跨平台：可以在不同的操作系统上使用相同的环境变量配置。
    # 7. 简化部署：部署时只需提供.env 文件，而无需手动设置环境变量。
    api_key=os.getenv("ZHIPU_API_KEY") 
)

# 创建一个简单的提示模板
prompt = ChatPromptTemplate.from_template("你好，{name}！欢迎来到 LangChain 的世界！")

# 创建链
chain = (
    {"name": RunnablePassthrough()} 
    | prompt 
    | llm 
    | StrOutputParser()
)

# 运行带前缀的链
result = chain.invoke("小明")
print(result)
