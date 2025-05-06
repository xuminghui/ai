#lnagchain大模型开发AI应用开发实践 11.3  P201
from email import message
import operator
from typing import Annotated, TypedDict, List
from langchain.agents import tool
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv


load_dotenv()

#定义大语言模型
llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4",
    openai_api_key=os.getenv("ZHIPU_API_KEY"),
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)

#定义工具
@tool("get_weather")
def get_weather(location:str)->str:
    return f"今天{location}的天气是晴"

@tool("serp_search") #command+enter 插入新行
def serp_search(query:str)->str:
    return f"搜索到了{query}相关的内容"

#定义智能体提示语

promptTemplate="""帮助用户回答问题
您可以使用以下工具帮忙解决问题


"""
ChatPromptTemplate.from_messages(
    [
        ("system","你是一个非常强大的助手，可以使用各种工具完成人类交给的问题和任务"),
        ("user",promptTemplate),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)
tools=[get_weather,serp_search]


class GState(TypedDict): #TypedDict是一个字典类型，它的键和值都有类型注解。

    messages:Annotated[List, operator.add]

response=llm.invoke("hello")
print(response.content)

new_gstate=GState(messages=["hello"])
print(new_gstate["messages"])
new_gstate["messages"]+=["world"]
print(new_gstate["messages"])

