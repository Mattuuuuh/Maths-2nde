import subprocess
import numpy as  np

class DM:

    def __init__(self, FOLDER="00-DM-Template/", generating_function=lambda:"\\newcommand{HW}{Hello World!}", double_compile = True, initial_seed = 0):
        self.N=1
        self.seeds=[0]
        self.FOLDER=FOLDER
        self.generating_function=generating_function
        
        self.initial_seed=initial_seed
        np.random.seed(initial_seed)
        
        self.double_compile = double_compile
    
    ###############################################
    ############## UTILITY FUNCTIONS ##############
    ###############################################

    # generates N seeds, i=0, ..., N-1...
    # the last three decimal places are i itself...
    # if i=5, last three digits are 005, for example.
    # ! seed list is entirely determined by initial_seed !
    def generate_seeds(self, N):
        self.N = N
        seeds = []
        
        assert N!=0, "N must be a positive integer."
        scale = 10**int(np.log10(N)+1)

        for i in range(N):
            seed = np.random.rand()*(10**2-1)
            seed = int(seed)+1
            seed*=scale
            seed+=i
            seeds+=[seed]

        self.seeds = seeds 
        return 0

    # write to file FOLDER/adr/{seed}.adr from seed and generate function
    # generate function should return a string with commands readable by latex
    # default seed 0 is for testing
    def write_adr(self, seed=0):
        FILE_NAME = f"adr/{seed}.adr"
        CONTENT = newcommand("seed", seed)
        
        np.random.seed(seed)
        
        CONTENT += self.generating_function()

        with open(FILE_NAME, 'w') as file:
            file.write(CONTENT)
        return 0

    # seeds is a list of seeds to write
    def write_adrs(self, seeds=None):
        if seeds is None:
            seeds=self.seeds
        for seed in seeds:
            self.write_adr(seed)
        return 0

    # reads seeds from adr files inside FOLDER/adr/
    def read_adrs(self):
        # TODO
        self.N = 0
        self.seeds = []
        return 0

    def compile_pdf(self, seed=0):
        # COMPILE WITH VARS INPUT
        FILE_NAME = f"adr/{seed}.adr"

        INPUTS = (
            "\input{../preamble.tex} \input{"+
            FILE_NAME+
            "} \input{main.tex}"
            )
        PARAMETER1 = f"-output-directory=out"
        PARAMETER2 = f"-jobname=seed_{seed}"
        # suppress output
        PARAMETER3 = "-interaction=batchmode"
        
        print(f"COMPILING SEED {seed}")
        subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, PARAMETER3, INPUTS])
        # compile twice if references are required
        if self.double_compile:
            subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, PARAMETER3, INPUTS])
        
        return 0

    # seeds is a list of seeds to compile
    def compile_pdfs(self, seeds=None):
        if seeds is None:
            seeds=self.seeds
        for seed in seeds:
            self.compile_pdf(seed)
        return 0

###############################################
########### NEWCOMMAND FUNCTIONS ##############
###############################################

# generic \newcommand
# inputs : command (string), value (string or castable to string)
def newcommand(command, value):
    # idk append this list when encountering commands
    if command in ["a", "angle"]:
        return renewcommand(command, value)
    return "\\newcommand{\\"+command+"}{"+str(value)+"}\n"

# generic \renewcommand
def renewcommand(command, value):
    return "\\renewcommand{\\"+command+"}{"+str(value)+"}\n"

# generic \newcommand with dfrac
def newcommand_dfrac(command, numerator, denominator=1):
    # turn things integer
    numerator, denominator = int(numerator), int(denominator)

    # zero case
    if numerator == 0:
        return newcommand(command, 0)

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

def newcommand_mult(command, numerator, denominator=1, sign=False):
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
        return newcommand(command, "+" if sign else "")
    
    # case val = -1
    if (denominator == 1) and (numerator == -1):
        return newcommand(command, "-")
    
    # case val is integer
    if denominator == 1:
        return newcommand(command, ("+" if sign and numerator>0 else "") + str(numerator))

    # else
    if sign:
        return newcommand(command, ("+" if numerator>0 else "-") + "\dfrac{"+str(np.abs(numerator))+"}{"+str(denominator)+"}")

    return newcommand(command, "\dfrac{"+str(numerator)+"}{"+str(denominator)+"}")
def newcommand_add(command, numerator, denominator=1):
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

# gives an int n verifying a <= n <= b.
# uniform random.
def int_between(a,b):
    assert a <= b, "a,b must verify a <= b."
    n = np.random.rand()
    n *= (b-a+1)
    n = int(n)
    n += a

    return n




