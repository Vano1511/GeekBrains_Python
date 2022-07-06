from random import randrange
quantity = int(input('введите количесвто элементов в списке : '))
first_list = [randrange(10) for el in range(quantity)]
print(first_list)

finish_list = [el for el in first_list if first_list.count(el) == 1]
print(finish_list)