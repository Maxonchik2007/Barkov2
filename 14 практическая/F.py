from random import randint
n = int(input("Введите количество элементов:\n"))
A = [randint(0, 5) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
max = 0
min = 0
for i in range(1, n):
    if A[i] >= A[max]:
        max = i
print("Максимальное значение:", A[max])
print("Количество элементов:", A.count(A[max]))

