number = input("Введите трехзначное число: ")
a = int(number[0]) + int(number[1])
b = int(number[1]) + int(number[2])
result = str(min(a, b)) + str(max(a, b))
print("Искомое число:", result)


