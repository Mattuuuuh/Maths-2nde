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
- [x] Fonctions : droites du plan
- [x] Vecteurs dans le plan
- [ ] Fonctions : variations et extrema
- [ ] Algorithmique
- [ ] Fonctions : fonctions de référence
- [ ] Échantillonnage

# Devoirs maison

Les devoirs maison ont leur propre README rudimentaires dans les dossiers nommés `/dm*`.
Chacun a ses fichiers `preamble.tex`, `dm*.tex`, et `generate.py` ; ce dernier permettant de générer les devoirs après création des dossiers `out/` et `adr/` si nécessaire.
La repo contient les DM suivants.
- [x] Statistiques 1 (`/Statistiques/dm1`)
- [x] Statistiques 2 (`/Statistiques/dm2`)
- [x] Problèmes de géométrie 1 (`/Problèmes de géométrie/dm1`)
- [x] Fonctions affines (`/Fonctions-affines/dm1`)
- [ ] Problèmes de géométrie 2 (`/Problèmes de géométrie/dm2`)

# Séries d'exercices, évaluations, automatismes, …

Les autres fichiers `.tex`se compilent sans précaution particulière. Les versions OpenDyslexic requièrent XeLaTeX et les polices OpenDyslexic et Fira Math.

Les automatismes avec réponses A/B utilisent ```tcolorbox``` et XeLaTeX est nécessaire pour avoir les polices correctes.
