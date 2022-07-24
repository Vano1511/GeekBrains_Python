class NoNum(Exception):  # создаем ошибку
    def __init__(self, text):
        self.text = text

def validate(new, cls): # метод проверки на ошибку
    try:
        if type(new) != int:
            raise NoNum(f'введите количество {type(cls).__name__} цифрой')

    except NoNum as e:
        print(e)
        return 1


class Warehouse:
    warehouse_dict = {} # создаем данные по складу

    def to_warehouse(self, equipment): # метод приема оргтехники на склад
        if equipment != []:
            self.quantity = equipment.pop(1)
            self.key = tuple(equipment)
            new_dict = {self.key : self.quantity}
            self.warehouse_dict.update(new_dict)


    def from_warehouse(self, quantity): # метод вывоза оргтехники со склада
        if self.name != []:
            if self.warehouse_dict.get(self.key) >= quantity:
                self.warehouse_dict[self.key] = self.warehouse_dict.get(self.key) - quantity
            else:
                print(f'на складе только {self.warehouse_dict.get(self.key)} штук {type(self).__name__}{self.key}')

        
class OfficeEquipment(Warehouse):

    def __init__(self, name, quantity, value):
        self.list = []
        self.quantity = quantity
        self.value = value
        for el in name, quantity, value:
            self.list.append(el)
        self.name = self.list
        if validate(self.quantity, self) == 1:
            self.name = []


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, value, colors):
        self.list = []
        self.quantity = quantity
        self.value = value
        self.colors = colors
        for el in name, quantity, value, colors:
            self.list.append(el)
        self.name = self.list
        if validate(self.quantity, self) == 1:
            self.name = []

class Xerox(OfficeEquipment):
    def __init__(self, name, quantity, value, colors):
        self.list = []
        self.quantity = quantity
        self.value = value
        self.colors = colors
        for el in name, quantity, value, colors:
            self.list.append(el)
        self.name = self.list
        if validate(self.quantity, self) == 1:
            self.name = []

class Scaner(OfficeEquipment):
    pass



print1 = Printer('hp', 25, 2000, 8)  # описываем товар
scan1 = Scaner('lenovo', 3, 12000)
xerox1 = Xerox('Samsung', 35, 5000, 4)
xerox1.to_warehouse(xerox1.name) # поставляем на склад
scan1.to_warehouse(scan1.name)
print1.to_warehouse(print1.name)
print1.from_warehouse(20)  # вывозим со склада определенное количество
xerox1.from_warehouse(15)
print(Warehouse.warehouse_dict)
