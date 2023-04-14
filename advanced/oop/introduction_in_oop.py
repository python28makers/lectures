""" ООП - Объектно Ориентированное Программирование """

# int
# list 
# dict 
# str
# ООП - способ написания кода (парадигма - видение решения проблемы), основанный на классах и его объектах

class MyClass:
    ...

# Класс - описание объектов, чертеж для объектов - в нем описывается поведение объекта.
# Класс состоит из атрибутов и методов

# class Human:
#     hands = 2
#     legs = 2
#     head = 1
    # переменные класса/атрибуты класса

    # def eat(self): # метод - функция внутри класса
    #     print('человек кушает')

# print(Human.hands)
# a = 10
# a = int(10)
# h1 = Human()
# print(h1.legs)
# h1.eat()
# Human.eat(h1)
# h2 = Human()
# h3 = Human()
# h2.fingers = 20 # добавление атрибута объекту
# h2.legs = 3 # изменение атрибута объекта
# print(h2.fingers)
# print(h2.legs)

# print(h3.fingers) # AttributeError
# Human.eyes = 2
# print(h3.eyes)
# print(h2.eyes)


# class Person:
#     human_counter = 0
#     heart = True
#     brain = True
#     tongue = "Есть"
#     # переменные класса/атрибуты класса

#     def __init__(self, name, age, height, weight) -> None:
#         # переменные/атрибуты экземпляра/объекта класса
#         # self - ссылка на объект
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#         Person.human_counter += 1
#         print('__init__ сработал под капотом')

#     def get_info(self):
#         return f'Имя: {self.name}, возраст: {self.age}'
    
#     def birthday(self):
#         self.age += 1
#         return f'с днем рождения, {self.name}. Теперь Вам {self.age} лет'

# p1 = Person('Valeriy', 25, 178, 87) # объект класса Person
# p2 = Person('Aidai', 29, 170, 80)
# # p2.name # Aidai
# print(p1.get_info())
# print(p2.get_info())
# print(p2.birthday())
# print(p1.human_counter)


# class Wallet:
    # def __init__(self, money: int):
    #     if money < 0:
    #         raise ValueError('Неправильное значение')
    #     self.money = money

#     def __init__(self, money: int):
#         self.money = self.check_money(money)

#     def check_money(self, value: int):
#         if value < 0:
#             raise ValueError('Неверное значение')
#         return value
    

# w1 = Wallet(200)


class Animal:
    def __init__(self, legs, voice, skin):
        self.legs = legs
        self.voice = voice
        self.skin = skin

horse = Animal(4, 'игого', 'гладкая')
print(horse.__dict__)
# horse.a = 10
# horse.__dict__.update({'a': 10})


"""  
Принципы ООП

Наследование
Инкапсуляция
Полиморфизм

Абстракция
                -  Агрегация
Ассоциация -<
               - Композиция
"""