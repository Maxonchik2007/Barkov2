X, D = map(int,input('Введите X и D :\n').split())
print('массив:')
a = []
for _ in range(5):
    a.append(X)
    X += D
print(' '.join(str(i) for i in a))
