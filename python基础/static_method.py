from typing import Self


class PromptTemplate:
    template: str
    def __init__(self, template: str):
        self.template = template
    @staticmethod
    #下面这个函数定义的写法，Self还可以替换为PromptTemplate，但需要增加引号。
    #def from_template(template: str) -> "PromptTemplate":   
    # 使用引号可以确保类型提示正确，而不需要导入Self类型。但缺点是在类名改变时，需要修改所有的类型提示。
    # 推荐使用Self类型，因为它是类型提示的标准方式，并且可以在类名改变时自动更新类型提示。  
    def from_template(template: str) -> Self:
        return PromptTemplate(template)


if __name__ == "__main__":
    # 本地验证代码
    template = "Hello, {name}!"
    prompt = PromptTemplate.from_template(template)
    print(prompt.template)  # 输出: Hello, {name}!