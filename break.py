# управляющая конструкция break позволяет выходить из цикла не важно выполнилось условие или нет
name = None
while True:                   #name != 'Гвидо':
    name = input('Кто создатель Python? ')
    if name == 'Гвидо':
        break
    print('НЕ верно')

print('Верно!')