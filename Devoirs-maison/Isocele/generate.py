# importing DM class one folder above 
import sys
sys.path.append("..")
from DM import *

import random

###############################################
############# GENERATE FUNCTION ###############
###############################################

def pythagoricien():
    # returns (p²-q², 2pq, p²+q²)
    p = int_between(3, 6)
    q = int_between(1,p-1)
    return [p**2-q**2, 2*p*q, p**2+q**2]

def generate():

    CONTENT = ""

    # EX 1

    [a, b, R] = pythagoricien()
    # a² + b² = R², integers
    
    # points A, B, O
    O = (0,0)
    pool_of_points = zip([a,a,-a,-a,b,b,-b,-b],[b,-b,b,-b,a,-a,a,-a])
    pool_of_points = [p for p in pool_of_points]

    num_points = 8
    A, B = (0,0), (0,0)
    while A==B or (A[0]==-B[0] and A[1] == -B[1]):
        A = random.choice(pool_of_points)
        B = random.choice(pool_of_points)
    
    # shift everything now
    xO, yO = 0,0
    while xO==0 and yO==0:
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

    dx = a
    dy = b

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



