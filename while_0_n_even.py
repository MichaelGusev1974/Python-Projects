#вывод чисел от 0 до n, только четные
number = 0
n = int(input('Введите число n: '))
while number <= n:
    if number % 2 == 0:
        print(number)
    #number = number +1
    number += 1