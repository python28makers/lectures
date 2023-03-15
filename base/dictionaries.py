# слово - word
""" dictionaries - словари """
# dict() - изменяемый, итерируемый, неиндексируемый(вместо индексов выступают ключи). Состоит из пар - ключ: значение

# ключи могут только неизменяемыми типами данных и должны быть уникальными

# значения могут быть любыми типами данных

# словари используются для описания объектов

# литералы - {}

# stol = {'nojki': 4, 'color': 'white', 'height': 80}
# print(stol['nojki'])
# # print(stol['weight']) # KeyError
# stol['color'] = 'red'
# print(stol)

# human = {
#     'name': 'Aliya', 
#     'age': 22,
#     'height': 163,
#     'name': 'Aigerim'
# }
# print(human)

# a = {[1, 2]: '996712342'} # TypeError

""" Создание словаря """

dict1 = {'key': 'value'}

dict2 = dict(key='value', key2='value2')

dict3 = dict.fromkeys(['a1', 'b1'], 'value12')
# print(dict1)
# print(dict2)
# print(dict3)


""" Получение данных из словарей """
phone = {
    'model': 'Samsung',
    'color': 'black', 
    'memory': 256,
}

phone['memory'] # 256
# phone['display'] # KeyError

# print(phone.get('color')) # 'black'
# print(phone.get('display')) # None
# print(phone.get('power', 'Нет такого ключа в словаре')) # 'Нет такого ключа в словаре'


# print(phone.setdefault('model')) # Samsung
# print(phone.setdefault('power', 100)) # создал новый ключ 'power' и присвоил значения None
# print(phone)

""" Добавление данных в словарь """
human = {
    'name': 'Bakyt',
    'age': 24,
}

human['surname'] = 'Azamatov'
# print(human)

human.setdefault('height', 180)
# print(human)

human.update({'weight': 80})
# print(human)
human.update([['is_married', False]])
# print(human)


""" Удаления данных из словаря """
movie = {
    'title': 'Вторая жизнь Уве',
    'duration': 160,
    'year': 2015,
    'genre': ['Drama', 'Comedy']
}

# deleted_key = movie.pop('year')
# print(movie)
# print(deleted_key)
# del_el = movie.pop('country') # KeyError
# default_el = movie.pop('country', 'Значение1')
# print(default_el)

# deleted_pair = movie.popitem()
# print(deleted_pair)
# print(movie)

# del movie['title']
# print(movie)

# movie.clear()
# print(movie)


""" Перебор словаря / работа с циклом """

product = {
    'title': 'Robot Vacuum',
    'description': 'Пылесос',
    'price': 25000,
    'in_stock': True
}

# for i in product:
#     print(i)

# for key in product:
#     print(product[key])

# print(product.keys()) # возвращает коллекцию из ключей словаря
# for key in product.keys():
#     print(key)

# print(product.values()) # возвращает коллекцию из значений словаря
# for value in product.values():
#     print(value)

# print(product.items()) # .items() - возвращает коллекцию из кортежей состоящих из 2 значений, где первое ключ, второе - значение
# for key, value in product.items():
#     print(f'Ключ {key}', f'Значение {value}')

a1, a2 = ('val1', 'val2') # распаковка 



# product2 = product.copy()
# print(product2)
# product3 = product
# print(id(product))
# print(id(product2))
# print(id(product3))

# product3.pop('price')
# print(product)
# print(product3)
# print(product is product3)


human = {
    'name': 'Misha',
    'friends': ['Masha', 'Karina']
}
human_2 = human.copy()
human_2['friends'].append('Sergey')
# print(human_2)
# print(human)
# print(human['friends'] is human_2['friends'])

from copy import deepcopy
human3 = deepcopy(human)
# print(human3['friends'] is human['friends'])


# person = {
#     'name': 'Meerim',
#     'age': 25,
#     'passport': {
#         'name': 'Meerim',
#         'birth_date': '1996.03.14',
#         'nationality': 'Kyrgyz'
#     }
# }
# print(person['passport']['birth_date'])


car = {'model': 'Toyota', 'color': 'white', 'engine': 3.5}
car1 = {}
for key, value in car.copy().items():
    car.pop(key)
    car1[key] = value

print(car1)
print(car)


# for val1, val2, val3 in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
#     print(val1, val2, val3)