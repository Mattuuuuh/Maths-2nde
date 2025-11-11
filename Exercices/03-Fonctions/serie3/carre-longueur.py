def carre(x):
    return x*x

def carre_longueur(xA,yA,xB,yB):
    return carre(xA-xB)+carre(yA-yB)

print(carre_longueur(2,1,-1,-3))
