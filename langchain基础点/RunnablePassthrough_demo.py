from langchain_core.runnables import RunnablePassthrough, RunnableLambda

# 模拟数据库查询函数
def query_user_info(username):
    # 这里应该是实际的数据库查询逻辑
    return {
        "age": 25,
        "location": "北京"
    }

# 创建复杂处理链
complex_chain = (
    {
        "username": RunnablePassthrough(),  # 保留原始用户名
        "user_info": lambda x: query_user_info(x)  # 查询用户信息
    }
    | RunnableLambda(lambda x: f"用户 {x['username']} 的信息：年龄 {x['user_info']['age']}, 所在地 {x['user_info']['location']}")
)

# 使用链
result = complex_chain.invoke("小明")
print(result)