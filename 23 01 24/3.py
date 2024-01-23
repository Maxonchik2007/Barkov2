N = int(input('N='))
MKX = N
N = N**2
for i in range(1, N):
    a = i**2
    print('afor',a)
    if a % 100 == i:
        print(i)



