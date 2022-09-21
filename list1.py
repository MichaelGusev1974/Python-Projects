friends = ['Max', 'Leo', 'Kate']
print(friends)
# длина списка
print(len(friends)) # возвращает количетво элементов

# добавление элемента в список
friends.append('Ron') #добавили элемент списка 'Ron'
print(friends)
print(len(friends))

#удаление последнего элемента и его выода
print(friends.pop())# удалили последний элемент списка 'Ron' и вывели его в консоль
print(friends)

# очистить весь список
friends.clear() # очистили список
print(friends)

friends = ['Max', 'Leo', 'Kate']
# 1-й способ удаления элемента (объекта) из списка по значению
friends.remove('Kate')
print(friends)

# 1-й способ удаления элемента (объекта) из списка по значению
del friends[0]
print(friends)

