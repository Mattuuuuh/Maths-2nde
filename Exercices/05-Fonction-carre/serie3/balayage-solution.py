def f(x):
    return x*x - 7

amplitude = 0.2
x = 0
while f(x) < 0:
    x = x+amplitude

print("Encadrement : ", x-amplitude, "< racine de 7 <", x)
