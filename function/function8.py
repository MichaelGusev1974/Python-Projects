# args - передача любого количества параметров
# kwargs - передача любого количества параметров параметров


def greeting(say, *args):  # поставили * значит можем после * добавлять сколько угодно параметров, передать в виде кортежа
    print(say, args)        # получаем кортеж из параметров на выводе
# параметр со звездочкой принято называть args, другой kwargs
greeting('hello', 'Leo')
greeting('hello', 'Leo', 'Max')
greeting('hello', 'Leo', 'Max', 'Kate')

def get_person(**kwargs):  # получаем словарь
    for k,v in kwargs.items():
        print(k, v)
get_person(name = 'Leo', age = 20, has_car = True)
