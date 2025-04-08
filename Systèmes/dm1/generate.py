import subprocess
import numpy as  np


###############################################
############# UTILITY FUNCTIONS ###############
###############################################

# generic \newcommand
# inputs : command (string), value (string or castable to string)
def newcommand(command, value):
    # idk append this list when encountering commands
    if command in ["\\a", "\\angle"]:
        return renewcommand(command, value)
    return "\\newcommand{"+command+"}{"+str(value)+"}\n"

# generic \renewcommand
def renewcommand(command, value):
    return "\\renewcommand{"+command+"}{"+str(value)+"}\n"

# generic \newcommand with dfrac
def newcommand_dfrac(command, numerator, denominator):
    # turn things integer
    numerator, denominator = int(numerator), int(denominator)
    # make coprime
    gcd = np.gcd(numerator, denominator)
    assert gcd != 0, "null GCD?"
    numerator //= gcd
    denominator //= gcd
    # sign is always on top
    if denominator < 0:
        numerator *= -1
        denominator *= -1

    # integer case
    if denominator == 1:
        return newcommand(command, numerator)
    
    # else
    return newcommand(command, "\dfrac{"+str(numerator)+"}{"+str(denominator)+"}")

def newcommand_mult(command, numerator, denominator):
    """
    Fonction qui crée un commande \dfrac{numerator}{denominator} irréductible.
    La constante numerator/denominator est supposée multiplicative :
        - si elle est 1, elle n'affiche rien
        - le signe positif n'est pas affiché
        - le signe négatif est uniquement au numérateur le cas échéant
    
    INPUTS : numerator, denominator (signed ints)
    """

    # make coprime
    gcd = np.gcd(numerator, denominator)
    assert gcd != 0, "null GCD?"
    numerator //= gcd
    denominator //= gcd
    # sign is always on top
    if denominator < 0:
        numerator *= -1
        denominator *= -1

    # case val = 1
    if (denominator == 1) and (numerator == 1):
        return newcommand(command, "")
    
    # case val is integer
    if denominator == 1:
        return newcommand(command, numerator)

    # else
    return newcommand(command, "\dfrac{"+str(numerator)+"}{"+str(denominator)+"}")

def newcommand_add(command, numerator, denominator):
    """
    Fonction qui crée un commande \dfrac{numerator}{denominator} irréductible.
    La constante numerator/denominator est supposée additive :
        - si elle est 0, elle n'affiche rien
        - le signe positif est affiché
        - le signe négatif est devant la fraction le cas échéant
    
    INPUTS : numerator, denominator (signed ints)
    """

    # make coprime
    gcd = np.gcd(numerator, denominator)
    assert gcd != 0, "null GCD?"
    numerator //= gcd
    denominator //= gcd
    # sign is always on top
    if denominator < 0:
        numerator *= -1
        denominator *= -1

    # case val = 0
    if numerator == 0:
        return newcommand(command, "")
    
    # else
    # sign is separated
    sign = "+" if numerator>=0 else "-"
    numerator = np.abs(numerator)
    
    # case val is integer
    if denominator == 1:
        return newcommand(command, sign+str(numerator))
    
    return newcommand(command, sign+"\dfrac{"+str(numerator)+"}{"+str(denominator)+"}")

# write decimal separator with commas instead of dots
def comma(num):
    return f'{num}'.replace('.', ',')

###############################################

def write(CONTENT, seed):
    # WRITE TO FILE

    FILE_NAME = f"adr/vars_{seed}.adr"

    with open(FILE_NAME, 'w') as file:
        file.write(CONTENT)
    return 0

def pdflatex(seed):
    # COMPILE WITH VARS INPUT

    FILE_NAME = f"adr/vars_{seed}.adr"

    INPUTS = "\input{preamble.tex} \input{"+FILE_NAME+"} \input{dm.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"
    # suppress output
    PARAMETER3 = "-interaction=batchmode"

    print(f"COMPILING SEED {seed}")
    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, PARAMETER3, INPUTS])
    #subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, PARAMETER3, INPUTS])
    # compile twice if references are required
    
    return 0

###############################################
############# GENERATE FUNCTION ###############
###############################################

def system2():
    """
    Part d'un système 2x2 diagonal Dx = b entiers.
    Génère A entière aléatoire inversible ; nouveau système AD x = Ab <=> Mx = c.
    """
    
    # nonzero diagonal
    diag = [0,0]
    while diag[0]*diag[1] == 0:
        diag = (np.random.rand(2)*22-11).astype(int)

    D = np.diag(diag)

    # nonzero integer b
    b = [0,0]
    while b[0]*b[1] == 0:
        b = (np.random.rand(2)*30-15).astype(int)

    # invertible A, no zero coeffs
    A = np.zeros((2,2))
    while np.linalg.det(A) == 0 or A[0,0]*A[0,1]*A[1,0]*A[1,1]==0:
        A = (np.random.rand(2,2)*26-13).astype(int)
    
    # ADx = Mx = Ab = c
    M = A@D
    c = A@b
    
    return D, b, M, c

