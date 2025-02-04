import subprocess
import numpy as  np

# heh
def newcommand(current_str, command, value):
    if command in ["\\sol", "\\c", "\\b", "\\a", "\d", "\k", "\Q", "\P"]:
        prefix = "\\renewcommand"
    else:
        prefix = "\\newcommand"
    
    if value == 1:
        value=""
    elif value == -1:
        value="-"
    return current_str+prefix+"{"+command+"}{"+str(value)+"}\n"

# huge mess
def newcommand_dfrac(current_str, command, numerator, denominator):
    d = np.gcd(numerator, denominator)
    numerator = int(numerator/d)
    denominator = int(denominator/d)
    if ((denominator == 1) and (numerator == 1)) or (numerator == 1):
        current_str = newcommand(current_str, command, "")
    elif denominator == 1:
        current_str = newcommand(current_str, command, numerator)
    else:
        if numerator < 0 and denominator < 0:
            numerator *= -1
            denominator *= -1
        current_str = newcommand(current_str, command, "\dfrac{"+str(numerator)+"}{"+str(denominator)+"}")
    return current_str

# write decimal separator with commas instead of dots
def comma(num):
    return f'{num}'.replace('.', ',')


###############################################

def write(CONTENT, seed):
    # WRITE TO FILE

    FILE_NAME = f"adr/vars_{seed}.adr"

    with open(FILE_NAME, 'w') as file:
        file.write(CONTENT)
    return 0

def pdflatex(seed):
    # COMPILE WITH VARS INPUT

    FILE_NAME = f"adr/vars_{seed}.adr"

    INPUTS = "\input{preamble.tex} \input{"+FILE_NAME+"} \input{dm1.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"

    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    #subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    # compile twice if references are required
    
    return 0


def generate(seed):
    CONTENT = newcommand("", "\seed", seed)

    # generate random integer ax + b = cx + d to solve, with a != c.
    [a,b,c,d] = (np.random.rand(4)*12 - 6).astype(int)
    while a == c:
        [a,b,c,d] = (np.random.rand(4)*12 - 6).astype(int)
   
    for s in ["a", "b", "c", "d"]:
        CONTENT = newcommand(CONTENT, f"\\{s}", eval(s))

    CONTENT = newcommand_dfrac(CONTENT, f"\\sol", d-b, a-c)

    return CONTENT    

    return 0

if __name__=="__main__":

    N = 1
    # always the same N to recompile if needed
    np.random.seed(51) # not a prime 

    for _ in range(N):
        ## SEED ##
        seed = int(np.random.rand() * (2**16 - 1))

        # uncomment to fix seed
        #seed=10354

        np.random.seed(seed)
        
        CONTENT = generate(seed)
        write(CONTENT, seed)
        pdflatex(seed)




