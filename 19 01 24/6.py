n = int(input('Введите натуральное число:\n'))
K = [0] * 10
while n > 0:
    dig = n % 10
    K[dig] += 1
    print(K)
    n //= 10
    if 2 in K:
        print('Да.')
        break
    else:
        print('Нет.')

