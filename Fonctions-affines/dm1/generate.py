import subprocess
import numpy as  np


###############################################
############# UTILITY FUNCTIONS ###############
###############################################

# generic \newcommand
# inputs : command (string), value (string or castable to string)
def newcommand(command, value):
    # idk append this list when encountering commands
    if command in ["\\a"]:
        return renewcommand(CONTENT, command, value)
    return "\\newcommand{"+command+"}{"+str(value)+"}\n"

# generic \renewcommand
def renewcommand(command, value):
    return "\\renewcommand{"+command+"}{"+str(value)+"}\n"

# generic \newcommand with dfrac
def newcommand_dfrac(command, numerator, denominator):
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
    
    # case val is integer
    if denominator == 1:
        return newcommand(command, numerator)

    # else
    # sign is separated
    sign = "+" if numerator>=0 else "-"
    numerator = np.abs(numerator)
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

    INPUTS = "\input{preamble.tex} \input{"+FILE_NAME+"} \input{dm1.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"

    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    #subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    # compile twice if references are required
    
    return 0

###############################################
############# GENERATE FUNCTION ###############
###############################################


def generate(seed):
    CONTENT = newcommand("\seed", seed)

    # generate random integer ax + b = cx + d to solve, with a != c.
    [a,b,c,d] = (np.random.rand(4)*12 - 6).astype(int)
    while a == c:
        [a,b,c,d] = (np.random.rand(4)*12 - 6).astype(int)
   
    for s in ["a", "c"]:
        CONTENT += newcommand_mult(f"\\{s}I", eval(s), 1)
    for s in ["b", "d"]:
        CONTENT += newcommand_add(f"\\{s}I", eval(s), 1)

    CONTENT += newcommand_dfrac(f"\\solI", d-b, a-c)

    return CONTENT    

    return 0


### main ###

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




