from langchain_community.chat_models.zhipuai import ChatZhipuAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, Runnable
from dotenv import load_dotenv
import os

# 加载环境变量
# 确保在项目根目录下有一个 .env 文件，其中包含 ZHIPU_API_KEY=your_zhipu_api_key
# 或者直接在代码中设置 ZHIPU_API_KEY 环境变量，例如：
# os.environ["ZHIPU_API_KEY"] = "your_zhipu_api_key"     
# 或者使用 load_dotenv() 加载 .env 文件，例如：
# load_dotenv()  # 从 .env 文件加载环境变量
load_dotenv() 


# 初始化智谱AI
llm = ChatZhipuAI(
    model_name="glm-4",  # 或 "glm-3-turbo"
    temperature=0.7,
    api_key=os.getenv("ZHIPU_API_KEY")
    #export ZHIPU_API_KEY=8cf4efc687e84d2aad2e663488221d26.x8BLO7JsMtSEglxt

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
