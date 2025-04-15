# lambda函数示例
# 基本语法
double = lambda x: x * 2
print("double(5):", double(5))  # 输出: 10

# 与常规函数比较
def double_func(x):
    return x * 2
print("double_func(5):", double_func(5))  # 输出: 10

# 实用场景1: 排序
students = [
    {'name': '张三', 'score': 90},
    {'name': '李四', 'score': 85},
    {'name': '王五', 'score': 95}
]
# 按分数排序
students_sorted = sorted(students, key=lambda x: x['score'], reverse=True)
print("按分数排序:", students_sorted)

# 实用场景2: 映射
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("平方后的列表:", squared)  # 输出: [1, 4, 9, 16, 25]

# 实用场景3: 过滤
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("偶数:", even_numbers)  # 输出: [2, 4]

# 高阶函数示例
def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(5, 3, lambda a, b: a * b)
print("5 * 3 =", result)  # 输出: 15