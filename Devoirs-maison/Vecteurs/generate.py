# importing DM class one folder above 
import sys
sys.path.append("..")
from DM import *

import numpy as  np

###############################################
############# GENERATE FUNCTION ###############
###############################################

def point():
    x = int_between(-5, 5, remove=[0])
    y = int_between(-5, 5, remove=[0])
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

def are_colinear(u,v):
    return u[0]*v[1] - u[1]*v[0] == 0

# NOT SYMMETRIC
def fourier(u,v):
    assert scalar(u,u) != 0, "u is zero vector."
    return scalar(u,v)/scalar(u,u)

def generate():
    R = ""
    
    # EX 1
    u = point()

    R += newcommand("ux", u[0])
    R += newcommand("uy", u[1])

    v = (0,0)
    # but for a good drawing, fourier should additionally not be close to +1 or to 0
    #while scalar(u,v)==0 or are_colinear(u,v) or fourier(u,v) == 1:
    while are_colinear(u,v) or abs(fourier(u,v)) < .2 or abs(1-fourier(u,v)) < .2:
        v = point()
    
    R += newcommand("vx", v[0])
    R += newcommand("vy", v[1])

    projection_num = sum(mult(scalar(u,v),u), mult(-scalar(u,u),v))
    projection_denom = scalar(u,u)

    projection_denom, projection_num = reduce(projection_denom, projection_num)

    R += newcommand("projx", projection_num[0])
    R += newcommand("projy", projection_num[1])
    R += newcommand_mult("projmult", 1, projection_denom)

    Ox = -(u[0]+v[0])
    Oy = -(u[1]+v[1])

    R += newcommand_frac("Ox", Ox, 3)
    R += newcommand_frac("Oy", Oy, 3)

    xvalues = [Ox/3 + el for el in [0, u[0], v[0],v[0]+projection_num[0]/projection_denom]]
    yvalues = [Oy/3 + el for el in [0, u[1], v[1],v[1]+projection_num[1]/projection_denom]]
    
    # this is good
    # but non orthonormal grid distorts angles
    # so right-angled triangle won't appear so
    #R += newcommand("xmin", min(xvalues)-1)
    #R += newcommand("xmax", max(xvalues)+1)
    #R += newcommand("ymin", min(yvalues)-1)
    #R += newcommand("ymax", max(yvalues)+1)

    #R += newcommand("xpt", 200/(max(xvalues)-min(xvalues)))
    #R += newcommand("ypt", 100/(max(yvalues)-min(yvalues)))

    # ah oui Malak a raison ; il faut ajouter un pourcentage, pas une valeur fixe.
    # mettons 10%
    xymin = min(min(xvalues),min(yvalues))*1.1
    xymax = max(max(xvalues),max(yvalues))*1.1
    R += newcommand("xymin", xymin)
    R += newcommand("xymax", xymax)
    assert xymax != xymin, "All points are regrouped into 1 somehow (should not be possible)."
    R += newcommand("xypt", 150/(xymax-xymin))

    # SOL 1
    # points
    R += newcommand_frac("xA", Ox, 3)
    R += newcommand_frac("yA", Oy, 3)
    R += newcommand("xAreal", Ox/3)
    R += newcommand("yAreal", Oy/3)
    
    R += newcommand_frac("xB", Ox+u[0]*3, 3)
    R += newcommand_frac("yB", Oy+u[1]*3, 3)
    R += newcommand("xBreal", Ox/3+u[0])
    R += newcommand("yBreal", Oy/3+u[1])

    R += newcommand_frac("xC", Ox+v[0]*3, 3)
    R += newcommand_frac("yC", Oy+v[1]*3, 3)
    R += newcommand("xCreal", Ox/3+v[0])
    R += newcommand("yCreal", Oy/3+v[1])
    
    R += newcommand_frac("xD", (Ox+v[0]*3)*projection_denom+projection_num[0]*3, 3*projection_denom)
    R += newcommand_frac("yD", (Oy+v[1]*3)*projection_denom+projection_num[1]*3, 3*projection_denom)
    R += newcommand("xDreal", Ox/3+v[0]+projection_num[0]/projection_denom)
    R += newcommand("yDreal", Oy/3+v[1]+projection_num[1]/projection_denom)

    # w = v + proj
    w_num = (projection_num[0]+projection_denom*v[0], projection_num[1] + projection_denom*v[1])
    w_denom, w_num = reduce(projection_denom, w_num)
    R += newcommand_frac("wx", w_num[0])
    R += newcommand_frac("wy", w_num[1])
    R += newcommand_mult("wmult", 1, w_denom)

    # fourier coeff
    R += newcommand_frac("fourier", scalar(u,v), scalar(u,u))

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
#dm.write_adr(1217)
#dm.compile_pdf(1217)

# for generating seeds
#dm.generate_seeds(80)
#dm.write_adrs()
#dm.compile_pdfs()

# for reading adr files in case initial seed is missing or NumPy changes something
dm.read_adrs()
# compile
dm.compile_pdfs()
