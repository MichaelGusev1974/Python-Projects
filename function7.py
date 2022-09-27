# Можно указать у параметра значение по умолчанию


def greeting(who, say='Hello'):
    print(say, who)

greeting('Leo', 'Hi')
greeting('Leo')
greeting('Leo', 'Hi')