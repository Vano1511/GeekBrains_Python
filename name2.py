input_time = int(input('Введите время в секундах: '))

seconds = input_time % 60
input_time = input_time // 60

minutes = input_time % 60
hours = input_time // 60

text = 'Введенное время составляет: {0}:{1}:{2}'.format(hours,minutes,seconds)

print(text)