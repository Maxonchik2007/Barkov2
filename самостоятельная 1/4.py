def f(n):
    if n < 2:
        return n
    if n >= 2:
        return f(n // 2) + f(n % 2)
a = 0
for i in range(27, 2**12):
    print(f'при {i} f = {f(i)}')
    a += 1
print(a)


