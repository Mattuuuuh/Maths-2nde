# Initialize

```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv init Animations
uv add manim
cd Animations/
manim init project Dichotomie --default
```

# Compile

```
cd dichotomie/
manim render -pql start.py
manim render -pqh start.py
```

# Todo

- [x] Dichotomie (à adapter)
- [ ] Plan cartésien
- [ ] Courbe représentative
- [ ] Fonctions parentes
- [ ] Signe affine
- [ ] Signe du produit
- [ ] Manipulation d'équation visuellement : évolutions, équations linéaires
- [ ] Inclusion-exclusion
- [ ] Vecteurs directeurs
- [ ] Statistiques descriptives : linéarité moyenne + quartiles
- [ ] Échantillonnage ?
- [ ] Variations : différents candidats de fonctions associées à un tableau de variations (concave, convexe, combinaisons, ..)
