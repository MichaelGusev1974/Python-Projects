#Дан список заполненный произвольными целыми числами.
#Получите новый список, элементами которого будут только уникальные элементы исходного.

numbers = [2, 2, 5, 12, 8, 2, 12, 30, 6, 6, 6.9, 13, 28.5, 7, 7, 11, 5, 5.5]
result = [] #создаем пустой список
for number in numbers:
    if numbers.count(number) == 1:        # count()метод, который проверяет, сколько раз число входит в список.
        result.append(number)             # добавляем при помощи метода append() уникальное число в пустой список result = []

print(result)                             # выводим result

