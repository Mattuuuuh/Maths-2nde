# nombre de multiples de 3 ou de 5
# initialisé à 0
N = 0

# boucle n = 1, 2, 3, ..., 1000
# range(a,b) correspond aux entiers de l'intervalle [a, b[
for n in range(1,1001):
    # si n est divisible par 3 ou n est divisible par 5
    # a%b correspond au reste de la division euclidienne de a par b.
    if n%3 == 0 or n%5 == 0:
        # ajouter 1 à N
        N = N + 1

# imprimer N
print(N)
