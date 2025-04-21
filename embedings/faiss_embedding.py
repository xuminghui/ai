#使用zhipuai的embedding
from langchain_community.embeddings import ZhipuAIEmbeddings
#加载器
from langchain_community.document_loaders import TextLoader
#分割器
from langchain_text_splitters import CharacterTextSplitter

#导入FAISS库
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()
loader = TextLoader("embedings/demo.txt")
document=loader.load()
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = text_splitter.split_documents(document)
#初始化模型
embeddings = ZhipuAIEmbeddings(model="embedding-3",api_key=os.getenv("ZHIPU_API_KEY"))
#创建向量数据库
vector_store = FAISS.from_documents(docs, embeddings)
#查询
query = "人工智能"
docs = vector_store.similarity_search(query)
print(docs[0].page_content)
