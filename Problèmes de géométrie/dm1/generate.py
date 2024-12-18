import subprocess
import numpy as  np

def newcommand(current_str, command, value):
    if command in ["\d", "\k", "\Q", "\P"]:
        prefix = "\\renewcommand"
    else:
        prefix = "\\newcommand"
    return current_str+prefix+"{"+command+"}{"+str(value)+"}\n"

def newcommand_dfrac(current_str, command, numerator, denominator):
    if (denominator == 1) and (numerator == 1):
        current_str = newcommand(current_str, command, "")
    elif denominator == 1:
        current_str = newcommand(current_str, command, numerator)
    else:
        current_str = newcommand(current_str, command, "\dfrac{"+str(numerator)+"}{"+str(denominator)+"}")
    return current_str
# write decimal separator with commas instead of dots
def comma(num):
    return f'{num}'.replace('.', ',')


##### UNUSED (merci les mathématiques :)) #####
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
###############################################

def generate(seed):
    CONTENT = newcommand("", "\seed", seed)

    # points A and B with integer coords in [-5,5]
    xA=yA=xB=yB=0 
    while xA*yA*xB*yB == 0 or xA*xB + yA*yB == 0 or xA*yB - xB*yA == 0:
        [xA, yA, xB, yB] = (np.random.rand(4)*12 - 6).astype(int)
        print(xA,yA,xB,yB)
    CONTENT = newcommand(CONTENT, "\\xA", xA)
    CONTENT = newcommand(CONTENT, "\yA", yA)
    CONTENT = newcommand(CONTENT, "\\xB", xB)
    CONTENT = newcommand(CONTENT, "\yB", yB)


    # projection of B onto A

    numerator = xA*xB + yA*yB
    denominator = xA**2 + yA**2
    d = np.gcd(numerator, denominator)
    numerator = int(numerator/d)
    denominator = int(denominator/d)

    CONTENT = newcommand_dfrac(CONTENT, "\LAMBDA", numerator, denominator)

    # norms

    normBsq = xB**2 + yB**2
    CONTENT = newcommand(CONTENT, "\Bnormsq", normBsq)
    normPnum = (xA**2 + yA**2) * numerator**2
    normPdenom = denominator**2
    d = np.gcd(normPnum, normPdenom)
    normPnum, normPdenom = int(normPnum/d), int(normPdenom/d)
    CONTENT = newcommand_dfrac(CONTENT, "\Pnormsq", normPnum, normPdenom)
    
    normBPnum = normBsq*normPdenom - normPnum
    normBPdenom = normPdenom
    d = np.gcd(normBPnum, normBPdenom)
    normBPnum, normBPdenom = int(normBPnum/d), int(normBPdenom/d)
    CONTENT = newcommand_dfrac(CONTENT, "\BPnormsq", normBPnum, normBPdenom)

    # random root in [7,10]
    root = int(np.random.rand()*4+7)
    CONTENT = newcommand(CONTENT, "\\xmax", root)
    halfroot = int(root/2)
    CONTENT = newcommand(CONTENT, "\ALPHA", halfroot if root%2 == 0 else "\dfrac{"+str(root)+"}{2}")
    
    # values of x to draw
    CONTENT = newcommand(CONTENT, "\\xfirst", int(root/3))
    CONTENT = newcommand(CONTENT, "\\xsecond", int(2*root/3))

    # constant area (base x height /2)
    # beta is constant * alpha²/2
    
    constant = np.abs(xA*yB - yA*xB)
    d = np.gcd(constant, 2)

    CONTENT = newcommand_dfrac(CONTENT, "\prodovertwo", int(constant/d), int(2/d))

    BETA = constant*root**2
    d=np.gcd(BETA,8)

    CONTENT = newcommand_dfrac(CONTENT, "\BETA", int(BETA/d), int(8/d))

    # all commented below replaced by the 6 lines above thanks to math (:
    """
    numCsquared = (xA**2 + yA**2)*normBPnum*normBPdenom
    numC = reduced_sqrt(numCsquared)

    d = np.gcd(numC[0], 2*normBPdenom)

    C = [int(numC[0]/d), numC[1]]
    
    denumC = int(2*normBPdenom/d)

    if denumC==1:
        prodovertwo = "" if C[0] == 1 else str(C[0])
    else:
        prodovertwo = "\dfrac{"+str(C[0])+"}{"+str(denumC)+"}"

    squarerootsuffix = "" if C[1] == 1 else "\sqrt{"+str(C[1])+"}"
    ###### alors la racine disparaît toujours et il y a une raison :
    ###### on calcule en fait la racine de ||v - \lambda u||² · || u ||² = ||u||² · ||v||² - <u,v>², par Pythagore ( \lambda = <u,v>/<u,u>)
    ###### et cette différence est elle-même un carré car (x²+y²)(a²+b²) - (ax+by)² = (ay-bx)², le déterminant au carré.
    ###### je me demande s'il y a quelque chose de profond derrière ça ?


    d = np.gcd(C[0]*root**2, 8)
    numBeta = int(C[0]*root**2/d)
    denumBeta = int(8/d)
    if denumBeta==1:
        BETA = "" if numBeta==1 else str(numBeta)
    else:
        BETA = "\dfrac{"+str(numBeta)+"}{"+str(denumBeta)+"}"

    CONTENT = newcommand(CONTENT, "\prodovertwo", prodovertwo+squarerootsuffix)
    CONTENT = newcommand(CONTENT, "\BETA", BETA+squarerootsuffix)
    """
    # WRITE TO FILE

    FILE_NAME = f"adr/vars_{seed}.adr"

    with open(FILE_NAME, 'w') as file:
        file.write(CONTENT)

    # COMPILE LATEX TWICE

    INPUTS = "\input{preamble.tex} \input{"+FILE_NAME+"} \input{dm1.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"

    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    #subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    # compile twice for references 
    
    return 0

if __name__=="__main__":

    # always the same 34 to recompile if needed
    np.random.seed(1729) # taxicab number

    for _ in range(10):
        ## SEED ##

        seed = int(np.random.rand() * (2**16 - 1))
        # uncomment to fix seed
        #seed=12345

        np.random.seed(seed)
        
        generate(seed)




