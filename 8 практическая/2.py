def prime(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 'Составное число'
        return 'Простое число'
for n in range(9900000,12000000):
    print(prime(n))

