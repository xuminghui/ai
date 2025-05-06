from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.prompts import chat
from langchain_openai.chat_models import ChatOpenAI
import os


llm = ChatOpenAI(
    temperature=0.1,
    model="glm-4",
    openai_api_key=os.getenv("ZHIPU_API_KEY"),
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/",
    max_retries=2,  # 显式设置重试次数
    metadata={"response_format": {"type": "json_object"}}
)
llm.bind()
chatPromptTemplate=ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])
content=chatPromptTemplate.format_messages(input="Hello, how are you?")
response=llm.invoke(content)
print(response)
