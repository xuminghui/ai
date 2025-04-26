class MyClass:
    def func1(self) -> str:
        print("这是一个实例方法")
        return "Hello, world!"
    def __init__(self) -> None:
        print("这是一个构造方法")
    def __call__(self) -> str:
        print("这是一个可调用对象")
        return "Hello, world!"
my_class=MyClass()
print(my_class.func1())
print(my_class()) #什么情况下，这个调用会成功？ 
print(callable(my_class)) # True


