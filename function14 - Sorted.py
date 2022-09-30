# Функция Sorted
# сортировка последовательности
# sorted(iterable,*, key = None, reverse = False
# аргументы: последовательность, ключ для сортировки, порядок
# набор чисел
numbers = [1, 5, 3, 5, 9, 7, 11]
# сортировка по возрастанию
print(sorted(numbers))
# сортировка по убыванию
print(sorted(numbers, reverse=True))

# набор срок
names = ['Max', 'Alex', 'Kate']
# сортировка по алфавиту
print(sorted(names))

# города и численность населения (цифры не настоящие)
citys = [('Москва', 1000), ('Лас-Вегас', 500), ('Антверпен', 2000)]
# такая сортировка сработает по алфавиту
print(sorted(citys))
# как отсортировать по численности населения?

def by_count(city):
    return city[1]      # функцией возвращаем второй элемент кортежа по индексу 1, по немк будет сортировать ф-я sorted

print(sorted(citys, key=by_count)) # во 2-й  параметр функции sorted передаем ф-ю by_count(без параметра)
print(sorted(citys, key=lambda city: city[1]))