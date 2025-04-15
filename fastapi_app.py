from fastapi import FastAPI
from langchain_community.chat_models.zhipuai import ChatZhipuAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 初始化FastAPI应用
app = FastAPI()

# 初始化智谱AI
llm = ChatZhipuAI(
    model_name="glm-4",  # 或 "glm-3-turbo"
    temperature=0.7,
    api_key=os.getenv("ZHIPU_API_KEY")
)

# 创建提示模板
prompt = ChatPromptTemplate.from_template("你好，{name}！欢迎来到 LangChain 的世界！")

# 创建链
chain = (
    {"name": RunnablePassthrough()} 
    | prompt 
    | llm 
    | StrOutputParser()
)

@app.post("/greet")
async def greet(name: str):
    """
    API端点，接收名字参数并返回LangChain生成的问候语
    """
    result = chain.invoke(name)
    return {"message": result}

@app.post("/greet_with_prefix")
async def greet_with_prefix(name: str, prefix: str = "尊敬的"):
    """
    API端点，接收名字和前缀参数，返回带前缀的LangChain问候语
    """
    full_name = f"{prefix}{name}"
    result = chain.invoke(full_name)
    return {"message": result}

@app.get("/")
async def root():
    return {"message": "LangChain FastAPI 服务已启动"}