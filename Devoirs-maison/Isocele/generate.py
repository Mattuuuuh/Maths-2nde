# importing DM class one folder above 
import sys
sys.path.append("..")
from DM import *

import random

###############################################
############# GENERATE FUNCTION ###############
###############################################


# OLD, LESS INTERESTING (ALL POINTS OF TYPE (A,B) (B,A), TRIVIAL PYTHAGORAS)
"""
def pythagoricien():
    # returns (p²-q², 2pq, p²+q²)
    p = int_between(3, 6)
    q = int_between(1,p-1)
    return [p**2-q**2, 2*p*q, p**2+q**2]

# ABO isoceles in O
def ABO():
    [a, b, R] = pythagoricien()
    # a² + b² = R², integers
    
    pool_of_points = zip([a,a,-a,-a,b,b,-b,-b],[b,-b,b,-b,a,-a,a,-a])
    pool_of_points = [p for p in pool_of_points]

    A, B = (0,0), (0,0)
    while A==B or (A[0]==-B[0] and A[1] == -B[1]) or A[0]==B[0] or A[1]==B[1]:
        A = random.choice(pool_of_points)
        B = random.choice(pool_of_points)

    return A, B
"""

def compose(primes, powers):
    P = 1
    for i in range(len(primes)):
        P*=primes[i]**powers[i]
    return P

def ABO():
    # return A, B st ABO is rectangle in O
    # ie needs A·B = 0
    primes = [2,3,5,7]
    powers = [int_between(1,4),int_between(1,2),int_between(0,2), int_between(0,0)]
    P = compose(primes, powers)
    
    a, b, c, d = 1,1,1,1
    xA,yA,xB,yB = 1,1,1,1
    while a==c or b==d or xA==xB or yA==yB:
    
        firstpowers = [int_between(1,powers[0]), int_between(0,powers[1]), int_between(0,powers[2]), int_between(0,powers[3])]
        a = compose(primes, firstpowers)
        c = P//a
        secondpowers = [int_between(0,powers[0]-1), int_between(0,powers[1]-1), int_between(0,powers[2]), int_between(0,powers[3])]
        b = compose(primes, secondpowers)
        d = P//b
    
        xA = a+c
        yA = d-b
        xB = b+d
        yB = c-a
        # P = a*c = b*d
        # P = ((a+c)/2 + (c-a)/2)((a+c)/2 - (c-a)/2) = ((b+d)/2 - (d-b)/2)((b+d)/2 + (d-b)/2)
        # ie. (a+c)² + (d-b)² = (b+d)² + (c-a)²

    assert xA**2 + yA**2 == xB**2 + yB**2, "not isoceles, i messed up something, God help me."

    return (xA,yA), (xB,yB)


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
    
    # shift again to center the picture
    baryx = (0+A[0]+B[0])/3
    baryy = (0+A[1]+B[1])/3

    denominator = int_between(1,14)

    xO -= int(baryx)*denominator
    yO -= int(baryy)*denominator
    
    # maybe for later? annoying right now
    # scale everything to |.| <= 50
    #scale = max(abs(A[0]), abs(A[1]), abs(B[0]), abs(B[1]))
    #scale = int(50/scale)+1

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
    ABsq = (A[0]-B[0])**2 + (A[1]-B[1])**2
    CONTENT += newcommand("ABsq", ABsq)
    CONTENT += newcommand("BCsq", B[0]**2 + B[1]**2)

    CONTENT += newcommand("AC", int(np.sqrt(A[0]**2+A[1]**2)))
    
    AB = np.sqrt(ABsq)
    ABlow = int(AB)
    if AB == int(AB):
        isSquare = 1
    else:
        isSquare = 0

    # testing
    #isSquare =1

    CONTENT += newcommand("isSquare", isSquare)
    CONTENT += newcommand("ABlow", int(np.sqrt(ABsq)))
    CONTENT += newcommand("ABhigh", int(np.sqrt(ABsq))+1)

    

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
#dm.write_adr()
#dm.compile_pdf()

# for generating seeds
#N = 80
#dm.generate_seeds(N)
#dm.write_adrs()
#dm.compile_pdfs()

# for reading adr files in case initial seed is missing or NumPy changes something
dm.read_adrs()
# for testing
#dm.seeds = [dm.seeds[0]]
#dm.N = 1
# compile
dm.compile_pdfs()


