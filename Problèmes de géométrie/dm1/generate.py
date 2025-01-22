import subprocess
import numpy as  np

def newcommand(current_str, command, value):
    if command in ["\d", "\k", "\Q", "\P"]:
        prefix = "\\renewcommand"
    else:
        prefix = "\\newcommand"
    return current_str+prefix+"{"+command+"}{"+str(value)+"}\n"

def newcommand_dfrac(current_str, command, numerator, denominator):
    d = np.gcd(numerator, denominator)
    numerator = int(numerator/d)
    denominator = int(denominator/d)
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

    CONTENT = newcommand_dfrac(CONTENT, "\LAMBDA", numerator, denominator)

    # norms

    normBsq = xB**2 + yB**2
    CONTENT = newcommand(CONTENT, "\Bnormsq", normBsq)
    normPnum = (xA**2 + yA**2) * numerator**2
    normPdenom = denominator**2
    CONTENT = newcommand_dfrac(CONTENT, "\Pnormsq", normPnum, normPdenom)
    
    normBPnum = normBsq*normPdenom - normPnum
    normBPdenom = normPdenom
    CONTENT = newcommand_dfrac(CONTENT, "\BPnormsq", normBPnum, normBPdenom)

    # random root in [7,10]
    root = int(np.random.rand()*4+7)
    CONTENT = newcommand(CONTENT, "\\xmax", root)
    halfroot = int(root/2)
    CONTENT = newcommand(CONTENT, "\ALPHA", halfroot if root%2 == 0 else "\dfrac{"+str(root)+"}{2}")
    
    # values of x to draw
    xfirst = np.rint(root/3).astype(int)
    xsecond = np.rint(2*root/3).astype(int)
    CONTENT = newcommand(CONTENT, "\\xfirst", xfirst)
    CONTENT = newcommand(CONTENT, "\\xsecond", xsecond)

    # constant area (base x height /2)
    # beta is constant * alpha²/2
    
    constant = np.abs(xA*yB - yA*xB)
    d = np.gcd(constant, 2)

    CONTENT = newcommand_dfrac(CONTENT, "\prodovertwo", int(constant/d), int(2/d))

    BETA = constant*root**2
    d=np.gcd(BETA,8)

    CONTENT = newcommand_dfrac(CONTENT, "\BETA", int(BETA/d), int(8/d))

    ###### SOLUTIONS ######

    # QUESTION 1

    A = np.array([xA, yA])
    B = np.array([xB, yB])
    xAfirst, yAfirst = xfirst * A
    xAsecond, yAsecond = xsecond * A
    xBfirst, yBfirst = (root-xfirst)*B
    xBsecond, yBsecond = (root-xsecond)*B
    xPfirst, yPfirst = (root - xfirst) * A
    xPsecond, yPsecond = (root - xsecond) * A
    
    xcoords = [2, -2]
    ycoords = [2, -2]
    for point in ["A", "B", "P"]:
        for suffix in ["first", "second"]:
            xcoords+=[eval(f"x{point}{suffix}")]
    for point in ["A", "B", "P"]:
        for suffix in ["first", "second"]:
            ycoords+=[eval(f"y{point}{suffix}")]

    # marche pas pour une raison inconnue. scope ?
    #xcoords = [eval(f"x{point}{suffix}") for point in ["A", "B", "P"] for suffix in ["first", "second"]]
    #ycoords = [eval(f"y{point}{suffix}") for point in ["A", "B", "P"] for suffix in ["first", "second"]]

    for coord in ["x", "y"]:
        CONTENT = newcommand(CONTENT, f"\\{coord}low", min(eval(f"{coord}coords"))-1)
        print(f"{coord}low", min(eval(f"{coord}coords"))-1)
        print(max(eval(f"{coord}coords"))+1)
        CONTENT = newcommand(CONTENT, f"\\{coord}high", max(eval(f"{coord}coords"))+1)

    for suffix in ["first", "second"]:
        for coord in ["x", "y"]:
            CONTENT = newcommand(CONTENT, f"\\{coord}A{suffix}", eval(f"{coord}A{suffix}"))
            CONTENT = newcommand(CONTENT, f"\\{coord}B{suffix}", eval(f"{coord}B{suffix}"))
            CONTENT = newcommand(CONTENT, f"\\{coord}P{suffix}", eval(f"{coord}P{suffix}")*numerator/denominator)

    # QUESTION 6

    CONTENT = newcommand(CONTENT, "\\Anormsq", int(xA**2 + yA**2))

    # QUESTION 7

    CONTENT = newcommand(CONTENT, "\\BETAval", BETA/8)
    CONTENT = newcommand(CONTENT, "\\prodovertwoval", constant/2)


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

    # always the same 40 to recompile if needed
    np.random.seed(1729) # taxicab number

    for _ in range(40):
        ## SEED ##

        seed = int(np.random.rand() * (2**16 - 1))
        # uncomment to fix seed
        #seed=12345

        np.random.seed(seed)
        
        generate(seed)




