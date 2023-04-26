""" Магические методы """

"""  
Магические методы (dunder methods) - методы имеющие в названии по два нижних подчеркивания с двух сторон.

1. Они вызываются сами по себе в определенные моменты
2. Они встроенные
"""

class MagicMethods:
    def __new__(cls, *args, **kwargs): 
        return super().__new__(cls)
        # pass

    def __init__(self):
        print('__init__ works')
        self.attr = 'magic'
    # __new__ & __init__ - методы-конструкторы - отвечают за создание объектов

    def __del__(self): # деструктор - удаляет объект 
        print('__del__ works')
        del self
    
    def __str__(self) -> str: 
        # человеко-читабельное отображение объекта
        return self.attr
    
    def __repr__(self) -> str:
        # Отображение объекта для компьютера
        return self.attr
    


# obj = MagicMethods()
# obj2 = MagicMethods()
# print(obj)
# magic_list = [obj, obj2]
# print(magic_list)


# Singleton - паттерн, в котором от класса может быть создан всего 1 объект

# class Singleton:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             return cls._instance
#         else:
#             return cls._instance
        
        
    

# obj = Singleton()
# obj2 = Singleton()
# print(obj is obj2) # True

# b = None
# c = None
# print(b is c)
# n = 'sartdyufyguhijkl;'
# m = 'sartdyufyguhijkl;'
# cd = True
# dc = True
# print(cd is dc)


class MyInt:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value
    
    """  
    __add__ - '+'
    __sub__ - '-'
    __mul__ - '*'
    __pow__ - '**'
    __truediv__ - '/'
    __floordiv__ - '//'
    __mod__ - '%'
    """
    # def __eq__(self, other):
    #     return self.value == other.value
    
    """  
    __eq__ - '=='
    __lt__ - '<'
    __gt__ - '>'
    __ne__ - '!='
    __ge__ - '>='
    __le__ - '<='
    """
    # def __eq__(self, __value: object) -> bool:
    #     print(__value)
    #     return self.value == __value

    
    
int1 = MyInt(1888)
int2 = MyInt(1888)
# print(int1 + int2) # 
# print(int2 - int1)
# print(int2 == int1)



# for num in nums:
#     print(num)
# nums = nums.__iter__()
# print(nums.__next__())
# print(nums.__next__())
# print(nums.__next__())
# print(nums.__next__())
# print(nums.__next__())
# while True:
# nums = [1, 2, 3, 4, 5]
# nums = nums.__iter__()
# while True:
#     try:
#         print(nums.__next__())
#     except StopIteration:
#         break


# class MyList:
#     def __init__(self, list_):
#         self.list_ = list_
    
#     def __iter__(self):
#         return MyIterator(self.list_)

# class MyIterator:
#     def __init__(self, list_):
#         self.index = 0
#         self.list_ = list_
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index >= len(self.list_):
#             raise StopIteration
#         res = self.list_[self.index]
#         self.index += 1
#         return res
    
# for num in MyList([1, 2, 3, 4, 5]):
#     print(num)

# nums = MyList([1, 2, 3, 4, 5])
# iterable = nums.__iter__()
# iterable.__next__() # 1


# class CallableClass:
#     def __call__(self, a, b):
#         return a + b

# obj = CallableClass()
# print(obj(10, 20))


# with open() as f:
#     ...

# with sum([1, 2, 3]) as f:
#     ...

# __enter__
# __exit__
class DBConnection:
    def __init__(self):
        self.connection = 'opened'

    def __enter__(self):
        return self
    
    def close_connection(self):
        self.connection = 'closed'

    def __exit__(self, *args, **kwargs):
        self.close_connection()


with DBConnection() as connection:
    print(connection.connection)

print(connection.connection)

