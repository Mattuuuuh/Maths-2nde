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

    # canonique

    # f(x) = hbeta + hA (ha x + hb)² 
    # = (hA·ha²) x² + (2·hA·ha·hb) x + (hbeta + hA·hb²)
    # = fa x² + fb x + fc
    
    hA = int_between(-5, 5, remove=[0,1,-1])

    hbeta = 20*int_between(1,4, remove=[0]) + int_between(5,15)
    if hA > 0:
        hbeta*=-1

    ha = int_between(1, 9)

    hb = int_between(-10, 10, remove=[0])

    R += newcommand("hbeta", hbeta)
    R += newcommand_mult("hA", hA, sign=True)
    R += newcommand_mult("ha", ha)
    R += newcommand_add("hb", hb)
   
    # dev red
    fa = hA*ha**2
    fb = 2*hA*ha*hb
    fc = hbeta+hA*hb**2
    R += newcommand_mult("fa", fa)
    R += newcommand_mult("fb", fb, sign=True)
    R += newcommand_add("fc", fc)
    
    R += newcommand("faR", fa)
    R += newcommand("fbR", fb)
    R += newcommand("fcR", fc)
    
    # graph
    
    f = lambda x: fa*x**2+fb*x+fc
    xstar = -hb/ha
    xmin = int(xstar)-3
    xmax = int(xstar)+3
    R+= newcommand("xstar", xstar)
    R+= newcommand_frac("xstarfrac", -hb, ha)
    R+= newcommand("xmin", xmin)
    R+=newcommand("xmax", xmax)

    images = {f(xstar), f(xmin), f(xmax)}
    R+= newcommand("ymin", min(images)-10)
    R+= newcommand("ymax", max(images)+10)

    # SOL 1
    R+= newcommand("ishApositive", int(hA>0))

    return R

###############################################
############## USING DM LIBRARY ###############
###############################################

dm = DM(
        FOLDER="Canonique/",
        generating_function=generate,
        double_compile=True,
        initial_seed=0,
        a5=True,
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
# compile
#dm.compile_pdfs()




