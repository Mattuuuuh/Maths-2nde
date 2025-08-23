# importing DM class one folder above 
import sys
sys.path.append("..")
from DM import *

import numpy as  np

###############################################
############# GENERATE FUNCTION ###############
###############################################

def generate():
    R = ""

    # EX 1

    # 20 different choices
    x1 = int_between(1,20)
    x2 = x1+1
    x3 = x2+1
    
    a = lambda x: (x-x2)*(x-x3)
    b = lambda x: (x-x1)*(x-x3)
    c = lambda x: (x-x1)*(x-x2)

    q1 = a(x1)
    q2 = b(x2)
    q3 = c(x3)
    
    R += newcommand("xI", x1)
    R += newcommand("xII", x2)
    R += newcommand("xIII", x3)

    R += newcommand_mult("qI", 1, q1)
    R += newcommand_mult("qII", 1, q2)
    R += newcommand_mult("qIII", 1, q3)
    
    # EX 2
    
    # 11 different choices
    b = int_between(2, 9)
    # 2 different choices
    sign = 1 if np.random.rand()<.5 else -1
    b *= sign

    f = lambda x: x+b

    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)

    R += newcommand_mult("fI", f1) 
    R += newcommand_mult("fII", f2) 
    R += newcommand_mult("fIII", f3) 

    # EX 3

    R += newcommand_add("bI", b)

    # 20*11*2 = 440 different choices.
    return R

###############################################
############## USING DM LIBRARY ###############
###############################################

dm = DM(
        FOLDER="Fonctions1/",
        generating_function=generate,
        double_compile=True,
        initial_seed=0,
    )

# for testing (seed 0)
#dm.write_adr()
#dm.compile_pdf()

# for generating seeds
dm.generate_seeds(4)
dm.write_adrs()
dm.compile_pdfs()

# for reading adr files in case initial seed is missing or NumPy changes something
# TODO




