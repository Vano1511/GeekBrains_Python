from random import randrange

count = int(input('введите количество элементов в списке : '))
first_list = [randrange(500) for el in  range(count)]
print(first_list)

finish_list = [first_list[i] for i in range(count) if first_list[i] > first_list[i-1]]
print(finish_list)