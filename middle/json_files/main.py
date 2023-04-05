""" JSON """

# JSON - JavaScript Object Notation - формат файлов для обмена данными между разными языками программирования

# True, False -> true, false
# None -> null

import json
human = {
    'name': 'Aibek',
    'age': 28,
    'is_married': False,
    'job': None,
    'friends': ['Dinara', 'Aidai']
}
json_human = json.dumps(human)
# print(json_human)
# print(type(json_human))

# Сериализация - процесс перевода из питон-объектов в JSON-объекты


with open('db.json', 'w') as db:
    laptop = {
        'brand': 'Acer',
        'price': 96000,
        'in_stock': True,
        'reviews': ['Классный ноут!', 'Не зависает!!'] 
    }
    json_laptop = json.dumps(laptop, indent=4, ensure_ascii=False)
    db.write(json_laptop)
    # json.dumps(obj) - принимает объект(словарь, список) и переводит в json, возвращает str


json_book = '{"title": "Времени нет", "author": "Алексей Б.", "year": 2005, "bestseller": true}'
python_book = json.loads(json_book)
# print(python_book)
# print(type(python_book))
python_book['author'] # Алексей Б. 
# Десериализация - процесс перевода из JSON-объектов в питон-объекты

# with open('db.json', 'r') as file:
#     json_obj = file.read()
#     python_obj = json.loads(json_obj)
#     print(python_obj)
#     print(python_obj['brand'])
    # json.loads(json-obj) - принимает json-строку, превращает в питон объект

# with open('books.json', 'w+') as file:
#     books = [
#         {
#             'title': 'Киберканикулы',
#             'author': 'Ольга Громыко'
#         },
#         {
#             'title': 'Новейший завет',
#             'author': 'Алексей Б.'
#         }
#     ]
#     json.dump(books, file, indent=4, ensure_ascii=False)
#     file.seek(0)
#     python_books = json.load(file)
#     print(python_books)


# Python          JSON
# dict            object
# list            array(массив)
# str             string
# int             number(int)
# float           number(real)
# True/False      true/false
# None            null

