""" CSV """
# Comma Separated Values - Данные Разделенные Запятой. Формат данных табличного вида

import csv

# with open('phones.csv', 'w') as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(['title', 'price', 'color'])
#     csv_writer.writerow(['Samsung', 67000, 'black'])


phones = [
    {
        'title': 'Samsung',
        'price': 300,
        'in_stock': True
    },
    {
        'title': 'IPhone',
        'price': 400,
        'in_stock': False
    },
    {
        'title': 'Nokia',
        'price': 300000,
        'in_stock': True
    },
    {
        'title': 'Motorola',
        'price': 500,
        'in_stock': False
    }
]
with open('store.csv', 'w') as file:
    fieldnames1 = ['title', 'price', 'in_stock']
    writer = csv.DictWriter(file, fieldnames=fieldnames1)
    writer.writeheader()
    for phone in phones:
        writer.writerow(phone)