#вывод чисел от 0 до 100
# While - Else - в блоке else (после while) мы выполняем действия после того, как вышли из цикла while,
# когда условие цикла стало (false)
number = 0
while number <= 100:
    print(number)
    #number = number +1
    number += 1
else:
    print('and')
# можно просто напечатать  print('and'), но фишка else в том, что только при условии того, что цикл отработал,
# условие number <= 100 стало false, только тогда сработает else и выведет and