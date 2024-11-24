import subprocess
import numpy as  np

def newcommand(current_str, command, value):
    if command in ["\d", "\k", "\Q", "\P"]:
        prefix = "\\renewcommand"
    else:
        prefix = "\\newcommand"
    return current_str+prefix+"{"+command+"}{"+str(value)+"}\n"

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

    TVA = int(np.random.rand()*40 +5)
    Pfixe = int(np.random.rand()*P/2 + 20)

    CONTENT = newcommand(CONTENT, "\TVA", TVA)
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
    Dispd = int(Dispd)+Dispa+6

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

    FILE_NAME = f"adr/vars_{seed}.adr"

    with open(FILE_NAME, 'w') as file:
        file.write(CONTENT)

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
        print(seed)
        # uncomment to fix seed
        #seed=59583
        np.random.seed(seed)

        generate(seed)




