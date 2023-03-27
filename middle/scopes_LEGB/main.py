""" Области видимости и пространства имен """

# x = 10
# print(x)

# y = 20
# def func1():
#     print(y)

# func1()

# def func2():
#     x = 20

# print(x)

# LEGB - Local Enclosed Global Built-in
# Local - локальное пространство имен(ПИ)
# Enclosed - замкнутное ПИ
# Global - глобальное ПИ
# Built-in - встроенное ПИ


# global_ = 'Глобальная переменная'

# def func2():
#     local_ = 'локальная переменная'
#     # замнкутое
#     def inner_func():
#        print(local_)
#        local_too = 'тоже локальная переменная' 
#        def func3():
#            a = 10


# Из локальных пространств доступно ВСЁ, что на глобальном и замнкнутом пространстве
# из глобального доступно только глобальные и встроенные имена

# name = 'Masha'
# def change_name():
#     name = 'Aliya'

# change_name()
# print(name)


# name = 'Kanat'
# def change_name_for_real():
#     global name, a, b
#     name = 'Misha'
#     a = 10
#     b = 20

# change_name_for_real()
# print(name)
# print(a)
# print(b)


# gl = 5
# def func1():
#     loc = 10
#     a = 10
#     def func2():
#         nonlocal loc, a
#         loc = 20
#         def func3():
#             nonlocal loc, a
#             loc = 30
#             a = 20
#         func3()
#     func2()
#     print(loc, a)

# func1()


# плохой код - функция зависит от внешней переменной
# nums = range(1, 10)
# def iter_and_mul():
#     for num in nums:
#         print(num * 2)
# iter_and_mul()

# хороший код - функция не зависит от внешних данных
# def iter_and_mul(nums):
#     for i in nums:
#         print(i * 2)

# iter_and_mul(range(1, 10))


""" globals(), locals() """
# globals() - возвращает словарь из глобальных имен
# locals() - возвращает словарь из локальных имен

var = 'jqiwgefhjrwektfiqwhebfrnmqeqwefihe'
def func1():
    pass

# print(globals())
# import math
# globals()

# print(locals())
# def func() -> dict[str, Any]:
#     a = 10
#     b = 20
#     print(locals())
#     return locals()

# # func()
# a = func()['a']
# print(a)

# from test1 import func, ab

# func()
# print(ab)

# from package1.funcs1 import calculate_nums, a
# from package2.funcs2 import greet_user

# print(calculate_nums(10, 20))
# print(greet_user('Женя'))

# a = 20
# print(a)

# def func():
#     print('Hello world')
#     print(__name__)


# if __name__ == '__main__': # точка входа в программу
#     print(10)
#     func()