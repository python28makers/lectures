""" Множественное наследование """

class Mom(object):
    height = 170

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self):
        print('Хорошо поет')


class Dad(object):
    height = 180

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def drive(self):
        print('Хорошо водит')


class Child(Mom, Dad):
    pass


child = Child('Maksat', 15)
child.drive()
child.sing()
print(child.height) # 170 - Mom

# print(Child.mro())
# MRO - method resolution order - правило поиска методов и атрибутов
# По этому правилу поиск атрибутов идет слева направо

# Проблема ромба - решенная 

# class A1:
#     pass

# class B2(A1):
#     pass

# class C3(A1):
#     pass

# class D4(B2, C3):
#     pass

# d = D4()
# d.attr


# Перекрестное наследование - нерешенная проблема
# class A1:
#     pass

# class B2:
#     pass

# class C3(A1, B2):
#     pass

# class D4(B2, A1):
#     pass

# class E5(C3, D4):
#     pass


""" Миксины - классы-примеси """
# Миксины - несамостоятельные классы, от которых нельзя создавать объекты и служат для дополнения функционала других классов
# при наследовании миксины должны идти в первую очередь

class CranMixin:
    def move_heave_things(self):
        print('Поднимаю тяжелые вещи')


class NitroMixin:
    def add_speed(self, speed):
        self.speed += speed

class Car(CranMixin, NitroMixin):
    def __init__(self, color, brand, speed):
        self.color = color
        self.brand = brand
        self.speed = speed


# car = Car('Оранжевый', "КАМАЗ", 80)
# car.move_heave_things()
# car.add_speed(100)
# print(car.speed)

# nitro = NitroMixin()
# nitro.add_speed(100)

# Классы делят на 2 типа:
# 1. Функциональные - классы, выполняющие какие-то действия
# 2. Датаклассы - классы для хранения значений

# class RegisterUser:
#     def register(self):
#         ...
    
#     def login(self):
#         ...


# class User:
#     def __init__(self, name: str, password: str, email: str):
#         self.name = name
#         self.password = password
#         self.email = email

# from dataclasses import dataclass


# @dataclass
# class User:
#     name: str
#     password: str
#     email: str

# u1 = User('Hoolig@n', 'superpassword123', 'superboy@mail.ru')

