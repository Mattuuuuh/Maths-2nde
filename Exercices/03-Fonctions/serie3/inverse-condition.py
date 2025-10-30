def f(x):
    if x == 0:
        return "undefined"
    return 1/x

liste = [-1 + 2*k/100 for k in range(101)]

for x in liste:
    print(f(x))
