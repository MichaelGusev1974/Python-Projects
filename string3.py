friends = 'Максим Леонид'
print(friends)
print(len(friends))# длина строки, сколько символов, включая пробел

print(friends.find('Лео'))# методы, в отличие от функций, мы вызываем через точку
# возвращает индекс "7" с этого индеса начинается подстрока "Лео"

print(friends.find('123'))# возвращает -1 - это значит, что такой строки нет

print(friends.split())# метод,разбивающий строки через пробел (возвращает ['Максим', 'Леонид'] две строки)
friends = 'Максим ; Леонид'
print(friends.split(';'))#разделителем будет ";"

print(friends.isdigit())# метод, проверяющий состоит ли строка из чисел или нет, возвращает True или False
number = '123'
print(number.isdigit())# возвращает True

print(friends.upper())#метод приведения строки к верхнему регистру

print(friends.lower())#метод приведения строки к нижнему регистру





