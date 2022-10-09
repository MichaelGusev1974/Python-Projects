# Параметры (аргументы) функции
# параметры ф-ции определяются в скобках после имени;
# def my_func(параметр1, параметр2,...), параметров м.б. много или не быть совсем

def hello_Max():
    print('Hello', 'Max')

hello_Max()

def hello(who):
    print('Hello', who)

hello('Leo')

def greeting(who, say):
    print(say, who)

greeting('Leo', 'Hi')
greeting('Max', 'Hiiiii!')