""" Наследование - принцип ООП, предпологающий наследование кода от родительских классов дочерними классами """


# class Parent:
#     eyes = 2
#     hands = 2

#     def draw(self):
#         print('Хорошо рисует')


# class Child(Parent):
#     pass


# ch1 = Child()
# print(ch1.eyes)
# print(ch1.hands)
# ch1.draw()

"""
При наследовании все атрибуты и методы родительского класса перенимаются дочерним классом.

DRY - Don't Repeat Yourself
"""

# class Parent:
#     eyes = 2
#     hands = 2

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def drive(self):
#         print('Good driver')

#     def talent(self):
#         print('Хорошо поет')



# class Child(Parent):
#     def drive(self):
#         print('Bad driver')
#         # переопределение метода - полная смена поведения метода

#     def __init__(self, name, age, surname):
#         super().__init__(name, age)
#         # Parent.__init__(self, name, age)
#         self.surname = surname
#         # дополнение метода

#     def talent(self):
#         super().talent()
#         print('Хорошо рисует')


# par = Parent("Alina", 25)
# child = Child("Kanat", 15, "Artemov")
# par.talent()
# child.talent()
# par.drive()
# child.drive()


str
int
list
float
# function
dict
set
tuple
None
bool


class MyStr(str):
    def first_letter(self):
        return self[0]

    def find(self, value):
        result = super().find(value)
        # result = str.find(self, value)
        if result == -1:
            return 'Нет такой подстроки'
        return result
    



# string = MyStr("random string")
# print(string.upper())
# print(string.first_letter())
# # print(dir(string))
# print(string.find('e'))



class MyClass(object):
    a = 1
    b = 2
    c = 3

    def __str__(self):
        return "Мой объект"

obj = MyClass()
# print(dir(obj))
# print(obj)

# setattr()
# delattr()
# getattr()

setattr(obj, "d", 4)
# obj.d = 4
data = {'name': "Masha", "age": 20}
for k, v in data.items():
    setattr(obj, k, v)

# print(obj.name)
# print(getattr(obj, "name"))

# print(obj.weight) # AttributeError
# print(getattr(obj, "weight", "Нет такого атрибута")) # Нет такого атрибута

# del obj.name
# delattr(obj, "name")


# issubclass()
class Parent:
    ...

class Child(Parent):
    ...

print(issubclass(Child, Parent)) # True

ch2 = Child()
print(isinstance(ch2, Child)) # True
print(isinstance(ch2, str)) # False