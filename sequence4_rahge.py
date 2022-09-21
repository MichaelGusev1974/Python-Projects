#когда нам может помочь range
winners = ['Max', 'Leo', 'Kate']
#простой перебор

for winner in winners:
    print(winner)

# используем range
#for i in range(len(winners)):
    #print(i)
    #print(i, ')', winners[i])            # т.к. ввод по индексу, первый будет "0", можно сделать i + 1
   # print(i + 1, ')', winners[i])

for i in range(1, len(winners) + 1):      # старт с 1, к длине последовательности + 1

    print(i, ')', winners[i - 1])         # вывод 1 ) Max
                                                # 2 ) Leo
                                                # 3 ) Kate