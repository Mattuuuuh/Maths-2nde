N=1000
liste = [ 1 + k/N for k in range(N+1)]

for x in liste:
    if x**2 < 2:
        print(x)
