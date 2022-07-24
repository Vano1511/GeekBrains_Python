class Data:

    def __init__(self, data):
        self.data = data

    def data_num(self):
        self.numbers = self.data.split('-')
        self.numlist = [int(el) for el in self.numbers]
        return self.numlist

    def valid_data(self, list):
        if list[0] in range(1, 32):
            if list[1] in range(1,13):
                if list[2] in range (0, 2022):
                    return 'дата введена корректно'
                else:
                    return 'введен некорректно год'
            else:
                return 'введен некорректно месяц'
        else:
            return 'число введено некорректно'

data = input('введите дату в формате дд-мм-гггг : ')

day = Data(data)

print(day.valid_data(day.data_num()))
print(day.data_num())