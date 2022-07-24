class NoString(Exception):

    def __init__(self, text):
        self.text = text

def validate(new):
    try:
        return int(new)
    except Exception:
        return 1

numlist = []
new = 0
while new != 'stop':
    new = input('введите число, если хотите завершить ввод наберите stop ')
    mistake = NoString(validate(new))
    if mistake.text == 1:
        print('введено не число, прошу повторить')
    else:
        numlist.append(int(new))

print(numlist)