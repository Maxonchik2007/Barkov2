def m_e(a, b):
    if b == 0:
        return a
    return m_e(b, a % b)
a,b = map(int,input('').split())
print(f'НОД({a},{b}) = {m_e(a,b)}. ')
