# Initialize

```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv init Animations
uv add manim
cd Animations/
manim init project dichotomie --default
```

# Compile

```
cd dichotomie/
manim render -pql start.py
manim render -pqh start.py
```

# Todo

- [x] Dichotomie (fonction à adapter)
- [x] Plan cartésien
- [x] Courbe représentative (revoir les zoom)
- [ ] Fonctions parentes
- [ ] Signe affine
- [x] Signe du produit
- [ ] Manipulation d'équation visuellement : évolutions, équations linéaires
- [ ] Trigonométrie, quart de cercle unité
- [ ] Inclusion-exclusion
- [ ] Vecteurs directeurs
- [ ] Statistiques descriptives : linéarité moyenne + quartiles
- [ ] Échantillonnage ?
- [ ] Variations : différents candidats de fonctions associées à un tableau de variations (concave, convexe, combinaisons, ..)
