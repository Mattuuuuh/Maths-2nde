def carre(x):
    return x*x

def carre_longueur(xA,yA,xB,yB):
    return carre(xA-xB)+carre(yA-yB)

def is_isosceles(xA,yA,xB,yB):
    return carre_longueur(xA,yA,0,0) == carre_longueur(xB,yB,0,0)

print(is_isosceles(-1,-3,3,-1))
