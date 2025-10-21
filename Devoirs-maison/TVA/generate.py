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

    TVA = int(np.random.rand()*40 +5)
    R += newcommand("TVA", TVA)
    P = int_between(50, 650)
    Pfixe = int(np.random.rand()*P/2 + 20)

    R += newcommand("PFIXE", Pfixe)

    [A,B] = np.random.rand(2)*1900+100
    A, B = int(A), int(B)

    R += newcommand("A", A)
    R += newcommand("B", B)

    # EX 2

    [remise, aug] = np.random.rand(2)*[100, 300] + 5
    remise, aug = int(remise), int(aug)
    dim = int(np.random.rand()*remise/2 + 2)

    R += newcommand("REMISE", remise)
    R += newcommand("FINALaug", aug)
    R += newcommand("FINALdim", dim)

    # EX 1 SOLUTION

    Asol = np.round((1+TVA/100)*A,2)
    R += newcommand("Asol", comma(Asol))
    Bsol = np.round(B/(1+TVA/100),2)
    R += newcommand("Bsol", comma(Bsol))

    gcd = np.gcd(TVA, 100+TVA)
    rationum = int(TVA/gcd)
    ratiodenom = int((100+TVA)/gcd)
    
    R += newcommand("rationum", rationum)
    R += newcommand("ratiodenom", ratiodenom)

    # EX 2 SOLUTION

    reciproque = np.round(1/(1-remise/100),2)
    R += newcommand("reciproque", comma(reciproque))
    recsol = int(100*(reciproque-1))
    R += newcommand("recsol", recsol)

    evoldeux = np.round((1+aug/100)/(1-remise/100),2)
    R += newcommand("evoldeux", comma(evoldeux))
    FINALaugsol = int(100*(evoldeux-1))
    R += newcommand("FINALaugsol", FINALaugsol)
    
    evoltrois = np.round((1-dim/100)/(1-remise/100),2)
    R += newcommand("evoltrois", comma(evoltrois))
    FINALdimsol = int(100*(evoltrois-1))
    R += newcommand("FINALdimsol", FINALdimsol)

    return R

###############################################
############## USING DM LIBRARY ###############
###############################################

dm = DM(
        FOLDER="TVA/",
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
# TODO




