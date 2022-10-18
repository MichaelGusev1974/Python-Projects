# Основные функции Random в Python:
# randint - целое случайное число от А до В
# choice - случайный элемент последовательности
# shuffle - перемешивание последовательности
# random - случайное число щт 0 до 1
# sample - список длиной k из последовательности
# и др.
from random import randint, choice, sample, shuffle
# 1 выбрать случайное число от 0 до 100
print(randint(0, 100))

# 2 выбрать победителя лотереи из списка players
players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players))  #  ф-я choice позволяет выбрать значение из списка случайным образом

# 3 выбрать трех победителей лотереи из списка players
print(sample(players, 3)) #  ф-я sample позволяет выбрать несколько значений из списка случайным образом

# 4 перемешать карты в стопке (списке) cards
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(cards)
shuffle(cards) # перемешивает список случайным образом
print(cards)
