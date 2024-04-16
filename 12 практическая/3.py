x,d = map(int, input('Введите X и D:\n').split())
print('массив:')
a = []
c = x+d*4
for _ in range(5):
    a.append(c)
    c -= d
print(' '.join(str(i) for i in a))


