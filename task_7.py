from math import factorial

def fact(n):       # создаем генератор
    for el in range(n):
        yield el

n = int(input('факториалы до какого числа вы хотите получить? : '))

for i in fact(n): # перебираем с помощью генератора
    print(f'факториал числа {i+1} равен : {factorial(i+1)}')
