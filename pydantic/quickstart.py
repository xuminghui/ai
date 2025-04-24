from pydantic import BaseModel, ValidationError, Field

class User(BaseModel):
    id: int
    name: str = "匿名用户"
    age: int = Field(ge=0, description="年龄需非负")

# 正确输入：自动转换类型
user = User(id="123", age=25)  # id被转为int(123)
print(user.model_dump())  # {'id': 123, 'name': '匿名用户', 'age': 25}

# 错误输入：触发ValidationError
try:
    User(id="1", age=-1)
except ValidationError as e:
    print(e.errors())
    """
    try 成功执行之后，except 不会被执行，else 会被执行
    """
else:
    print("没有错误")
    # 输出：[{'type': 'int_parsing', 'loc': ('id',), ...}, ...]