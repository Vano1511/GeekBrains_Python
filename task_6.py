from itertools import cycle,count

# for el in count(5): # скрипт итератора, генерирующего целые числа по порядку
#     if el > 20:
#         break
#     else:
#         print(el)

counter = 0 # итератор, который проходит по элементам множества по кругу
word = 'round'
for el in cycle(word):
    print(el)
    if counter > 8:
        break
    else:
        counter +=1


