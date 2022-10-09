# Функция filtr
# фильтрация последовательности
# filtr(function, iterable)
# аргументы: функция фильтрации, последовательность.
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
# получить только четные числа:
def is_even(number):
    return number % 2 == 0
result = filter(is_even, numbers)
print(result)                      # вывод: <filter object at 0x0000023DC61B7D60>
result = list(result)              # чтобы сделать красывый вывод - записываем результат в список
print(result)

# набор срок
names = ['Max', 'Leo', 'Kate']
# получить строки больше трех сивловов
print(list(filter(lambda names: len(names) > 3, names)))
