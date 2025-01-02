import subprocess
import numpy as  np

def newcommand(current_str, command, value):
    if command in ["\d", "\k", "\Q", "\P", "\\vert"]:
        prefix = "\\renewcommand"
    else:
        prefix = "\\newcommand"
    return current_str+prefix+"{"+command+"}{"+str(value)+"}\n"


def generate(seed):
    CONTENT = newcommand("", "\seed", seed)

    # number of trials N around 10k plus-minus 500
    N = 10**4 + (np.random.rand()-.5)*1000
    N=int(N)
    
    # Rouge 1/3 Bleu 1/2 et Vert 1/6
    toss = np.random.rand(N)
    R = np.sum(toss < 1/3)
    B = np.sum(toss < (1/3+.5)) - R
    V = N - R - B

    CONTENT = newcommand(CONTENT, "\\rouge", R)
    CONTENT = newcommand(CONTENT, "\\bleu", B)
    CONTENT = newcommand(CONTENT, "\\vert", V)
    
    # WRITE TO FILE

    FILE_NAME = f"adr/vars_{seed}.adr"

    with open(FILE_NAME, 'w') as file:
        file.write(CONTENT)

    # COMPILE LATEX TWICE

    INPUTS = "\\newif\ifdys \\newif\ifsolutions \input{preamble.tex} \\begin{document} \input{"+FILE_NAME+"} \input{serie2.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"

    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    #subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    # compile twice for references 
    
    return 0

if __name__=="__main__":

    # always the same 40 to recompile if needed
    np.random.seed(666) # devil D:

    for _ in range(34):
        ## SEED ##

        seed = int(np.random.rand() * (2**16 - 1))
        # uncomment to fix seed
        # seed=12345

        np.random.seed(seed)
        
        generate(seed)




