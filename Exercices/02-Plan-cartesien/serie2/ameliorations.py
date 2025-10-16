# prendre 100 valeurs entre 0 et 1
liste = [i/100 for i in range(101)]

# importer les colormaps
import matplotlib.cm as cm
# ajouter le point (2;3) avec couleur 0.5
plt.scatter(2,3, c=cm.rainbow(0.5))

# afficher un quadrillage
plt.grid()

# centrer les axes
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# définir les plages en x et y
plt.xlim(-2, 4)
plt.ylim(-2, 5)

# calcul de lambda en abscisses
xM = 1
xlam = (xM - 3)/(-2)
