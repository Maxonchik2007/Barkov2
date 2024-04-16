def calkulator(a):
    sumapologit = sum(i for i in a if i > 0)
    sumaotricat = sum(abs(i) for i in a if i < 0)
    if sumaotricat == 0:
        return 'На 0 делить нельзя'
    b = sumapologit / sumaotricat
    return b
spisok = [1, -2, 3, -4, 5]
resultat = calkulator((spisok))
print(resultat)
