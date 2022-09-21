numbers = range(10)
print(numbers)
print(type(numbers))# получим специальный тип - диапазон <class 'range'>

print(list(numbers))# приведение к типу list - список вывод:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] последняя цифра не входит в диапазон

numbers = range(66)
print(list(numbers))