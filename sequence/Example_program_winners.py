#Пользователь вводит количество участников соревнований по Python
#Пользователь вводит  участников и их места в зависимости от количества
# 1. Вывод имен участников по алфавиту
# 2. Получить трех победителей и поздравить их
# 3.Победители: .... поздравляем!
print('СОРЕВНОВАНИЯ ПО PYTHON')
count = int(input('Введите количество участников: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место'.format(i))
    members.append(name)
    i -=1

# кто учавствовал в соревновании (по алфавиту)
print('В соревновании учавствовали:', sorted(members))

# мы записали людей с конца?
members.reverse()

# нам нужно взять первые три места
result = members[:3]
result = 'Победители {} поздравляем'.format(result)
print(result)