class MyClass:
    static_var = 0
    
    def __init__(self, value):
        self.value = value

print(MyClass.static_var)

obj1 = MyClass(10)
obj2 = MyClass(20)
print(obj1.static_var)
print(obj2.static_var)

MyClass.static_var = 100
print(obj1.static_var)
print(obj2.static_var)

class MathUtils:
    
    @staticmethod
    def add(x, y):
        return x + y

result = MathUtils.add(5, 7)
print(result)

math_instance = MathUtils()
result = math_instance.add(3, 4)
print(result)
