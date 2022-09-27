# передача параметров в функцию: по порядку; по имени;

#def greeting(who, say):
    #print(say, who)
# по порядку
#greeting('Leo', 'Hello') # в том порятке, в котором у нас объявлены параметры, мы передаем значения.

# по имени
#greeting(say='Hello', who='Leo') # не важен порядок, но чтобы присвоить значение ьы явно указываем имя значения

def greeting(who, say):
    print(say, who)

greeting('Leo', 'Hi')
greeting('Hi', 'Leo')
greeting(say='Hi', who='Leo')