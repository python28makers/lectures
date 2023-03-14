""" list - списки """

# list() - коллекция. Изменяемый, упорядоченный, индексируемый, итерируемый. Служит для хранения набора элементов

# Элементами списка могут быть любые типы данных

list1 = [10, 'str', [1, 2, 3], (2, 3), {'key': 'value'}, True, None, set()]

# list2 = [1, 2, 3]
# print(list2[1])
# list2[1] = 5
# print(list2[1])
# print(list2)

""" Методы списков """
# print(dir(list))

# 1. Добавление элементов в список
# my_list = [1, 2, 3]
# print('До', my_list)
# my_list.append(4)
# print('После', my_list)
# list.append(obj) - добавляет obj в конец списка


# my_list2 = [1, 3, 4]
# my_list2.insert(1, '2')
# print(my_list2)
# # list.insert(index, obj) - вставляет obj на место index
# my_list2.insert(2, 'element')
# my_list2.insert(len(my_list2), '10')
# print(my_list2)


# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# list_1.extend(list_2)
# print(list_1)
# print(list_2)
# list.extend(iterable) - добавляет элементы iterable в конец list


# 2. Удаление элементов из списка
# nums = [1, 2, 3]
# deleted_el = nums.pop()
# first_elem = nums.pop(0)
# print(deleted_el)
# print(nums)
# list.pop([index]) - удаляет и возвращает элемент по index, по умолчанию последний

# nums = [4, 5, 6, 7, 5, 5]
# nums.remove(5)
# print(nums)
# list.remove(value) - удаляет первый встретившийся value из списка

# nums.clear()
# print(nums)
# list.clear() - полностью очищает список

# nums = [1, 2, 3]
# del nums[1]
# print(nums)


nums = [5, 3, 6, 2, 1]
# nums.sort() # по возрастанию
print(nums)
nums.sort(reverse=True) # по убыванию
print(nums)

names = ['Aliyaaasdfasdf', 'Sergeasdfy', 'Kanaasdft', 'Mariya']
# names.sort()
# print(names)
# names.sort(key=len, reverse=True)
# print(names)
# list.sort([key], [reverse]) - сортирует список по возрастанию, если reverse = True - по убыванию. Если в key передать имя функции, применит key к каждому элементу списка

# names.reverse()
# print(names)
# list.reverse() - переворачивает список
# print(names[::-1])


# nums = [1, 1, 1, 2, 3, 4]
# print(nums.count(1))
# list.count(value) - считает количество value  в списке

# print(nums.index(3))

