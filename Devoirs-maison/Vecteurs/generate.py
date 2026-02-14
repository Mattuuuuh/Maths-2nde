# importing DM class one folder above 
import sys
sys.path.append("..")
from DM import *

import numpy as  np

###############################################
############# GENERATE FUNCTION ###############
###############################################

def point():
    x = int_between(-5, 5)
    y = int_between(-5, 5)
    return (x,y)

def scalar(u,v):
    return u[0]*v[0]+u[1]*v[1]

def mult(k, u):
    return (u[0]*k, u[1]*k)

def sum(u,v):
    return (u[0]+v[0], u[1] + v[1])

def reduce(denominator, v):
    d = np.gcd(denominator, v[0])
    d = np.gcd(d, v[1])
    denominator//=d
    v = (v[0]//d, v[1]//d)
    return denominator, v

def generate():
    R = ""
    
    # EX 1
    u = point()

    R += newcommand("ux", u[0])
    R += newcommand("uy", u[1])

    v = (0,0)
    while scalar(u,v)==0:
        v = point()
    
    R += newcommand("vx", v[0])
    R += newcommand("vy", v[1])

    projection_num = sum(mult(scalar(u,v),u), mult(-scalar(u,u),v))
    projection_denom = scalar(u,u)

    projection_denom, projection_num = reduce(projection_denom, projection_num)

    R += newcommand("projx", projection_num[0])
    R += newcommand("projy", projection_num[1])
    R += newcommand_mult("projmult", 1, projection_denom)

    Ox = -(u[0]+v[0])/2
    Oy = -(u[1]+v[1])/2
    Ox = int(Ox)
    Oy = int(Oy)

    R += newcommand("Ox", Ox)
    R += newcommand("Oy", Oy)

    return R

###############################################
############## USING DM LIBRARY ###############
###############################################

dm = DM(
        FOLDER="Vecteurs/",
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




