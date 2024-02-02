n = int(input()) + 1
for num in range(1, n):
    num2 = num
    while num2 > 0:
        dig = num2 % 10
        num2 //= 10
        if dig == 0 or num % dig != 0:
            break
        else:
            print(num, end=' ')