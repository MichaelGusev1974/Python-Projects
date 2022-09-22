# Добавляем к игре угадай число уровень сложности
import random
number = random.randint(1, 100)
#print(number)
user_namber = None
while  number != user_namber:
    user_namber = int(input('Введите число: '))
    if number < user_namber:
        print('Ваше число больше загаданного')
    elif number > user_namber:
     print('Ваше число меньше загаданного')

print('Победа')