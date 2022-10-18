# sys.argv
# список аргументов командной строки при запуске скрипта Python
# sys.argv[0] -  путь до скрипта
# остальные параметры передаются при вызове скрипта через пробел
# Python my_script.py Par1 Par2 Par3
import sys

print(sys.argv[0])