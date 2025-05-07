from llama_index.core.llms import structured_llm
from llama_index.llms.deepseek import DeepSeek
from llama_index.core.prompts.prompts import PromptTemplate
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
load_dotenv()



#定义一个实体
class Person(BaseModel):
  job: str = Field(..., description="职业")
  age: int = Field(..., description="年龄")
  married: bool = Field(..., description="是否结婚")
  #兴趣爱好
  hobby: str = Field(..., description="兴趣爱好")
class Persons(BaseModel):
    persons: list[Person] = Field(..., description="Multiple person")     

    
#定义llm
llm = DeepSeek(model="deepseek-chat", api_key=os.getenv("DEEPSEEK_API_KEY"))
prompt=PromptTemplate(
 "从下面的文本提取person信息，如果找不到对应的信息，就用'无'代替。文本是：{text}"
)
text="""
我是老徐，40了，已婚。我是码农。
"""
response=llm.structured_predict(Persons,prompt=prompt,text=text)
print(response.model_dump_json(indent=2))