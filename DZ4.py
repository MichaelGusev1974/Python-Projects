#Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
#1-й способ
#my_list_1 = [2, 5, 8, 8, 8, 2, 12, 12, 4]
#my_list_2 = [2, 7, 12, 3]
#print(type(my_list_1))
#print(my_list_1)
#print(my_list_2)
#result = set(my_list_1) - set(my_list_2) # приводим тип список к типу множество и делаем разность множеств
#print(list(result))                      #результат вывода приводим обратно к типу список
# если добавим в 1-й список несколько одинаковых элементов (например будет три 8) этот способ выведит только одну 8 и это не правильно!

# 2-й способ
my_list_1 = [2, 5, 8, 8, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for number in my_list_1:
    if number in my_list_2:
        my_list_1.remove(number)

#print(my_list_1)      # вывод: [5, 8, 8, 8, 12, 4] число 12 есть все равно! т.к. в первом списке числа 12 идут подряд.


# 3-й способ, правильный!!!
my_list_1 = [2, 5, 8, 8, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
for number in my_list_1[:]:             # делаем копию - срез списка [:] от начала и до конца, и теперь цикл for не
                                        # пропустит число, а выводится список. Срезы нужно делать не всегда,  только при удалении эл-ов.
    if number in my_list_2:
        my_list_1.remove(number)

print(my_list_1)