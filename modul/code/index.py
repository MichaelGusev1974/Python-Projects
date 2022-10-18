import moda
from folderb.modb import foo, bar
# import modc
from modc import foo   # кажется, что при импорте конкретной переменной (foo) код скрипта не будет выполнятся. Будет!!!
                       # при любом варианте импорта (весь модуль или конкр. перем.) будет выполнятся скрипт или код этого модуля
print(moda.foo)        # здесь указываем модуль т.к. import moda
moda.bar()

print(foo)             #  здесь без указания модуля т.к. from folderb.modb import foo, bar
bar()

#  можем импортировать модуль целиком (import moda), либо конкретные объекты (from folderb.modb import foo, bar), либо
#  все объекты (import moda*) - не рекомендуется