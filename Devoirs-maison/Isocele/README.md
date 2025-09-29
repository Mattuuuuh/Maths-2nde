Pour compiler :
```
mkdir out adr
python3 generate.py
```
Sur TeXworks, il est possible de modifier l'action de Ctrl+T : Edit -> Preferences -> Typesetting -> Processing tools. Mettre Program : python3, et Arguments : generate.py.

Pour scinder :
```
cd out/
find name *pdf -exec pdftk \{\} cat 1 output \{\}_1stpage.pdf \;
```

Pour fusionner :
```
pdftk $(ls out/*.pdf) cat output merged.pdf
```

Fusionner deux A5 en un A4
```
pdfjam merged.pdf --nup '1x2' --suffix a4paper
```


