def sallary(hours,stake,bonus):
    return hours*stake+bonus


hours = [] # создаем пустые списки данных для сохранения информации(если вдруг потребуются)
stake = []
bonus = []
sallary_dict = {} # создаем пустой словарь для записи выходных данных
names = input('введите имена сотрудников через пробел : ').split()

for i in range(len(names)):
    name = names[i] # переменная для удобства записи
    hours.append(int(input(f'введите отработанные часы для работника {name} ')))
    stake.append(int(input(f'введите чсовую ствку для работника {name} ')))
    bonus.append(int(input(f'введите премию для работника {name} ')))
    sallary_dict[name] = sallary(hours[i],stake[i],bonus[i])


print(sallary_dict)

#print(hours)
#print(stake)
#print(bonus)