## Mathématiques en classe de 2nde.

# Notes de cours

Les notes de cours du dossier `/notes/` sont à compiler avec pdfLaTeX et le flag `-shell-escape`.

```
pdflatex -shell-escape notes.tex
```

Sur TeXworks, il faut aller dans Preferences, Typesetting, Tool Configuration (double click pdfLaTeX) et ajouter l'argument `-shell-escape`.

Contenu par chapitre :
- [x] Ensembles dénombrables
- [x] Arithmétique
- [x] Droite réelle et géométrie plane
- [x] Statistiques descriptives
- [x] Fonctions : généralités
- [x] Problèmes de géométrie
- [x] Probabilités
- [ ] Fonctions : variations et extrema
- [ ] Vecteurs dans le plan
- [ ] Fonctions : droites du plan
- [ ] Fonctions : fonctions de référence
- [ ] Échantillonnage

# Séries d'exercices, évaluations, automatismes, …

Les autres fichiers `.tex`se compilent sans précaution particulière. Les versions OpenDyslexic requièrent XeLaTeX et les polices OpenDyslexic et Fira Math.

Les automatismes avec réponses A/B utilisent ```tcolorbox``` et XeLaTeX est nécessaire pour avoir les polices correctes.
