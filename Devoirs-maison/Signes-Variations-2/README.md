Pour compiler :
```
mkdir out adr
python3 generate.py
```

Pour fusionner :
```
pdftk $(ls out/*.pdf) cat output merged.pdf
```
