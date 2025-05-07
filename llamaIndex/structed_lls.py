from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.llms import structured_llm
from llama_index.llms.deepseek import DeepSeek
from llama_index.embeddings.zhipuai import ZhipuAIEmbedding
from llama_index.core import Document
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

load_dotenv()


"""
  讲解扩展点
  age2: str = Field(..., description="10年后的年龄")
  age3: str = Field(..., description="20年后的年龄")  大模型语义的强大之处。
  age4: str = Field(..., description="Person's hobbie")
  基于description，大模型感知此提示词
  变量定义的语义，大模型也会感知此语义
  TODO：如何能找到此示例的提示语，让我们对提示词有一个直观的印象
"""
#定义一个实体
class Person(BaseModel):
  age: str = Field(..., description="Person's job")
  age1: int = Field(..., description="Person's age")
  age_after_30_years: str = Field(...)
  age3: str = Field(..., description="20年后的年龄")
  age4: str = Field(..., description="Person's hobbie")

class Persons(BaseModel):
    persons: list[Person] = Field(..., description="Multiple person")     

    
#定义llm
llm = DeepSeek(model="deepseek-chat", api_key=os.getenv("DEEPSEEK_API_KEY"))
structured_llm=llm.as_structured_llm(Persons)
from llama_index.core.prompts.prompts import SchemaExtractPrompt,PromptTemplate

text="""
我是abc，20了，未婚。我是一个程序员，我喜欢编程。
"""

print(Person.model_json_schema())
response=structured_llm.complete(text)
print(response.text)
print(response.raw)