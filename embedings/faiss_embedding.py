#使用zhipuai的embedding
from langchain_community.embeddings import ZhipuAIEmbeddings
#加载器
from langchain_community.document_loaders import DirectoryLoader
#分割器
from langchain_text_splitters import CharacterTextSplitter

#导入FAISS库
from langchain_community.vectorstores import FAISS
import os
from dotenv import load_dotenv

load_dotenv()
# 加载多个文件
loader = DirectoryLoader("embedings", glob="*.txt")
document=loader.load()
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = text_splitter.split_documents(document)
#初始化模型
embeddings = ZhipuAIEmbeddings(model="embedding-3",api_key=os.getenv("ZHIPU_API_KEY"))
#创建向量数据库
vector_store = FAISS.from_documents(docs, embeddings)
#查询
query = "老徐的妻子是谁？"
docs_with_scores= vector_store.similarity_search_with_relevance_scores(query)
for doc, score in docs_with_scores:
    print("Score: ", score)
    print(doc.page_content)
    print("metadata: ",doc.metadata)

