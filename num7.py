start = int(input('введите начальный показатель спортсмена: '))
finish = int(input('Введите его цель: '))
i = 1

while start < finish:
    start *= 1.1
    i += 1

print('спортсмен достигнет цели на ', i,'-й день')