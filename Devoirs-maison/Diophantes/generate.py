# importing DM class one folder above 
import sys
sys.path.append("..")
from DM import *

import numpy as  np

###############################################
############# GENERATE FUNCTION ###############
###############################################

def randomize():

    p, b0 = 2,2
    while np.gcd(p, b0) != 1:
        p = int_between(2, 25)
        b0 = int_between(6,12)

    print(p,b0)

    a0 = 1
    while (p*a0+1) % b0 != 0:
        a0+=1
    
    q = (p*a0+1)//b0

    print(q,a0)

    Xbar = int_between(-30,30)

    c = int_between(2,3)

    scale = c*int_between(2,3)
    scale *= 1 if np.random.rand()<.5 else -1
    
    A = Xbar - scale*p
    B = Xbar + scale*q
    C = Xbar - scale//c

    return [p,q,a0,b0, Xbar, c, scale, A, B, C]

def generate():

    CONTENT = ""

    # EX 1

    [p,q,a0,b0, Xbar, c, scale, A, B, C] = randomize()

    CONTENT += newcommand("p", p)
    CONTENT += newcommand("q", q)
    CONTENT += newcommand("Xbar", Xbar)
    CONTENT += newcommand("cI", c)
    CONTENT += renewcommand("A", A)
    CONTENT += newcommand_mult("B", B, sign=True)
    CONTENT += renewcommand("C", C)

    CONTENT += newcommand("sola", a0+q)
    CONTENT += newcommand("solb", b0+p)

    # SOL 1

    CONTENT += newcommand("azero", a0)
    CONTENT += newcommand("bzero", b0)
    
    CONTENT += newcommand("atwo", a0+2*q)
    CONTENT += newcommand("btwo", b0+2*p)
    CONTENT += newcommand("athree", a0+3*q)
    CONTENT += newcommand("bthree", b0+3*p)
    
    return CONTENT

###############################################
############## USING DM LIBRARY ###############
###############################################

dm = DM(
        FOLDER="Diophantes/",
        generating_function=generate,
        double_compile=True,
        initial_seed=0,
    )

# for testing (seed 0)
dm.write_adr()
dm.compile_pdf()

# for generating seeds
#dm.generate_seeds(4)
#dm.write_adrs()
#dm.compile_pdfs()

# for reading adr files in case initial seed is missing or NumPy changes something
#dm.read_adrs()
# for testing
#dm.seeds = [dm.seeds[0]]
#dm.N = 1
# rewrite 
#dm.write_adrs()
# compile
#dm.compile_pdfs()

