from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory  # 修改导入的memory类型
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4",
    openai_api_key=os.getenv("ZHIPU_API_KEY"),
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)
memory = ConversationBufferWindowMemory(k=2,memory_key="chat_history", return_messages=True)
memory.save_context({"input": "你好"}, {"output": "你好"})
memory.save_context({"input": "你好吗"}, {"output": "我很好"})

"""
{'chat_history': [
    HumanMessage(content='你好', additional_kwargs={}),
    AIMessage(content='你好', additional_kwargs={})
]} 这里的chat_history就是一个变量key，它的值是一个list，list里面是HumanMessage和AIMessage的对象。
"""
"""
为什么入参是一个"{}"？如果下面的入参包含了参数，请给出示例：

"""
print(memory.load_memory_variables({"input": "abc"}))