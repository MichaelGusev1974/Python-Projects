# Пользователь вводит три числа, найти максимальное из них, минимальное из них, их сумму и вывести результат на экран.
numbers = []
for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)

print(max(numbers))
print(min(numbers))
print(sum(numbers))