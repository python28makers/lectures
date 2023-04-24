""" Полиморфизм """

# Полиморфизм - принцип ООП, означающий использование одного и того же метода для разных классов/типов данных, но с различным результатом

# +
10 + 10 # 20 - сложение

'hello' + 'world' # 'helloworld' - конкатенация

(1, 2, 3) + (4, 5, 6) # (1, 2, 3, 4, 5, 6)


# print()

# len()


class Computer:
    def turn_on(self):
        print('Компьютер включился')


# class Phone:
#     def turn_on(self):
#         print('Телефон включился')


# class TV:
#     def turn_on(self):
#         print('Телевизор включился')


# class Remote:
#     def click(self, obj):
#         obj.turn_on()


# comp = Computer()
# phone = Phone()
# tv = TV()

# remote = Remote()
# for obj in (comp, phone, tv):
#     remote.click(obj)
# remote.click(comp)
# remote.click(phone)
# remote.click(tv)

# dict.pop()
# list.pop()


# class Human:
#     def __init__()


""" Абстракция """

# Абстракция - сущность без конкретной реализации
# Абстракция - не основной принцип ООП, означающий описание классов без реализации методов


class FakeAbstractCreature:
    def eat(self):
        pass

    def breath(self):
        pass

    def die(self):
        pass


class Human(FakeAbstractCreature):
    def eat(self):
        print('Ест ртом')
    
    def breath(self):
        print('Дышит носом')

    def die(self):
        print('Умирает от старости')


# human = Human()


from abc import ABC, abstractmethod, abstractproperty

class RealAbstractTechnique(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractproperty
    def display(self):
        pass

    @abstractmethod
    def sound(self):
        pass


class Laptop(RealAbstractTechnique):
    def turn_on(self):
        print('Включается ноутбук')
    
    @property
    def display(self):
        return 'Средний дисплей'

    def sound(self):
        print('бип боп бибоп') 

laptop = Laptop()