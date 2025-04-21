from langchain_community.document_loaders import WebBaseLoader

# 基本用法示例
# loader = WebBaseLoader("https://en.wikipedia.org/wiki/LangChain")
# docs = loader.load()
# print(docs[0].page_content)

# # 带参数配置示例
# loader = WebBaseLoader(
#     web_paths=["https://en.wikipedia.org/wiki/LangChain"],
#     continue_on_failure=False,
#     requests_per_second=2
# )
# docs = loader.load()
# print(f"Loaded {len(docs)} documents")

# CSDN博客示例
loader = WebBaseLoader("https://blog.csdn.net/scaFHIO/article/details/145718716")
docs = loader.load()
print(f"CSDN博客内容:\n{docs[0].page_content}")