from random import randint
n = int(input('количество элементов в массиве '))
a = [randint(0, 5) for i in range(n)]
b = []
print('Массив', end = ' ')
print(*a)
for i in range(0, 6):
    if i in a:
        if a.count(i) > 1:
            b.append(i)
        else:
            pass
    else:
        pass
if len(b) >= 1:
    print('Есть:', ', '.join(str(i) for i in b))
else:
    print('нет')