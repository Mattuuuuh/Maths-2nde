# donne les diviseurs de N
# non optimal (on pourrait se restreindre aux diviseurs premiers)
def diviseurs(N):
    diviseurs = []
    # pour k de 1 à racine carrée de N
    for k in range(1, int(N**.5) + 1):
        # si k divise N (le reste de la division euclidienne est 0)
        if N%k == 0:
            # ajouter k et N/k à la liste des diviseurs
            diviseurs+=[k, N//k]
    return diviseurs

print(diviseurs(24))
print(diviseurs(2**13-1))
print(diviseurs(2**15-1))
