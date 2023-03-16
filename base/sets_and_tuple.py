""" кортежи - tuple """
# tuple() - неизменяемый, итерируемый, индексируемый, упорядоченный тип данных. 

# days = ['Пн', 'Вт', "Ср", "Чт", "Пт", "Сб", "Вс"]
# days[4] = 'Февраль'
# immutable_days = ('Пн', 'Вт', "Ср", "Чт", "Пт", "Сб", "Вс")
# immutable_days[3] = 'Март' # TypeError

# print(dir(immutable_days))

# list1 = [1, 2, 3]
# tuple1 = (1, 2, 3)

# print(list1.__sizeof__())
# print(tuple1.__sizeof__())

""" распаковка """
a, b = (1, 2)
c, d = [3, 4]

# fake_tuple = (20)
# print(type(fake_tuple))

# real_tuple = (10, )
# print(type(real_tuple))

# fake_int = 30, 
# print(type(fake_int))

# a = ()
# print(type(a))

n, m = (1, 2)
v, u = 1, 2

# tuple1 = (1, 2)
# n, m = tuple1
# print(n)
# print(m)

# a, b, *c = (1, 2, 3, 4, 5)
# print(a)
# print(b)
# print(c)

# dict1 = {'base': 10, 'exp': 5, 'mod': 3}
# print(pow(**dict1))
# print(pow(base=10, exp=5, mod=3))


""" set - множества """
# set() - коллекция уникальных, неизменяемых элементов. Может хранить в себе только неизменяемые типы данных. Убирает дубликаты элементов. Итерируемый, изменяемый, неиндексируемый, неупорядоченный.

# литералы - {}

# empty_set = set()
# print(type(empty_set))

# set_1 = {1, 2, 3}
# print(type(set_1))

# u_set = {True, 1, 'hello', 1, 2, (1, 2), 0, False, None}
# print(u_set)

# nums_set = {5, 6, 3, 2, 8, 10}
# print(nums_set)

# set_2 = {1, 2, [3, 4]} # TypeError

# list_1 = ['hello', 'hello', 1, 1, 1, 2, 2]
# a = set(list_1)
# b = list(a)
# print(b)

# a1 = {1, 2, 3, 4}
# b1 = {8, 7, 2, 4}
# print(a1.intersection(b1))

