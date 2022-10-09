cities = {'Las Vegas', 'Paris', 'Moscow'}
print(cities)
#добавление элемента
cities.add('Bruma')
print(cities)
# удаление элемента
cities.remove('Bruma')
print(cities)

# к множеству применимы методы последовательности: например взятие длины
print(len(cities))
# проверка на наличие элемента во множестве, выводит Yrue или False
print('Paris' in cities)
# перебор
for citi in cities:
    print(citi)