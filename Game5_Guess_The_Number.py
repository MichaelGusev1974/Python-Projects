# Добавляем к игре "угадай число"  возможность выбора кол-ва пользователей, ввода имен пользователей;
# Добавить систему поочередного хода, добавить объявление победителя
import random
number = random.randint(1, 100)
#print(number)
user_namber = None
count = 0
levels = {1: 10, 2: 8, 3: 6, 4: 4}
level = int(input('Выберите уровень сложности (из четырех возможных): '))
max_count = levels[level]
user_count = int(input('Выберите количество пользователей: '))  # переменная user_count для хранения количества пользователей
users = []
for i in range(user_count):                                     # цикл - перебор количества пользователей
    user_name = input(f'Введите имя пользователя {i}: ')        # ввод имени пользователя
    users.append(user_name)                                     # добавляем имена пользователей в пустой список users = []
print(users)
is_winner = False                                               # переменная, обозначающая то, что у нас есть победитель
winner_name = None                                              # имя победителя
while not is_winner:
    count += 1
    if count > max_count:
        print('Все пользователи проиграли!')
        break
    print(f'Попытка № {count}')
    for user in users:                                          # цикл перехода хода от одного пользователя к другому
        print(f'Ход пользователя: {user}')                      # указываем, кто делает ход
        user_namber = int(input('Введите число: '))
        if user_namber == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_namber:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
else:
    print(f'Победитель {winner_name}')