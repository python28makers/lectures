""" Инкапсуляция """

# Инкапсуляция - имеет 2 определения:
#     1. Сбор связанных между собой методов и атрибутов в один класс.
#     2. Защита данных внутри класса - ограничение доступа к определенным данным

# class Computer:
#     def __init__(self, monitor, ram, color):
#         self.monitor = monitor
#         self.ram = ram
#         self.color = color
    
#     def cook(self):
#         print('Готовит еду')
    # нарушен принцип инкапсуляции


# class Phone:
#     def __init__(self, ram, color, battery):
#         self.ram = ram
#         self.color = color
#         self.battery = battery


# phone = Phone(216, 'black', 5000)
# phone.battery # 5000
# phone.battery = -700

""" 
Защита данных в питоне работает на уровне соглашения

Модификаторы/уровни доступа/защищенности:

1. public - публичный
Публичные атрибуты и методы доступны везде: внутри класса, внутри дочерних классов, вне класса

2. protected
Защищенные атрибуты и методы доступны только внутри класса и в дочерних классах

3. private
Приватные методы и атрибуты доступны только внутри того класса, где они определены
"""

class EncapsulatedClass:
    public = 'public'
    _protected = 'protected'
    __private = 'private'

    def __init__(self, pub, prot, priv):
        self.pub = pub
        self._prot = prot
        self.__priv = priv
    
    def pub_method(self):
        ...

    def _prot_method(self):
        ...

    def __priv_method(self):
        ...
    

# obj = EncapsulatedClass('pub', 'prot', 'priv')
# print(obj.public)
# print(obj._protected)
# print(obj._EncapsulatedClass__private)
# obj._EncapsulatedClass__private = 292
# print(dir(obj))
# print(obj.__private)


class Phone:
    __MIN_RAM = 0
    __MAX_RAM = 1024

    def __init__(self, ram, battery, brand, color):
        if ram < self.__MIN_RAM and ram > self.__MAX_RAM:
            raise ValueError('Недопустимая память')
        self._ram = ram
        self._battery = battery
        self._brand = brand
        self._color = color


""" getter и setter (deleter) - интерфейсные методы """

class Light:
    __is_on = False
    __MAX_BRIGHTNESS = 100
    __MIN_BRIGHTNESS = 0

    def __init__(self, brightness: int, model):
        self.model = model
        if brightness < self.__MIN_BRIGHTNESS or brightness > self.__MAX_BRIGHTNESS:
            raise ValueError('Недопустимая яркость')
        self.__brightness = brightness

    def switch_light(self):
        # setter - устанавливает значение
        self.__is_on = not self.__is_on
    
    def is_on(self):
        # getter - показывает значение
        if self.__is_on:
            return 'Включен'
        return 'Выключен'
    
    @property # превращает метод в свойство - создает getter
    def brightness(self):
        return self.__brightness
    
    @brightness.setter
    def brightness(self, value):
        if value < self.__MIN_BRIGHTNESS or value > self.__MAX_BRIGHTNESS:
            raise ValueError
        self.__brightness = value
    
    @brightness.deleter
    def brightness(self):
        if self.__is_on:
            raise Exception('Сначала выключи свет')
        del self.__brightness


# light = Light(80, 'Apple')
# print(light.brightness)
# light.switch_light()
# light.brightness = 98
# print(light.brightness)
# del light.brightness
# light.model
# light.model = 'Samsung'
# del light.model
# light._Light__is_on = True
# print(light.is_on())
# light.switch_light()
# print(light.is_on())



