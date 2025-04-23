from dataclasses import dataclass
# 传统写法（需要手动实现大量样板代码）
# 不可变对象
# 替代字典作为复合数据结构user = {"name": "Tom", "age": 25}


@dataclass(frozen=True)
class FrozenDog():
    name: str   # 自动生成__init__参数
    age: int  = 10     # 自动生成属性访问方法
    # 带默认值的参数必须放在最后

if __name__ == "__main__":
    dog = FrozenDog("Tom", 3)
    print(dog.age)  
    dog.age = 4  # 报错，因为实例是不可变的
