# Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать
# строку вида «Василий, 21 год(а), проживает в городе Москва»
def person_info(name, age, city):
    result = f'{name}, {age}, год(а), проживает в городе {city}'
    return result

print(person_info('Василий', 21, 'Москва'))
