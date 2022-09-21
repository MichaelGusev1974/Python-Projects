#форматирование
name = 'Leo'
age = '30'
# 1. Конкатенация
hello_str = 'Привет, '+ name + ' тебе '+ str(age) + ' лет '
print(hello_str)

# 2. %
hello_str = 'Привет %s тебе %s лет' % (name, age)
print(hello_str)

# 2. %
hello_str = 'Привет {} тебе {} лет'.format(name, age)
print(hello_str)