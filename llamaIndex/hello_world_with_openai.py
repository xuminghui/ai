# deepseek 官网说明 https://api-docs.deepseek.com/zh-cn/
#DeepSeek API 使用与 OpenAI 兼容的 API 格式，通过修改配置，您可以使用 OpenAI SDK 来访问 DeepSeek API    

#借助langchain，我们就可以实现使用OpenAI的SDK来访问DeepSeek API
from llama_index.llms.openai_like import OpenAILike

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,Settings
import os
from dotenv import load_dotenv
from llama_index.embeddings.zhipuai import ZhipuAIEmbedding
from llama_index.llms.deepseek import DeepSeek

load_dotenv()

Settings.llm = OpenAILike(
    model="deepseek-chat",
    api_base="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    context_window=128000,
    is_chat_model=True,
    is_function_calling_model=True,
)
Settings.embed_model = ZhipuAIEmbedding(model="embedding-3",api_key=os.getenv("ZHIPU_API_KEY"))
documents = SimpleDirectoryReader("llamaIndex/data/source_files").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query(
    "the author's experiences,please answer in Chinese"
)
print(response)