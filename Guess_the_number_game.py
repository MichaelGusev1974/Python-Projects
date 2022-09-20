number = 43
value = int(input('Введите число от 1-го до 100: '))
if value == number:
    print('Вы угадали!')
else:
    if value < number:
        print('Нужно больше ')
    else:
        print('Нужно меньше ')