import sys
sys.setrecursionlimit(5000)
def f(n):
    return g(n - 1)
def g(n):
    if n < 10:
        return n
    elif n >= 10:
        return g(n - 2) + 1
c = 0
for i in range(1, 101):
    for j in range(1,11):
        if f(i) == j ** 2:
            c += 1
print(f'всего таких чисел {c}')