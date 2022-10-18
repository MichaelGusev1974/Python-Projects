# В зависимости от параметра вызывать различные функции скрипта
# параметр ping функция выводит pong
# 2 параметра name имя -> функция выводит приветствие
#  параметр list показать содержимое текущей директории

import sys, os

def ping():
    print('pong')
ping()

def hello(name):
    print('Hello', name)
hello('Leo')

def get_info():
    print(os.listdir())
get_info()

command = sys.argv[1]
if command == 'ping':
    ping()
elif command == 'lisi':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name)