def generate(seed):
    CONTENT = newcommand("\seed", seed)
    """
    Ex1 : simple 2x2 system Ax = b. A is invertible.

    Ex2 : 3x3 system from 2x2 subsystem.
    """
   
    #np.random.rand(10)
   
    ### EX 1 ###

    D, b, M, c = system2()

    # write
    CONTENT += newcommand_dfrac("\\x", b[0], D[0,0])
    CONTENT += newcommand_dfrac("\\y", b[1], D[1,1])

    CONTENT += newcommand_dfrac("\\ba", c[0], 1)
    CONTENT += newcommand_dfrac("\\bb", c[1], 1)
    CONTENT += newcommand_mult("\\Aa", M[0,0], 1)
    CONTENT += newcommand_add("\\Ab", M[0,1], 1)
    CONTENT += newcommand_mult("\\Ac", M[1,0], 1)
    CONTENT += newcommand_add("\\Ad", M[1,1], 1)
    
    ### EX 2 ###

    D, b, M, c = system2()
    
    # create larger M3, 3-by-3 matrix from embedding of 2-by-2 M.
    M3 = np.zeros((3,3)).astype(int)
    M3[1:, 1:] = M
    c3 = np.zeros(3)
    c3[1:] = c
    
    # first row has full support.
    # and they i add a nonzero multiple of the first row onto the second and third rows
    # one multiple is positive, the other negative :)
    
    # row1 is r@x = b1
    r = [0,0,0]
    b1 = 0
    while r[0]*r[1]*r[2]*b1 == 0 or np.linalg.det(M3) == 0:
        r = (np.random.rand(3)*20-10).astype(int)
        b1 = np.random.rand()*20-10
        b1=int(b1)
        M3[0,:] = r

    c3[0] = b1

    # m1 and m2 are multiples st m1*m2 < 0
    m1, m2 = 0, 0
    while m1 in [0, 1, -1] or m2 in [0, 1, -1] or m1*m2 > 0 or np.gcd(m1,m2)!=1:
        [m1, m2] = (np.random.rand(2)*16-8).astype(int)

    # elementary P
    P = np.array([[1,0,0],[m1,1,0],[m2,0,1]]).astype(int)
    MM = P@M3
    cc = P@c3


    # write
    CONTENT += newcommand_dfrac("\\yII", b[0], D[0,0])
    CONTENT += newcommand_dfrac("\\zII", b[1], D[1,1])
    CONTENT += newcommand_dfrac("\\xII", b1*D[0,0]*D[1,1] - r[1]*D[1,1]*b[0] - r[2]*D[0,0]*b[1] , D[0,0]*D[1,1]*r[0])

    CONTENT += newcommand_dfrac("\\baII", cc[0], 1)
    CONTENT += newcommand_dfrac("\\bbII", cc[1], 1)
    CONTENT += newcommand_dfrac("\\bcII", cc[2], 1)
    CONTENT += newcommand_mult("\\AaII", MM[0,0], 1)
    CONTENT += newcommand_add("\\AbII", MM[0,1], 1)
    CONTENT += newcommand_add("\\AcII", MM[0,2], 1)
    CONTENT += newcommand_mult("\\AdII", MM[1,0], 1)
    CONTENT += newcommand_add("\\AeII", MM[1,1], 1)
    CONTENT += newcommand_add("\\AfII", MM[1,2], 1)
    CONTENT += newcommand_mult("\\AgII", MM[2,0], 1)
    CONTENT += newcommand_add("\\AhII", MM[2,1], 1)
    CONTENT += newcommand_add("\\AiII", MM[2,2], 1)

    CONTENT += newcommand_dfrac("\\baIII", c[0], 1)
    CONTENT += newcommand_dfrac("\\bbIII", c[1], 1)
    CONTENT += newcommand_mult("\\AaIII", M[0,0], 1)
    CONTENT += newcommand_add("\\AbIII", M[0,1], 1)
    CONTENT += newcommand_mult("\\AcIII", M[1,0], 1)
    CONTENT += newcommand_add("\\AdIII", M[1,1], 1)
   
    ### EX 3 ###

    # u, w noncolinear
    uw = np.zeros((2,2))
    while np.linalg.det(uw) == 0 or uw[0,0]*uw[0,1]*uw[1,0]*uw[1,1] == 0:
        uw = (np.random.rand(2,2)*30 - 60).astype(int)

    u = uw[:,0]
    w = uw[:, 1]
    
    # v, nonzero multiple of u

    m = 0
    while m == 0:
        m = np.random.rand()*22-11
        m=int(m)
    
    v = m*u

    # write
    CONTENT += newcommand_dfrac("\\baIV", w[0], 1)
    CONTENT += newcommand_dfrac("\\bbIV", w[1], 1)
    CONTENT += newcommand_mult("\\AaIV", u[0], 1)
    CONTENT += newcommand_add("\\AbIV", v[0], 1)
    CONTENT += newcommand_mult("\\AcIV", u[1], 1)
    CONTENT += newcommand_add("\\AdIV", v[1], 1)

    # vector form
    CONTENT += newcommand_dfrac("\\baV", w[0], 1)
    CONTENT += newcommand_dfrac("\\bbV", w[1], 1)
    CONTENT += newcommand_dfrac("\\AaV", u[0], 1)
    CONTENT += newcommand_dfrac("\\AbV", v[0], 1)
    CONTENT += newcommand_dfrac("\\AcV", u[1], 1)
    CONTENT += newcommand_dfrac("\\AdV", v[1], 1)

    return CONTENT    


### main ###

if __name__=="__main__":

    N = 1
    # always the same N to recompile if needed
    np.random.seed(3) # troua :)  

    for _ in range(N):
        ## SEED ##
        seed = int(np.random.rand() * (2**16 - 1))

        # uncomment to fix seed
        #seed=34414

        np.random.seed(seed)
        
        CONTENT = generate(seed)
        write(CONTENT, seed)
        pdflatex(seed)




