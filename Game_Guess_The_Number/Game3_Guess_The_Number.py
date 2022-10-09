# Добавляем к игре угадай число уровень сложности: добавим количество попыток.
import random
number = random.randint(1, 100)
#print(number)
user_namber = None
count = 0                                              # ввели переменную count, счетчик попыток
max_count = 6
while number != user_namber:
    count += 1
    if count > max_count:
        print('Вы проиграли!')
        break
    print(f'Попытка № {count}')
    user_namber = int(input('Введите число: '))
    if number < user_namber:
        print('Ваше число больше загаданного')
    elif number > user_namber:
     print('Ваше число меньше загаданного')
    else:
        print('Победа')