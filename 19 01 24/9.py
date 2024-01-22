x, y, p = [int(i) for i in input('Введите три целых числа\n').split()]
g = 0
while x <= y:
    x += y
    g += 1
print(g)