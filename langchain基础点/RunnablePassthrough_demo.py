from langchain_core.runnables import RunnablePassthrough, RunnableLambda

#在构建复杂处理链时作为中间件使用的一个典型场景是： 需要将多个输入参数传递给链，同时保留原始输入数据 。
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
    #- 使用 RunnableLambda 将 lambda 函数包装为 Runnable 对象
    #- 确保 | 操作符后面的部分是一个可调用的对象
    | RunnableLambda(lambda x: f"用户 {x['username']} 的信息：年龄 {x['user_info']['age']}, 所在地 {x['user_info']['location']}")
)

# 使用链
result = complex_chain.invoke("小明")
print(result)