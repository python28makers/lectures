""" Декораторы """

# def func():
#     ...

# print(type(func))
# print(dir(func))
# print(func.__name__)


# Декораторы - функции высшего порядка, которые принимают другие функции, расширяют их функционал и на выходе возвращают измененную функцию. При этом тело принимаемой функции не затрагивается

# import time

# def func1():
#     start = time.time()
#     result = [i for i in range(1000)]
#     end = time.time()
#     print(end-start)
#     return result

# def func2():
#     start = time.time()
#     result = [i for i in range(1000)]
#     end = time.time()
#     print(end-start)
#     return result


# func1()
# func2()


import time

# def decorator(func):
#     def wrapper():
#         start = time.time()
#         res = func()
#         end = time.time()
#         print(end - start)
#         return res
#     return wrapper

# @decorator
# def func3():
#     return [i for i in range(10)]

# print(func3())

# @decorator
# def func4():
#     ...



# def timer(func):
#     def wrapper(*args, **kwargs):
#         import datetime
#         print(datetime.datetime.now())
#         res = func(*args, **kwargs)
#         return res
#     return wrapper

# @timer
# def add(x, y):
#     return x + y

# add = timer(add)
# print(add(1, 2))

# @timer
# def add_3_nums(a, b, c):
#     return a + b + c

# print(add_3_nums(10, 20, 30))
# print(add(10, 20))


# def func_name(func):
#     def wrapper(*args, **kwargs):
#         print(f"Вызвана  {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# def func_close(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print('Функция закончила свою работу')
#         return res
#     return wrapper

# def func_slow(func):
#     def wrapper(*args, **kwargs):
#         import time
#         time.sleep(4)
#         return func(*args, **kwargs)
#     return wrapper

# @func_close
# @func_slow
# @func_name
# def get_nums(nums):
#     return [i * 2 for i in nums]

# print(get_nums(range(1, 10)))


def call_func(times=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import time
            total_time = 0
            for _ in range(times):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                total_time += end - start
            avg_time = total_time / times
            print(f'Среднее время выполнения функции {func.__name__} - {avg_time}')
        return wrapper
    return decorator


# @call_func(times=10)
# def iterate_nums(nums):
#     return [i for i in nums]

# iterate_nums(range(100))

# @call_func(times=10)
# def open_site(url):
#     import urllib.request
#     urllib.request.urlopen(url)

# open_site('https://lovesimpsons.ru/')


def get_time():
    import datetime
    time_ = datetime.datetime.now()
    print(time_)

def func():
    get_time()
    ...

def func2():
    get_time()
    ...

