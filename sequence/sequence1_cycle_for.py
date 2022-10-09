friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'quest', 'user')
if 'Max' in friends:
    print('У меня есть этот друг')
if 'M' in friend_name:
    print('В имени друга есть символ "М"')

# While
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1


# cycle for позволяет нам перебирать элементы последовательности по очереди без указания индекса
#Заканчивается после перебора всех элементов последовательности, позволяет совершать меньше ошибок при переборе эл-ов

for friend in friends:
    print(friend)

print('end')

for letter in friend_name:
    print(letter)

print('end')

for role in roles:
    print(role)

print('end')