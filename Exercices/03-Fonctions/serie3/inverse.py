def f(x):
    return 1/x

N=100
liste = [-1 + 2*k/N for k in range(N+1)]

for x in liste:
    print(f(x))
