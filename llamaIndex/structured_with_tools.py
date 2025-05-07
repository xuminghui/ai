from llama_index.llms.deepseek import DeepSeek
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from llama_index.core.program.function_program import get_function_tool

load_dotenv()

class Person(BaseModel):
  job: str = Field(..., description="职业")
  age: int = Field(..., description="年龄")
  married: bool = Field(..., description="是否结婚")
  #兴趣爱好
  hobby: str = Field(..., description="兴趣爱好")
class Persons(BaseModel):
    persons: list[Person] = Field(..., description="Multiple person")   
tool = get_function_tool(Persons)
   
#定义llm
llm = DeepSeek(model="deepseek-chat", api_key=os.getenv("DEEPSEEK_API_KEY"))
text="""
我是老徐，40了，已婚。我是码农。
"""
resp = llm.chat_with_tools(
    [tool],
    # chat_history=chat_history,  # can optionally pass in chat history instead of user_msg
    user_msg="从下面文本中抽取信息，如果相关信息不存在，就填写'无': " + text,
    # tool_choice="Invoice",  # can optionally force the tool call
)

tool_calls = llm.get_tool_calls_from_response(
    resp, error_on_no_tool_calls=False
)

outputs = []
for tool_call in tool_calls:
    if tool_call.tool_name == "Persons":
        outputs.append(Persons(**tool_call.tool_kwargs))

# use your outputs
print(outputs[0])
