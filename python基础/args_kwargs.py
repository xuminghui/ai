###元组和字典。入参 *args, **kwargs的区别
#kw是keyword的缩写，表示“关键字”。在**kwargs中，kwargs即“关键字参数”（keyword arguments）。
#*args是一个元组（tuple），用于接收任意数量的位置参数。在函数定义中，*args可以用来接收任意数量的位置参数，并将它们作为一个元组传递给函数。
#**kwargs是一个字典（dictionary），用于接收任意数量的关键字参数。在函数定义中，**kwargs可以用来接收任意数量的关键字参数，并将它们作为一个字典传递给函数。   
#元组和字典都是Python中的数据结构，它们的主要区别在于：
#存储方式：元组是有序的不可变序列，而字典是无序的可变映射。
#访问方式：元组可以通过索引访问元素，而字典可以通过键（key）访问值。
#用途：元组通常用于存储一组相关的值，而字典通常用于存储一组键值对。
#示例：
#元组：
my_tuple = (1, 2, 3)
print(my_tuple[0])  # 输出：1
#字典：
my_dict = {"name": "Tom", "age": 25}
print(my_dict["name"])  # 输出：Tom


#PromptTemplate.from_template()这个类似java的静态方法，不需要实例化，直接调用。 
#这个在python中是怎么实现的？



