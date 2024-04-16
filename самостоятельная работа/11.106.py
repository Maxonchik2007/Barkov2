def massiv(a):
    maxmass = 0
    cu = 0
    for i in a:
        if i % 2 != 0:
            cu += 1
            maxmass = max(maxmass, cu)
        else:
            cu = 0
    return maxmass
a = [2, 5, 6, 7, 9, 11, 81, 10,13]
resultat = massiv(a)
print(f'длина наибольшего отрезка несчетных чисел в массиве:{resultat}')

