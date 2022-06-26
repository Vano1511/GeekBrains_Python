sales = int(input('Введите показатель выручки: '))
costs = int(input('Введите показатель издержек: '))

if sales > costs:
    print('за прошедший период прибыль компании равна: ', sales - costs)
elif sales == costs:
    print('за прошедший период компания сработала в ноль')
else:
    print('за прошедший период убыток компании равен: ', costs - sales)
