#вывести нечетные цифры от 1 до 5

numbers = [1, 3, 5]
for number in numbers:
    print(number)

#функция range имеет три параметра: start_or_stop - начало или конец последовательности
                                   # stop - конец
                                   # step - шаг

print(list(range(1, 30, 2)))#range(start_or_stop, stop[, step] вывод: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

for number in range(1, 30, 2):
    print(number) # вывод в столбик, от 1-го до 30 с шагом 2 , последнее число 29