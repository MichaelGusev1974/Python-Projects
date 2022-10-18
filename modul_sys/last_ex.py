#  в папке с модулем создать 5 подпапок названия которых состоят из платформы на которой запущен интерпретатор и
#  порядкового номера начиная с 1:  win 32_1, win 32_2, ..... платформа м.б. другой

import sys, os
name = sys.platform
for i in range(1, 6):
    new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
    os.mkdir(new_path)