def g(x):
    return x*x - x - 1

amplitude = 1e-5
x = 1
while g(x) < 0:
    x = x+amplitude

print("Encadrement : ", x-amplitude, "< phi <", x)
