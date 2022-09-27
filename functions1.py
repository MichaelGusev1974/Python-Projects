# abs - модуль числа; min/max - мин. и макс. значение числа; round - округление числа; sum - сумма эл-ов последовательности;
# enumerate - нумерация последовательности.

# abs
print(abs(-7))

# min,max
numbers = [5, 15, 7, 1, -9, 0]
print(max(numbers))
print(min(numbers))

# round
print(round(10.9872, 2))

# sum
print(sum(numbers))

# enumerate
winners = ['Leo', 'Max', 'Kate']
for number, winner in enumerate(winners, 1 ):
    print(number, winner)