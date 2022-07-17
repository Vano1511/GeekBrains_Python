from itertools import cycle
from time import sleep


class TrafficLight:
    def running(lights, times):
        count = 0
        for el in cycle(lights):
             if count < times:
                 print(el[0])
                 sleep(el[1])
                 count +=1
             else:
                 break

lights = [['Green', 4], ['Yellow', 1], ['Red', 3]]
times = int(input('введите количество желаемых переключений : '))
TrafficLight.running(lights, times)