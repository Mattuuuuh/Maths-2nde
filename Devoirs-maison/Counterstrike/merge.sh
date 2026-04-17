cd out/
echo "merging solutions"
pdftk $(ls *pdf) cat output ../DM_sols.pdf
echo "breaking up PDFs"
find *pdf -exec pdftk \{\} cat 1 output \{\}_1st.pdf \;
echo "merging without solutions"
pdftk $(ls *1st.pdf) cat output ../DM.pdf
echo "cleaning up"
rm *1st.pdf
