#вывод чисел от 0 до n, только не четные / четные
#управляющая конструкция continue позволяет переходить на следующую итерацию цикла (команды в цикле после continue не выполняются
number = 0
n = int(input('Введите число n: '))
while number <= n:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1