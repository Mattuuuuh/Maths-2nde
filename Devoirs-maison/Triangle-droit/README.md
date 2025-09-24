Pour compiler :
```
mkdir out adr
python3 generate.py
```
Sur TeXworks, il est possible de modifier l'action de Ctrl+T : Edit -> Preferences -> Typesetting -> Processing tools. Mettre Program : python3, et Arguments : generate.py.

Pour fusionner :
```
pdftk $(ls out/*.pdf) cat output merged.pdf
```

Fusionner deux A5 en un A4
```
pdfjam seed_0.pdf --nul '1x2'
```
