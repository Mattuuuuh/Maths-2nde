Pour compiler :
```
mkdir out adr
python3 generate.py
```
Sur TeXworks, il est possible de modifier l'action de Ctrl+T : Edit -> Preferences -> Typesetting -> Processing tools. Mettre Program : python3, et Arguments : generate.py.

Pour fusionner :
```
cd out/
pdftk $(ls *pdf) cat output ../DM_sols.pdf
find *pdf -exec pdftk \{\} cat 1 output \{\}_1st.pdf
pdftk $(ls *1st.pdf) cat output ../DM.pdf

cd ../
pdfjam DM.pdf --nup '1x2' --suffix a4
pdfjam DM_sols.pdf --nup '1x2' --suffix a4
```
