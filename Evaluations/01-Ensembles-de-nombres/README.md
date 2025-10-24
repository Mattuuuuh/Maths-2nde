```
mkdir out
python3 randomized.py
```

Supprimer les évaluations dont la mise en page n'est pas bonne (trop de pages p.ex.).

```
cd out/
pdftk $(ls *pdf) cat output ../evaluation.pdf
```
