#Цикл while
# Задавать вопросы , пока пользователь не введет правильный ответ
# Без цикла
#name = input('Кто создатель Python? ')
#if name == 'Гвидо':
    #print('Правильно')
#else:
    #print('Неверно')
#Цикл while

name = input('Кто создатель Python? ')
while name != 'Гвидо':
    print('НЕ верно')
    name = input('Кто создатель Python? ')

print('Верно!')