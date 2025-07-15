Pour compiler tous les fichiers `.tex` du dossier `figures` :
```
Sous Linux
```
cd figures
find . -name \*.tex -exec pdflatex \{\} \;
```
Sous Windows
```
cd figures
for /r %x in (*.tex) do pdflatex "%x"
```
Pour compiler les notes :
```
pdflatex -shell-escape 0-notes.tex
```

Optionnel :
Installer `xindy` pour l'index qui accepte les accents (éèà...).
```
sudo apt install xindy
```

Add parameter `-output-directory=out` after creating `/out/` folder to redirect out files (pdf included).


# Fork

Fork from CMT - Charlie's Math Template.

```
A personal template I have created for my own use.

A lot of the code is from the following sources:
1. https://github.com/tecosaur/BMC
2. https://github.com/lambdasolver/LaTeX
```
