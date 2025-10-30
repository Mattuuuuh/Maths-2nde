def F(x):
    return x*x

def G(x):
    return -100*x*x + 1

N = 1001
liste = [-1 + 2*k/N for k in range(N+1)]

for x in liste:
    if F(x) < G(x):
        print(x)
