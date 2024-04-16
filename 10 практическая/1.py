def summ(a, b):
    if a == b:
        return a
    return summ(a,b - 1) + b
a,b = map(int,input('Введите два натуральных числа:\n').split())
print(summ(a, b))
