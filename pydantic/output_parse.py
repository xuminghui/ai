from langchain.agents import tool
from pydantic import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser

# # 步骤1：定义工具输入模型
# class WordInput(BaseModel):
#     word: str = Field(description="待计算长度的单词")

# # 步骤2：绑定工具与输入模型
# @tool(args_schema=WordInput)
# def get_word_length(word: str) -> int:
#     """返回单词的长度"""
#     return len(word)

# 步骤3：解析LLM的输出为结构化数据
# 这里要注意，agent调用工具会返回word长度，所以LLM的输出应该是一个JSON，包含word和length字段
# 大模型在这里的作用是根据工具返回的word长度，再加上之前的入参word，生成一个JSON

#假设这是大模型返回的一个json结构，这里必须用BaseModel来定义
class LengthResponse(BaseModel):
    word: str
    length: int

parser = PydanticOutputParser(pydantic_object=LengthResponse)
#这里的输出格式是为了提供给llm一个提示，告诉llm输出的格式
print(parser.get_format_instructions())
prompt = PromptTemplate(
    template="回答用户问题：{query}\n{format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# 调用示例
llm_response = '{"word": "hello", "length": 5}'  # 假设LLM输出此JSON
response = parser.parse(llm_response)
print(response.word)  # hello
print(response.length)  # 5