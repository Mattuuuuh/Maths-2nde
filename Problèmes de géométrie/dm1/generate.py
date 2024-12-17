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

# reduce square root
def reduced_sqrt(n):
    a, b = 1, n
    k=2
    while k**2<=b:
        if b%(k**2) == 0:
            a*=k
            b=int(b/(k**2))
        else:
            k+=1
    return [a,b]

def generate(seed):
    CONTENT = newcommand("", "\seed", seed)

    # points A and B with integer coords in [-5,5]

    [xA, yA, xB, yB] = (np.random.rand(4)*12 - 6).astype(int)
    CONTENT = newcommand(CONTENT, "\\xA", xA)
    CONTENT = newcommand(CONTENT, "\yA", yA)
    CONTENT = newcommand(CONTENT, "\\xB", xB)
    CONTENT = newcommand(CONTENT, "\yB", yB)

    CONTENT = newcommand(CONTENT, "\Pnormsq", xA**2 + yA**2)
    CONTENT = newcommand(CONTENT, "\Bnormsq", xB**2 + yB**2)
    CONTENT = newcommand(CONTENT, "\BPnormsq", xB**2 + yB**2 - xA**2 - yA**2)

    # projection of B onto A

    numerator = xA*xB + yA*yB
    denominator = xA**2 + yA**2
    d = np.gcd(numerator, denominator)
    numerator = int(numerator/d)
    denominator = int(denominator/d)

    if (denominator == 1) and (numerator == 1):
        CONTENT = newcommand(CONTENT, "\LAMBDA", "")
    elif denominator == 1:
        CONTENT = newcommand(CONTENT, "\LAMBDA", numerator)
    else:
        CONTENT = newcommand(CONTENT, "\LAMBDA", "\dfrac{"+str(numerator)+"}{"+str(denominator)+"}")

    # random root in [7,10]
    root = int(np.random.rand()*4+7)
    CONTENT = newcommand(CONTENT, "\\xmax", root)
    halfroot = int(root/2)
    CONTENT = newcommand(CONTENT, "\ALPHA", halfroot if root%2 == 0 else "\dfrac{"+str(root)+"}{2}")
    
    # values of x to draw
    CONTENT = newcommand(CONTENT, "\\xfirst", int(root/3))
    CONTENT = newcommand(CONTENT, "\\xsecond", int(2*root/3))

    # constant area (base x height /2)
    # beta is constant * alpha²
    
    Csquared = (xA**2 + yA**2)*( ( xB - numerator/denominator*xA)**2 + (yB - numerator/denominator*yA)**2 )
    C = reduced_sqrt(Csquared)

    if C[0]%2 == 0:
        a = int(C[0]/2)
        prodovertwo = ("" if a==1 else str(a))  
        if root%2 == 0:
            BETA = str(halfroot**2*a) 
        else:
            BETA = "\dfrac{"+str(root**2*a)+"}4" 
    else:
        prodovertwo = "\dfrac{"+str(C[0])+"}2" 
        if root%2 == 0 and halfroot%2 == 0:
            BETA = str(int(halfroot**2*C[0]/2))
        elif root%2:
            BETA = "\dfrac{"+str(halfroot**2*C[0])+"}2"
        else:
            BETA = "\dfrac{"+str(root**2*C[0])+"}8"

    squarerootsuffix = "" if C[1] == 1 else "\sqrt{"+str(C[1])+"}"
    CONTENT = newcommand(CONTENT, "\prodovertwo", prodovertwo+squarerootsuffix)
    CONTENT = newcommand(CONTENT, "\BETA", BETA+squarerootsuffix)

    # WRITE TO FILE

    FILE_NAME = f"adr/vars_{seed}.adr"

    with open(FILE_NAME, 'w') as file:
        file.write(CONTENT)

    # COMPILE LATEX TWICE

    INPUTS = "\input{preamble.tex} \input{"+FILE_NAME+"} \input{dm1.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"

    #subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    #subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    # compile twice for references 
    
    return 0

if __name__=="__main__":

    # always the same 34 to recompile if needed
    np.random.seed(1729) # taxicab number

    for _ in range(1):
        ## SEED ##

        seed = int(np.random.rand() * (2**16 - 1))
        # uncomment to fix seed
        seed=1234

        np.random.seed(seed)
        
        generate(seed)




