# Lambda - функции:
# применяются для создания анонимных функций по месту их использования
# записывается Lambda - функция в одну строку: Lambda входные параметры: результат (после двоеточия)
def me_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def is_even(number):                 # теперь эту ф-ю можно удалить, т.к. ее функционал выполняет Lambda-функция
#     return number % 2 == 0
print(me_filter(numbers, lambda number: number % 2 == 0))  # Lambda входные параметры: результат (после двоеточия)
# если нужны не четные числа:

print(me_filter(numbers, lambda number: number % 2 != 0))

# если нужны числа, больше 4

print(me_filter(numbers,lambda number: number > 4))