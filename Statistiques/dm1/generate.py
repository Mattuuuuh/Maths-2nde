import subprocess
import numpy as  np

def newcommand(current_str, command, value):
    if command in ["\d", "\k", "\Q", "\P"]:
        prefix = "\\renewcommand"
    else:
        prefix = "\\newcommand"
    return current_str+prefix+"{"+command+"}{"+str(value)+"}\n"

# write decimal separator with commas instead of dots
def comma(num):
    return f'{num}'.replace('.', ',')

def generate(seed):
    CONTENT = newcommand("", "\seed", seed)

    ## EX 1

    
    [A,B] = np.random.rand(2)*1900+100
    A, B = int(A), int(B)

    CONTENT = newcommand(CONTENT, "\A", A)
    CONTENT = newcommand(CONTENT, "\B", B)

    # EX 2

    [P, D1, D2, D3] = np.random.rand(4)*600+50
    P = int(P)
    P2 = P+int(D1)
    P3 = P2+int(D2)
    P4 = P3+int(D3)

    CONTENT = newcommand(CONTENT, "\P", P)
    CONTENT = newcommand(CONTENT, "\PP", P2)
    CONTENT = newcommand(CONTENT, "\PPP", P3)
    CONTENT = newcommand(CONTENT, "\PPPP", P4)

    [Q, D1, D2, D3] = np.random.rand(4)*200+50
    Q = int(Q)
    Q2 = Q+int(D1)
    Q3 = Q2+int(D2)
    Q4 = Q3+int(D3)

    CONTENT = newcommand(CONTENT, "\Q", Q4)
    CONTENT = newcommand(CONTENT, "\QQ", Q3)
    CONTENT = newcommand(CONTENT, "\QQQ", Q2)
    CONTENT = newcommand(CONTENT, "\QQQQ", Q)

    # j'aurais aimé déclarer la TVA avant mais maintenant c'est fait et ça modifie le seed de la déplacer
    TVA = int(np.random.rand()*40 +5)
    CONTENT = newcommand(CONTENT, "\TVA", TVA)
    Pfixe = int(np.random.rand()*P/2 + 20)

    CONTENT = newcommand(CONTENT, "\PFIXE", Pfixe)

    # EX 3

    [remise, aug] = np.random.rand(2)*[100, 300] + 5
    remise, aug = int(remise), int(aug)
    dim = int(np.random.rand()*remise/2 + 2)

    CONTENT = newcommand(CONTENT, "\REMISE", remise)
    CONTENT = newcommand(CONTENT, "\FINALaug", aug)
    CONTENT = newcommand(CONTENT, "\FINALdim", dim)

    ### HISTOGRAM

    Conca = int(np.random.rand()*12)+2
    [EffConca, EffConcb, EffConcc, EffConcd] = np.random.rand(4)*20+3
    EffConca, EffConcb, EffConcc, EffConcd = int(EffConca), int(EffConcb), int(EffConcc), int(EffConcd)

    CONTENT = newcommand(CONTENT, "\CONCa", Conca)
    CONTENT = newcommand(CONTENT, "\CONCb", Conca+1)
    CONTENT = newcommand(CONTENT, "\CONCc", Conca+2)
    CONTENT = newcommand(CONTENT, "\CONCd", Conca+3)
    CONTENT = newcommand(CONTENT, "\EFFCONCa", EffConca)
    CONTENT = newcommand(CONTENT, "\EFFCONCb", EffConcb)
    CONTENT = newcommand(CONTENT, "\EFFCONCc", EffConcc)
    CONTENT = newcommand(CONTENT, "\EFFCONCd", EffConcd)


    [Dispa, Dispd] = np.random.rand(2)*8
    Dispa = int(Dispa)
    Dispd = int(Dispd)+Dispa+4

    [EffDispa, EffDispb, EffDispc, EffDispd, EffDispe] = np.random.rand(5)*20+3
    EffDispa, EffDispb, EffDispc, EffDispd, EffDispe = int(EffDispa), int(EffDispb), int(EffDispc), int(EffDispd), int(EffDispe)

    CONTENT = newcommand(CONTENT, "\DISPa", Dispa)
    CONTENT = newcommand(CONTENT, "\DISPb", Dispa+1)
    CONTENT = newcommand(CONTENT, "\DISPc", Dispa+2)
    CONTENT = newcommand(CONTENT, "\DISPd", Dispd)
    CONTENT = newcommand(CONTENT, "\DISPe", Dispd+1)
    CONTENT = newcommand(CONTENT, "\EFFDISPa", EffDispa)
    CONTENT = newcommand(CONTENT, "\EFFDISPb", EffDispb)
    CONTENT = newcommand(CONTENT, "\EFFDISPc", EffDispc)
    CONTENT = newcommand(CONTENT, "\EFFDISPd", EffDispd)
    CONTENT = newcommand(CONTENT, "\EFFDISPe", EffDispe)

    
    # EX 1 SOLUTION

    Asol = np.round((1+TVA/100)*A,2)
    CONTENT = newcommand(CONTENT, "\Asol", comma(Asol))
    Bsol = np.round(B/(1+TVA/100),2)
    CONTENT = newcommand(CONTENT, "\Bsol", comma(Bsol))

    gcd = np.gcd(TVA, 100+TVA)
    rationum = int(TVA/gcd)
    ratiodenom = int((100+TVA)/gcd)
    
    CONTENT = newcommand(CONTENT, "\\rationum", rationum)
    CONTENT = newcommand(CONTENT, "\\ratiodenom", ratiodenom)
   
    # EX 2 SOLUTION

    average = (P*Q4+P2*Q3+P3*Q2+P4*Q)/(Q+Q2+Q3+Q4)
    CONTENT = newcommand(CONTENT, "\\average", comma(np.round(average,2)))

    evol = lambda x : comma(np.round(x/(1+TVA/100) - Pfixe,2))

    CONTENT = newcommand(CONTENT, "\Psol", evol(P))
    CONTENT = newcommand(CONTENT, "\PPsol", evol(P2))
    CONTENT = newcommand(CONTENT, "\PPPsol", evol(P3))
    CONTENT = newcommand(CONTENT, "\PPPPsol", evol(P4))
   
    newaverage = evol(average)
    CONTENT = newcommand(CONTENT, "\\newaverage", newaverage)

    # EX 3 SOLUTION

    reciproque = np.round(1/(1-remise/100),2)
    CONTENT = newcommand(CONTENT, "\\reciproque", comma(reciproque))
    recsol = int(100*(reciproque-1))
    CONTENT = newcommand(CONTENT, "\\recsol", recsol)

    evoldeux = np.round((1+aug/100)/(1-remise/100),2)
    CONTENT = newcommand(CONTENT, "\\evoldeux", comma(evoldeux))
    FINALaugsol = int(100*(evoldeux-1))
    CONTENT = newcommand(CONTENT, "\\FINALaugsol", FINALaugsol)
    
    evoltrois = np.round((1-dim/100)/(1-remise/100),2)
    CONTENT = newcommand(CONTENT, "\\evoltrois", comma(evoltrois))
    FINALdimsol = int(100*(evoltrois-1))
    CONTENT = newcommand(CONTENT, "\\FINALdimsol", FINALdimsol)
    
    # EX 4a SOLUTION

    vala = Conca+.5
    valb = Conca+1.5
    valc = Conca+2.5
    vald = Conca+3.5

    CONTENT = newcommand(CONTENT, "\\vala", comma(vala))
    CONTENT = newcommand(CONTENT, "\\valb", comma(valb))
    CONTENT = newcommand(CONTENT, "\\valc", comma(valc))
    CONTENT = newcommand(CONTENT, "\\vald", comma(vald))
    
    N = EffConca + EffConcb + EffConcc + EffConcd
    X = [vala]*EffConca + [valb]*EffConcb + [valc]*EffConcc + [vald]*EffConcd
    assert len(X) == N
    
    Concaverage = comma(np.round(np.mean(X),2))
    Concstd = comma(np.round(np.std(X),2))
    Concmedian = comma(np.round(np.median(X),1))
    Concfirstquartile = X[int(np.ceil(N/4))]
    Concthirdquartile = X[int(np.ceil(3*N/4))]
    Concecart = Concthirdquartile - Concfirstquartile
    if Concecart == int(Concecart) : Concecart=int(Concecart)


    CONTENT = newcommand(CONTENT, "\Concaverage", Concaverage)
    CONTENT = newcommand(CONTENT, "\Concstd", Concstd)
    CONTENT = newcommand(CONTENT, "\Concmedian", Concmedian)
    CONTENT = newcommand(CONTENT, "\Concfirstquartile", comma(Concfirstquartile))
    CONTENT = newcommand(CONTENT, "\Concthirdquartile", comma(Concthirdquartile))
    CONTENT = newcommand(CONTENT, "\Concecart", comma(Concecart))

    # EX 4b SOLUTION
   
    vala = Dispa+.5
    valb = Dispa+1.5
    valc = Dispa+2.5
    vald = Dispd+.5
    vale = Dispd+1.5

    CONTENT = newcommand(CONTENT, "\\valA", comma(vala))
    CONTENT = newcommand(CONTENT, "\\valB", comma(valb))
    CONTENT = newcommand(CONTENT, "\\valC", comma(valc))
    CONTENT = newcommand(CONTENT, "\\valD", comma(vald))
    CONTENT = newcommand(CONTENT, "\\valE", comma(vale))
    
    N = EffDispa + EffDispb + EffDispc + EffDispd + EffDispe
    X = [vala]*EffDispa + [valb]*EffDispb + [valc]*EffDispc + [vald]*EffDispd + [vale]*EffDispe
    assert len(X) == N
    
    Dispaverage = comma(np.round(np.mean(X),2))
    Dispstd = comma(np.round(np.std(X),2))
    Dispmedian = comma(np.round(np.median(X),1))
    Dispfirstquartile = X[int(np.ceil(N/4))]
    Dispthirdquartile = X[int(np.ceil(3*N/4))]
    Dispecart = Dispthirdquartile - Dispfirstquartile
    if Dispecart == int(Dispecart) : Dispecart=int(Dispecart)

    CONTENT = newcommand(CONTENT, "\Dispaverage", Dispaverage)
    CONTENT = newcommand(CONTENT, "\Dispstd", Dispstd)
    CONTENT = newcommand(CONTENT, "\Dispmedian", Dispmedian)
    CONTENT = newcommand(CONTENT, "\Dispfirstquartile", comma(Dispfirstquartile))
    CONTENT = newcommand(CONTENT, "\Dispthirdquartile", comma(Dispthirdquartile))
    CONTENT = newcommand(CONTENT, "\Dispecart", comma(Dispecart))

    # WRITE TO FILE

    FILE_NAME = f"adr/vars_{seed}.adr"

    with open(FILE_NAME, 'w') as file:
        file.write(CONTENT)

    # COMPILE LATEX TWICE

    INPUTS = "\input{preamble.tex} \input{"+FILE_NAME+"} \input{dm1.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"

    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    # compile twice for references 
    
    return 0

if __name__=="__main__":

    # always the same 34 just in case...
    np.random.seed(42)

    for _ in range(34):
        ## SEED ##

        seed = int(np.random.rand() * (2**16 - 1))
        # uncomment to fix seed
        #seed=45294
        np.random.seed(seed)

        generate(seed)




