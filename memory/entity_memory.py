from langchain.memory import ConversationEntityMemory
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()  # 加载.env文件中的环境变量，包括API密钥和其他配置



# 使用需要input参数的memory类型
llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4",
    openai_api_key=os.getenv("ZHIPU_API_KEY"),
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)

#验证模型是否具备实体识别能力
test_prompt = "从这句话中提取实体：张三的订单TB20230901从杭州仓库发出"
response = llm.invoke(test_prompt)
print(f"模型响应：{response.content}")

memory = ConversationEntityMemory(llm=llm,input_key="input")
memory.save_context({"input": "张三的订单TB20230901情况"}, {"output": "订单TB20230901从杭州仓库发出"})

# 打印中间处理结果 目前这个入参，拿到的结果是空
print("实体存储缓存:", memory.entity_cache)
print("实体缓存关系:", memory.entity_store.store)


# 当输入包含实体时，会自动过滤相关记忆
# 需要模型具备实体识别能力？
print(memory.load_memory_variables({"history":"订单"}))
# 输出：{'history': 'Human: 张三的年龄？\nAI: 张三25岁', 'entities': {'张三': '25岁'}}