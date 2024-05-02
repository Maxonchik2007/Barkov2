a = input('Введите строку:')
b = input('Что меняем:')
c = input('Чем заменить:')
d = [ i for i in a.split(b)]
print('Результат: \n' + c.join(d))
