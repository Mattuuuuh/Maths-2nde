Pour compiler :
```
mkdir out adr
python3 generate.py
```

Pour fusionner :
```
cd out/
pdftk $(ls *.pdf) cat output merged.pdf
```
