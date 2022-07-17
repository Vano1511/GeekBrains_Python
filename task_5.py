class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):

    def draw(self):
        print(f'толщина линии {self.title} 1 мм')

class Pencil(Stationery):

    def draw(self):
        print(f'толщина линии {self.title} 2 мм')

class Handle(Stationery):

    def draw(self):
        print(f'толщина линии {self.title} 3 мм')

pen_1 = Pen('red pen')
pencil_1 = Pencil('gray pencil')
handle_1 = Handle('black handle')
pen_1.draw()
Stationery.draw(pencil_1)
pencil_1.draw()