# функция для фильтрации списка чисел
# def me_filter(numbers):
#     result = []
#     for number in numbers:
#         if number % 2 == 0:
#             result.append(number)
#     return result
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(me_filter(numbers))


def me_filter(numbers, function):    # передаём в функцию второй параметр function. Этф ф-я отвечает: записывать число в result или нет.
    result = []
    for number in numbers:           # меняем условие: если function(number) вернет True - мы будем записывать в result это число, если false - не записываем
        if function(number):
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Напишем ф-ю, которая будет определять четное число или нет.
def is_even(number):
    return number % 2 == 0
print(me_filter(numbers, is_even))   # передаем ф-ю is_even() в качестве второго параметра в ф-ю me_filter

# если нужны не четные числа:
def is_not_even(number):
    return number % 2 != 0
print(me_filter(numbers, is_not_even))

# если нужны числа, больше 4
def big_4(number):
    return number > 4
print(me_filter(numbers, big_4))