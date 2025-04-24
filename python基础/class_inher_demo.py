#父类必须在子类之前定义，否则会报错
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} is barking!")
class ElectricDog(Dog): # 继承Dog类
    def __init__(self, name, age, battery_life=70):
        super().__init__(name, age)
        self.battery_life = battery_life

    def charge(self):
        print(f"{self.name} is charging!")

if __name__ == "__main__":
    # 创建Dog和ElectricDog实例
    dog = Dog("Tom", 3)
    electric_dog = ElectricDog("Spark", 5)
    dog.bark()  # 输出: Tom is barking!
    electric_dog.bark()  # 输出: Spark is barking!
    electric_dog.charge()  # 输出: Spark is charging!
    





