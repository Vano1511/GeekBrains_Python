class Complex:

    def __init__(self, num):
        self.num = validate(num)

    def __add__(self, other):
        return self.num + other.num
    def __mul__(self, other):
        return self.num * other.num

def validate(num):   # проверка на комлексное число
    if 'j' not in num:
        print('введено не комплексное число')
        return None
    else:
        return complex(num)



comp1 = Complex(input('введите первое комплексное число с мнимой частью с символом j :'))
while comp1.num == None:                                                        # принимает только комплексные числа
    comp1 = Complex(input('введите повторно первое комплексное число :'))
comp2 = Complex(input('введите второе комплексное число с мнимой частью с символом j :'))
while comp2.num == None:                                                        # принимает только комплексные числа
    comp2 = Complex(input('введите повторно второе комплексное число :'))

print(f'сумма двух введенных комплесных чисел равна  {comp1 + comp2}')
print(f'произведение двух введенных комплесных чисел равно  {comp1 * comp2}')
