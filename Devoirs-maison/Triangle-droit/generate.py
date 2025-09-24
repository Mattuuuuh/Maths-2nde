# importing DM class one folder above 
import sys
sys.path.append("..")
from DM import *

import random

###############################################
############# GENERATE FUNCTION ###############
###############################################

def compose(primes, powers):
    P = 1
    for i in range(len(primes)):
        P*=primes[i]**powers[i]
    return P

def ABO():
    # return A, B st ABO is rectangle in O
    # ie needs A·B = 0
    primes = [2,3,5,7]
    powers = [int_between(2,4),int_between(1,2),int_between(0,2), int_between(0,1)]
    P = compose(primes, powers)

    firstpowers = [int_between(2,powers[0]-1), int_between(1,powers[1]-1), int_between(0,powers[2]), int_between(0,powers[3])]
    a = compose(primes, firstpowers)
    c = P//a
    secondpowers = [int_between(1,powers[0]-2), int_between(0,powers[1]-1), int_between(0,powers[2]), int_between(0,powers[3])]
    b = compose(primes, secondpowers)
    d = P//b

    signa = -1 if np.random.rand()<.5 else 1
    signb = -1 if np.random.rand()<.5 else 1
    signc = -1 if np.random.rand()<.5 else 1
    signd = -signa*signb*signc

    return (signa*a,signb*b), (signc*c,signd*d)

def generate():

    CONTENT = ""

    # EX 1
    
    # points A, B, O
    O = (0,0)
    A, B = ABO()

    # shift everything now
    xO, yO = 0,0
    while xO==0 or yO==0:
        xO = int_between(-33, 33)
        yO = int_between(-33, 33)
    
    denominator = int_between(1,12)

    CONTENT += newcommand_dfrac("xC", xO, denominator)
    CONTENT += newcommand_dfrac("yC", yO, denominator)
    
    CONTENT += newcommand_dfrac("xA", xO+A[0]*denominator, denominator)
    CONTENT += newcommand_dfrac("yA", yO+A[1]*denominator, denominator)

    CONTENT += newcommand_dfrac("xB", xO+B[0]*denominator, denominator)
    CONTENT += newcommand_dfrac("yB", yO+B[1]*denominator, denominator)

    # SOLUTIONS

    realxA = xO/denominator + A[0]
    realyA = yO/denominator + A[1]
    realxB = xO/denominator + B[0]
    realyB = yO/denominator + B[1]
    realxC = xO/denominator 
    realyC = yO/denominator 

    xmin = min(A[0], B[0],0) + xO/denominator - 1
    ymin = min(A[1], B[1],0) + yO/denominator - 1
    xmax = max(A[0], B[0],0) + xO/denominator + 1
    ymax = max(A[1], B[1],0) + yO/denominator + 1

    for var in ["realxC", "realyC", "realxA", "realxB", "realyA", "realyB", "xmin", "xmax", "ymin", "ymax"]:
        CONTENT += newcommand(var, np.round(eval(var),3))

    CONTENT += newcommand("ACx", A[0])
    CONTENT += newcommand("ACy", A[1])
    CONTENT += newcommand("BCx", B[0])
    CONTENT += newcommand("BCy", B[1])
    CONTENT += newcommand("ABx", B[0]-A[0])
    CONTENT += newcommand("ABy", B[1]-A[1])
    
    CONTENT += newcommand("ACsq", A[0]**2 + A[1]**2)
    CONTENT += newcommand("ABsq", (A[0]-B[0])**2 + (A[1]-B[1])**2)
    CONTENT += newcommand("BCsq", B[0]**2 + B[1]**2)


    return CONTENT

###############################################
############## USING DM LIBRARY ###############
###############################################

dm = DM(
        FOLDER="Isocele/",
        generating_function=generate,
        double_compile=True,
        initial_seed=0,
        a5=True,
    )

# for testing (seed 0)
dm.write_adr()
dm.compile_pdf()

# for generating seeds
#N = 70
#dm.generate_seeds(N)
#dm.write_adrs()
#dm.compile_pdfs()

# for reading adr files in case initial seed is missing or NumPy changes something
# TODO



