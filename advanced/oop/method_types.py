""" Виды методов внутри классов """


# Метод - функция, которая находится внутри класса

"""
instance method - методы экземпляра - в обязятельном порядке принимают в себя self (ссылка на объект). 
Имеет доступ к объекту, к классу (ко всем методам и атрибутам класса)
"""
class InstanceMethod:
    cl_attr = 10

    def __init__(self):
        self.in_attr = 20

    def method1(self):
        print(self.cl_attr)
        print(self.in_attr)

    def method2(self):
        print(self.method1())


obj1 = InstanceMethod()
obj2 = InstanceMethod()

obj1.cl_attr # 10 
obj2.cl_attr # 10

# obj1.cl_attr = 50
# print(obj1.cl_attr) # 50
# print(obj2.cl_attr) # 10

obj1.__class__.cl_attr = 100
# # InstanceMethod.cl_attr = 100
# print(obj1.cl_attr) # 100
# print(obj2.cl_attr) # 100

"""  
class method - методы класса - методы для работы с классом, в обязательном порядке принимают в себя cls.
Имеют доступ к классу, к методам класса, но не имеют доступа к объектам.

создаются с помощью декоратора @classmethod
"""
# class ClassMethod:
#     cl_attr = 10

#     def __init__(self):
#         self.in_attr = 20

    # @classmethod
    # def method1(cls):
    #     print(cls.cl_attr)
        # print(cls.in_attr) # AttributeError

# obj1 = ClassMethod()
# obj1.method1()


# class User:
#     counter = 0

#     def __init__(self, name):
#         self.name = name
#         # User.counter += 1
#         self.add_user()

#     @classmethod
#     def add_user(cls):
#         cls.counter += 1
    

# a = User('Kanat')
# b = User('Mirgul')
# print(User.counter)



"""  
static method - статические методы - не принимают никаких обязательных аргументов. Не имеют доступа ни к чему внутри класса. 

Служат для написания логических функций, которые строят класс.

создаются с помощью декоратора @staticmethod
"""
class User:
    db = []

    def __init__(self, username, password, email):
        self.username = username
        self.password = self._hash_password(password)
        self.email = email
        self.add_user(self)
    
    @classmethod
    def add_user(cls, user):
        cls.db.append(user.__dict__)
        
    @staticmethod
    def _hash_password(raw_password):
        from hashlib import sha256
        hashed_password = sha256(raw_password.encode()).hexdigest()
        return hashed_password
    
    def login(self, username, password):
        for user in self.db:
            if user['username'] == username:
                if self._hash_password(password) == self.password:
                    return True
                raise ValueError('Неправильно введены данные')
        return False

user = User('Shabdan', 'superpassword123', 'shaba@mail.com')
# print(user.password)
print(user.login('Shabdan', 'superpassword123'))
# User('asdf', 'superpass123', 'asdf@mail.ru')
# superpass123 -> ed23fp4890j53kh6j4w-09ut8qyr76edftebgnhr
    