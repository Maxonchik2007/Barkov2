from random import randint

n = int(input('Введите количество элементов:'))
a = [randint(-100,100)for _ in range(n)]
print(f'Массив A:\n{" ".join(str(i) for i in a)}')
print(*a[(len(a) // 2) - 1:: -1], end=' ')
print(*a[:(len(a) // 2) - 1: -1])
