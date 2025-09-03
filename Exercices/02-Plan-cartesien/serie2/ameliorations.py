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

# définir les bornes en x et y
plt.xlim(-2, 4)
plt.ylim(-2, 5)
