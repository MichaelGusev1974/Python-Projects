#математические операции (расчеты нашей жизни)

#средняя продолжительность жизни в России(лет)
ale = 71
age = int(input('Сколько Вам лет: '))
# +
after20 = age + 20
print('Через 20 лет Вам будет: ', after20)
# -
alive = ale - age
print('По статистике Вам осталось жить', alive)
# *
count = 144000000
all_alive = count * ale
print('Среднее время жизни всех людей', all_alive)
# /
live_part = age / ale
print('Часть прожитой жизни', live_part)
print(type(live_part))

# // Целая часть от деления
live_part = age // ale
print('Часть прожитой жизни', live_part)

# % остаток от деления
print(3%2)
print(4%2)
print(5%3)


# ** Возведение в степень
print(2 ** 10)
print(2 ** 2)
