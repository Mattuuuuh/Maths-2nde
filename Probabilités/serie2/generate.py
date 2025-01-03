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

    # ex4 (rouge bleu vert)

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
    
    # ex5 (d6)
    
    # number of trials N around 100k plus-minus 5000
    N = 10**5 + (np.random.rand()-.5)*10**4
    N=int(N)
    
    # P = (.2, .3, .1, .15, .2, .05)
    # Pcum = (.2, .5, .6, .75, .95, 1)
    toss = np.random.rand(N)
    un = np.sum(toss < .2)
    deux = np.sum(toss < .5) - un
    trois = np.sum(toss < .6) - deux - un
    quatre = np.sum(toss < .75) - trois - deux - un
    cinq = np.sum(toss < .95) - quatre - trois - deux - un
    six = N - cinq - quatre - trois - deux - un
    
    for num in ["un", "deux", "trois", "quatre", "cinq", "six"]:
        CONTENT = newcommand(CONTENT, f"\\{num}", eval(num))
    
    # WRITE TO FILE

    FILE_NAME = f"adr/vars_{seed}.adr"

    with open(FILE_NAME, 'w') as file:
        file.write(CONTENT)

    # COMPILE LATEX TWICE

    INPUTS = "\\newif\ifdys \\newif\ifsolutions \input{../preamble.tex} \\begin{document} \input{"+FILE_NAME+"} \input{serie2.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"

    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    #subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    # compile twice for references 
    
    return 0

if __name__=="__main__":

    # always the same 40 to recompile if needed
    np.random.seed(666) # devil D:

    for _ in range(38):
        ## SEED ##

        seed = int(np.random.rand() * (2**16 - 1))
        # uncomment to fix seed
        # seed=789

        np.random.seed(seed)
        
        generate(seed)




