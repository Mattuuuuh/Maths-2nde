Pré-requis : contfrac pour la fraction continue de l/L.
```
pip install contfrac
```

Pour compiler :
```
mkdir out adr
python3 generate.py
```

Pour fusionner :
```
pdftk $(ls out/*.pdf) cat output merged.pdf
```
