def f(x):
    return x*x - 700

amplitude = 1e-4
x = 20
while f(x) < 0:
    x = x+amplitude

print("Encadrement : ", x-amplitude, "< racine de 700 <", x)
