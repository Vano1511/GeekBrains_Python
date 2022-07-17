from functools import reduce
def sum(first,second):
    return first + second

my_list = [el for el in range(100,1001) if el % 2 == 0] # создаем список четных чисел
print(f' сумма всех четных чисел от 100 до 1000 равна : {reduce(sum,my_list)}')