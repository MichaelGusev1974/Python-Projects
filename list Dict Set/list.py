# Можно объявить пустой список
empty_list = []

# Можно объявить список и сразу заполнить его элементами
friends = ['Max', 'Leo', 'Kate']

# тип списка - list (класс list)
print(type(friends))

# как и в строке для списка доступны индексы (начинаются с 0)
print('Второй друг', friends[1])
print('Первый друг с конца', friends[-1])

# так же можно применить срезы
print(friends[1:2])
print(friends[:2])
print(friends[1:])
