sales = int(input('Введите показатель выручки компании: '))
costs = int(input('Введите показатель издержек компании: '))
employees = int(input('ведите количество сотрудников в компании: '))

if sales > costs:
    print('за прошедший период прибыль компании равна: ', sales - costs)
    print('причем рентабельность фирмы составляет: ', round(100*(sales/costs -1),2),'%')
elif sales == costs:
    print('за прошедший период компания сработала в ноль')
else:
    print('за прошедший период убыток компании равен: ', costs - sales)
print('прибыль(убыток) на сотрудника компании составляет: ', round((sales-costs)/employees, 2))