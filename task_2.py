class DivByZero(Exception):
    def __init__(self, text):
        self.text = text

def division(first, second):
    if second == 0:
        raise DivByZero('Деление на ноль является невозможным')
    else:
        return f'число {first} делим на {second} равно {round(first / second, 4)}'

first = int(input('введите число, которое будем делить : '))
second = int(input('введите число, на которое будем делить : '))

try:
    result = division(first, second)
except DivByZero as e:
    print(e.text)

