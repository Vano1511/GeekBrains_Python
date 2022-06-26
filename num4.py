num = int(input('введите натуральное число: '))
max = 0

while num >0:
    a = num % 10
    if a > max:
        max = a
    num = num // 10

print('Самая большая цифра в вашем числе это ', max)