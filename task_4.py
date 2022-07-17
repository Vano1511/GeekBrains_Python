class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'машина {self.name} поехала')


    def stop(self):
        print(f'машина {self.name} остановилась')

    def turn(self, direction):
        if direction == 'l':
            print(f'машина {self.name} повернула влево')
        elif direction == 'r':
            print(f'машина {self.name} повернула вправо')
        elif direction == 'b':
            print(f'машина {self.name} развернулась')
        else:
            print(f'машина {self.name} продолжает двигаться')

    def show_speed(self):
        print(f'скорость {self.name} - {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'скорость {self.name} больше допустимой')
        else:
            print(f'скорость {self.name} - {self.speed}')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'скорость {self.name} больше допустимой')
        else:
            print(f'скорость {self.name} - {self.speed}')

class PoliceCar(Car):
    pass
class SportCar(Car):
    pass

sport_1 = SportCar(250, 'green', 'BMW', False)
police_1 = PoliceCar(280, 'white-black', 'Lada', True)
town_1 = TownCar(80, 'red', 'Mazda', False)
work_1 = WorkCar(40, 'yellow', 'MTZ', False)
sport_1.go()
sport_1.show_speed()
police_1.go()
sport_1.turn('l')
police_1.stop()
town_1.go()
town_1.show_speed()