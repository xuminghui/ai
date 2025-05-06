from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,Settings
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from llama_index.llms.langchain import LangChainLLM
from langchain_community.embeddings import ZhipuAIEmbeddings
load_dotenv()

print(os.getenv("DEEPSEEK_API_KEY"))
from llama_index.llms.deepseek import DeepSeek

llm = DeepSeek(model="deepseek-chat", api_key=os.getenv("DEEPSEEK_API_KEY"))
# 配置DeepSeek模型
# deepseek_llm = OpenAI(
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com/v1", # DeepSeek专用端点
#     model="deepseek-chat",
#     temperature=0.1
# )
# llm = LangChainLLM(deepseek_llm)

Settings.embed_model = ZhipuAIEmbeddings(model="embedding-3",api_key=os.getenv("ZHIPU_API_KEY"))
# deepseek_llm = OpenAI(
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com/v1",
#     model="deepseek-reasoner",
#     temperature=0.1
# )
Settings.llm = llm
documents = SimpleDirectoryReader("llamaIndex/data/source_files").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query(
    "the author's experiences,please answer in Chinese"
)
print(response)
