friends = ['Max', 'Leo', 'Kate']
print(friends)
print(type(friends))
friend = friends[0]
print(friend)
print(type(friend))
# как добавить возраст другу

# Словарь dict - неупорядоченные коллекции произвольных объектов с доступом по ключю

friend = {                 # объявляется словарь в фигурных скобках, где указывается попарно ключь и значение
    'name': 'Max',
    'age': 23
}
print(friend) # вывод: {'name': 'Max', 'age': 23}
print(type(friend)) # вывод: <class 'dict'>