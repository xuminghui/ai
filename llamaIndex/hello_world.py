from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,Settings
import os
from dotenv import load_dotenv
from llama_index.embeddings.zhipuai import ZhipuAIEmbedding
from llama_index.llms.deepseek import DeepSeek

load_dotenv()

Settings.llm = DeepSeek(model="deepseek-chat", api_key=os.getenv("DEEPSEEK_API_KEY"))
Settings.embed_model = ZhipuAIEmbedding(model="embedding-3",api_key=os.getenv("ZHIPU_API_KEY"))
documents = SimpleDirectoryReader("llamaIndex/data/source_files").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query(
    "the author's experiences,please answer in Chinese"
)
print(response)
