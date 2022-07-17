class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.position = position
        self.surname = surname
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'полное имя работника : {self.name} {self.surname}')

    def get_full_income(self):
        print(f'полный доход работника {self.name} равен {self._income.get("wage")+ self._income.get("bonus")}')

worker_1 = Worker('Bill', 'Armsnrong', 'engeneer', {'wage' : 2800, 'bonus' : 400})
pos_w = Position('Jack', 'Daniels', 'manager', {'wage' : 3500, 'bonus' : 700})
pos_1 = Position.get_full_name(pos_w)
pos_2 = pos_w.get_full_income()