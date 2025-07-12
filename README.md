## Mathématiques en classe de 2nde.

# Notes de cours

Les images `tikz` sont à compiler avant la compilation des notes de cours. Chaque fichier `.tex` du dossier `/notes/figures/` est donc à compiler. 

Les notes de cours du dossier `/notes/` sont à compiler avec pdfLaTeX et le flag `-shell-escape`.

```
pdflatex -shell-escape notes.tex
```

Sur TeXworks, il faut aller dans Preferences, Typesetting, Tool Configuration (double click pdfLaTeX) et ajouter l'argument `-shell-escape`.

Contenu par chapitre :
1. [x] Nombres rationnels, nombres réels
2. [x] Plan cartésien
3. [ ] Fonctions
4. [ ] Évolution chiffrée
5. [x] Fonctions carré, racine carrée, valeur absolue
6. [x] Arithmétique
7. [ ] Problèmes de géométrie
8. [x] Fonctions affines
9. [x] Probabilités
10. [ ] Vecteurs
11. [ ] Signes et fonction inverse
12. [ ] Statistiques descriptives
13. [ ] Échantillonnage
14. [ ] Variations et extrema

# Devoirs maison

Les devoirs maison ont leur propre README rudimentaires dans les dossiers nommés `/dm*/`.
Chacun a ses fichiers `preamble.tex`, `dm*.tex`, et `generate.py` ; ce dernier permettant de générer les devoirs après création des dossiers `/out/` et `/adr/` si nécessaire.

La repo contient les DM suivants.
- [x] Statistiques 1 (`/Statistiques/dm1/`)
- [x] Statistiques 2 (`/Statistiques/dm2/`)
- [x] Problèmes de géométrie 1 (`/Problèmes de géométrie/dm1/`)
- [x] Fonctions affines (`/Fonctions-affines/dm1/`)
- [~] Signes et variations 2 (`/Signes-variations/dm2/`)
- [x] Systèmes 1 (`/Systèmes/dm1/`)

- [ ] Problèmes de géométrie 2 (`/Problèmes de géométrie/dm2/`)
- [ ] Signes et variations 1 (`/Signes-variations/dm1/`)

TODO : 
- unifier les scripts en un module avec documentation ;
- implémenter l'ex 2 de Signes et variations 2 ;
- revisiter Signes et variations 1 sur l'interpolation de Lagrange ;

# Séries d'exercices, évaluations, automatismes, …

Les autres fichiers `.tex`se compilent sans précaution particulière. Les versions OpenDyslexic requièrent XeLaTeX et les polices OpenDyslexic et Fira Math.

Les automatismes avec réponses A/B utilisent ```tcolorbox``` et XeLaTeX est nécessaire pour avoir les polices correctes.
