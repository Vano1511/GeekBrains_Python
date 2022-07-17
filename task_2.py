class Road:

    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def all_Asphault(self):
        return self._lenght * self._width * 25 * 5/1000

length = int(input('введите длинну дороги в метрах : '))
width = int(input('введите ширину дороги в метрах : '))
road = Road(length, width)
print(f'на укладку асфальта дороги длинной {road._lenght}м и шириной {road._width}м уйдет  {road.all_Asphault()} тонн асфальта')