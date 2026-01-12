## Mathématiques en classe de 2nde.

# Notes de cours

Les images `tikz` sont à compiler avant la compilation des notes de cours. Chaque fichier `.tex` du dossier `/Notes-de-cours/figures/` est donc à compiler. 

Les notes de cours du dossier `/Notes-de-cours/` sont à compiler avec pdfLaTeX et le flag `-shell-escape`.

```
pdflatex -shell-escape 0-notes.tex
```

Sur TeXworks, il faut aller dans Preferences, Typesetting, Tool Configuration (double click pdfLaTeX) et ajouter l'argument `-shell-escape`.

Contenu par chapitre :
1. [x] Nombres rationnels, nombres réels
2. [x] Plan cartésien
3. [x] Fonctions
4. [x] Évolution chiffrée
5. [x] Fonctions carré, racine carrée, valeur absolue
6. [x] Arithmétique
7. [x] Problèmes de géométrie
8. [x] Fonctions affines
9. [x] Probabilités
10. [x] Vecteurs
11. [x] Signes et fonction inverse
12. [ ] Statistiques descriptives
13. [ ] Échantillonnage
14. [x] Variations et extrema

# Devoirs maison

Les devoirs maison appartiennent au dossier `/Devoirs-maison/`.
Le dossier `/00-DM-Template/` donne un exemple de DM.

Dans chaque sous-dossier, il est toujours nécessaire de créer les dossier `/adr/` et `/out/`.
Le fichier `DM.py` contient la classe `DM` ainsi que quelques fonctions utilitaires pour créer les DM.
Le fichier `preamble.tex` est le préamble LaTeX, à changer si nécessaire (pacakages, macros,...).

La repo contient les DM suivants.
- [x] Lagrange
- [x] Diophantes
- [x] Triangle isocèle
- [x] Triangle rectangle
- [x] Forme canonique
- [ ] Triangle équilatéral affine
- [ ] Évolution
- [ ] Statistiques descriptives
- [ ] Trigonométrie
- [ ] Pente affine
- [ ] Signes
- [ ] Systèmes

# Séries d'exercices

Un exemple d'exercice est présent dans le dossier `/Exercices/00-Exercise-Template/`.
Les exercices et les solutions sont compilés au même moment, dans le même pdf.
L'avantage est de n'avoir qu'un seul fichier à téléverser sur le moodle (et ça ne me dérange pas de donner les solutions au même moment que les exercices).
Si nécessaire, `pdftk` permet de scinder les pdfs :
```
pdftk serie1.pdf cat 1-2 output set1.pdf
```

# Évaluations

Les évaluations appartiennent au dossier `/Evaluations/`.
Elles héritent du même système que les exercices.
Pour afficher le barème, le titre de chaque exercice doit être un nombre entier de points.
Le barème s'ajoute au compteur `points`.

# Automatismes

Les automatismes avec réponses A/B utilisent ```tcolorbox``` et XeLaTeX est nécessaire pour avoir les polices correctes.

# Animations

Les animations sont créées à l'aide de la libraire `manim` (https://docs.manim.community/en/stable/tutorials/quickstart.html).
Les instructions sont décrites dans le dossier `/Animations/`.
Comme les dépendances de `manim` sont assez strictes, un environnement Python est crée à l'aide de `uv`.
Généralement, les fichiers `main.py` ne contiennent qu'une seule scène à compiler.

```
manim render -pql main.py # low quality
manim render -pqh main.py # high quality
```

Playlist : 
https://youtube.com/playlist?list=PLB_8HoiptnmTKHbJjzLUVCFA0TooGBdgm&si=jRlpyESVkWWS6rv-

# TODO

- Adapter les anciens DM au nouveau système.
- Adapter les exercices au nouveau système.
- Adapter les évaluations au nouveau système.

DM à réfléchir :
- Nombres réels
- Plan cartésien
- Projeté orthogonal
- Arithmétique
- Probabilités
- Vecteurs (systèmes ?)
- Variations
- Échantillonnage

Animations à créer :
- [x] Moyenne pondérée, segment en 2d (revoir les zoom).
- [x] Dichotomie (fonction à adapter)
- [x] Plan cartésien
- [x] Courbe représentative (revoir les zoom)
- [ ] Fonctions parentes
- [ ] Signe affine
- [x] Signe du produit
- [x] Résolution graphique d'inégalités
- [ ] Manipulation d'équation visuellement : évolutions, équations linéaires
- [ ] Trigonométrie, quart de cercle unité
- [ ] Inclusion-exclusion
- [ ] Vecteurs directeurs
- [ ] Statistiques descriptives : linéarité moyenne + quartiles
- [ ] Échantillonnage ?
- [ ] Variations : différents candidats de fonctions associées à un tableau de variations (concave, convexe, combinaisons, ..)





##
