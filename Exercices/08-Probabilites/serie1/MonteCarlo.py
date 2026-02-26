import numpy as np

# génère un point dans [0,1]x[0,1]
def random_point():
    x = np.random.rand()
    y = np.random.rand()
    return x,y

# calcul la distance au carré de (x,y) à l'origine (0,0)
def distance_squared(x,y):
    return x*x + y*y

# renvoie 1 si la distance de (x,y) à (0,0) est inférieure à 1...
# renvoie 0 sinon.
def is_distance_less():
    d = distance_squared(random_point())
    if d <= 1:
        return 1
    return 0

# nombre de point à générer
N = 10**7

# TODO!
