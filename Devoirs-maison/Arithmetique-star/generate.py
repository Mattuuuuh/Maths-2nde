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

    # a<b coprime not unit
    a = int_between(2,15)
    b = int_between(a+1,a+15)
    d = np.gcd(a,b)
    while d==a:
        a = int_between(2,15)
        b = int_between(2,15)
        d = np.gcd(a,b)

    a //= d
    b //= d

    R += newcommand("aI", a)
    R += newcommand("bI", b)
    R += newcommand("abI", a*b)

    # SOL 1
    
    # finding au + bv = 1
    v = 1
    while (1-b*v)%a != 0:
        v+=1
    u = (1-b*v)//a

    R += newcommand("uI", u)
    R += newcommand("vI", v)

    # EX 2

    # SOL 2

    return R

###############################################
############## USING DM LIBRARY ###############
###############################################

dm = DM(
        FOLDER="Arithmetique-star/",
        generating_function=generate,
        double_compile=True,
        initial_seed=666,
        a5=True,
    )

# for testing (seed 0)
dm.write_adr()
dm.compile_pdf()

# for generating seeds
#dm.generate_seeds(80)
#dm.write_adrs()
#dm.compile_pdfs()

# for reading adr files in case initial seed is missing or NumPy changes something
#dm.read_adrs()
# compile
#dm.compile_pdfs()




