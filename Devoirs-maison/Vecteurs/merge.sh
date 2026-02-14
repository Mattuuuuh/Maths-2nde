
cd out/
echo "merging solutions"
pdftk $(ls *pdf) cat output ../DM_sols.pdf
echo "breaking up PDFs"
find *pdf -exec pdftk \{\} cat 1 output \{\}_1st.pdf \;
echo "merging without solutions"
pdftk $(ls *1st.pdf) cat output ../DM.pdf
echo "cleaning up"
rm *_1st.pdf

cd ../
echo "a5 to a4"
pdfjam DM.pdf --nup '1x2' --suffix a4
pdfjam DM_sols.pdf --nup '1x2' --suffix a4
