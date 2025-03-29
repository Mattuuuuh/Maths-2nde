import subprocess
import numpy as  np


###############################################
############# UTILITY FUNCTIONS ###############
###############################################

# generic \newcommand
# inputs : command (string), value (string or castable to string)
def newcommand(command, value):
    # idk append this list when encountering commands
    if command in ["\\a", "\\angle"]:
        return renewcommand(command, value)
    return "\\newcommand{"+command+"}{"+str(value)+"}\n"

# generic \renewcommand
def renewcommand(command, value):
    return "\\renewcommand{"+command+"}{"+str(value)+"}\n"

# generic \newcommand with dfrac
def newcommand_dfrac(command, numerator, denominator):
    # turn things integer
    numerator, denominator = int(numerator), int(denominator)
    # make coprime
    gcd = np.gcd(numerator, denominator)
    assert gcd != 0, "null GCD?"
    numerator //= gcd
    denominator //= gcd
    # sign is always on top
    if denominator < 0:
        numerator *= -1
        denominator *= -1

    # integer case
    if denominator == 1:
        return newcommand(command, numerator)
    
    # else
    return newcommand(command, "\dfrac{"+str(numerator)+"}{"+str(denominator)+"}")

def newcommand_mult(command, numerator, denominator):
    """
    Fonction qui crée un commande \dfrac{numerator}{denominator} irréductible.
    La constante numerator/denominator est supposée multiplicative :
        - si elle est 1, elle n'affiche rien
        - le signe positif n'est pas affiché
        - le signe négatif est uniquement au numérateur le cas échéant
    
    INPUTS : numerator, denominator (signed ints)
    """

    # make coprime
    gcd = np.gcd(numerator, denominator)
    assert gcd != 0, "null GCD?"
    numerator //= gcd
    denominator //= gcd
    # sign is always on top
    if denominator < 0:
        numerator *= -1
        denominator *= -1

    # case val = 1
    if (denominator == 1) and (numerator == 1):
        return newcommand(command, "")
    
    # case val is integer
    if denominator == 1:
        return newcommand(command, numerator)

    # else
    return newcommand(command, "\dfrac{"+str(numerator)+"}{"+str(denominator)+"}")

def newcommand_add(command, numerator, denominator):
    """
    Fonction qui crée un commande \dfrac{numerator}{denominator} irréductible.
    La constante numerator/denominator est supposée additive :
        - si elle est 0, elle n'affiche rien
        - le signe positif est affiché
        - le signe négatif est devant la fraction le cas échéant
    
    INPUTS : numerator, denominator (signed ints)
    """

    # make coprime
    gcd = np.gcd(numerator, denominator)
    assert gcd != 0, "null GCD?"
    numerator //= gcd
    denominator //= gcd
    # sign is always on top
    if denominator < 0:
        numerator *= -1
        denominator *= -1

    # case val = 0
    if numerator == 0:
        return newcommand(command, "")
    
    # else
    # sign is separated
    sign = "+" if numerator>=0 else "-"
    numerator = np.abs(numerator)
    
    # case val is integer
    if denominator == 1:
        return newcommand(command, sign+str(numerator))
    
    return newcommand(command, sign+"\dfrac{"+str(numerator)+"}{"+str(denominator)+"}")

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

    INPUTS = "\input{preamble.tex} \input{"+FILE_NAME+"} \input{dm2.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"
    # suppress output
    PARAMETER3 = "-interaction=batchmode"

    print(f"COMPILING SEED {seed}")
    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, PARAMATER3, INPUTS])
    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, PARAMETER3, INPUTS])
    # compile twice if references are required
    
    return 0

###############################################
############# GENERATE FUNCTION ###############
###############################################

def generate(seed):
    """
    Generate a, b, beta integers such that 
        3 <= a <= 11,
        |b| <= 6,
        b!=0,
        b >= 10,
        beta is squarefree (don't want to deal with simplifying sqrts).

    h(x) = -beta + (ax+b)²
    
    Call D = sqrt(beta) the discriminant.
    
    g(x) = (ax + b + D)(ax + b - D)

    f(x) = a²x² + 2abx + b² - beta
    """

    CONTENT = newcommand("\seed", seed)

    ### EX 1 ###

    # h(x)

    a = np.random.rand()*9+3
    a = int(a)

    b = np.random.rand()*6+1
    b = int(b)
    sign = 1 if np.random.rand() > .5 else -1
    b *= sign

    squarefreeints = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17]
    # taken from sequence A005117 for oeis.
    # sample uniformly from squarefreeints
    N = len(squarefreeints)
    index = np.random.rand()*N
    index=int(index)
    assert 0 <= index < N, "Index outside of squarefreeints bounds."
    beta = squarefreeints[index]

    CONTENT += newcommand("\\hbeta", beta)
    CONTENT += newcommand("\\ha", a)
    CONTENT += newcommand_add("\\hb", b, 1)

    # g(x)

    CONTENT += newcommand("\\gaI", a)
    CONTENT += newcommand("\\gaII", a)

    if sign==1:
        CONTENT += newcommand("\\gbI", f"+{b} + \\sqrt{{{beta}}}")
        CONTENT += newcommand("\\gbII", f"+{b} - \\sqrt{{{beta}}}")
    else:
        CONTENT += newcommand("\\gbI", f"{b} + \\sqrt{{{beta}}}")
        CONTENT += newcommand("\\gbII", f"{b} - \\sqrt{{{beta}}}")
            

    # f(x)

    CONTENT += newcommand("\\fa", a**2)
    CONTENT += newcommand_add("\\fb", 2*a*b, 1)
    CONTENT += newcommand_add("\\fc", b**2 - beta, 1)

    ### EX 3 ###

    """
    Generate a, b, c, d integers such that
        20 > a,b,c,d > 2
        b/a != c/d, ie. ac-bd != 0
        
    f(x) = (ax² - b)(c - dx²)
        = -adx⁴ + (ac + bd)x² - bc
    """

    a, b, c, d = (np.random.rand(4)*17+3).astype(int)
    btimesd = b*d
    while a*c - btimesd == 0:
        c, d = (np.random.rand(2)*17+3).astype(int)

    for letter in ["a", "b", "c", "d"]:
        CONTENT += newcommand(f"\\{letter}V", eval(letter))

    CONTENT += newcommand("\\eqIa", -a*d)
    CONTENT += newcommand("\\eqIb", a*c+b*d)
    CONTENT += newcommand("\\eqIc", -b*c)

    ### EX 4 ###
    """
    Generate rationnals a/b, c/d such that
        b·d != 0
        a/b·c/d < 0
        0 < |a,b,c,d| < 20
    """

    a, b, c, d = (np.random.rand(4)*19+1).astype(int)
    
    sign = 1 if np.random.rand() > .5 else -1
    a *= sign
    c *= -sign

    CONTENT += newcommand_dfrac("\\qI", a, b)
    CONTENT += newcommand_dfrac("\\qII", c, d)


    return CONTENT    


### main ###

if __name__=="__main__":

    N = 40
    # always the same N to recompile if needed
    np.random.seed(125) # not a square 

    for _ in range(N):
        ## SEED ##
        seed = int(np.random.rand() * (2**16 - 1))

        # uncomment to fix seed
        #seed=34414

        np.random.seed(seed)
        
        CONTENT = generate(seed)
        write(CONTENT, seed)
        pdflatex(seed)




