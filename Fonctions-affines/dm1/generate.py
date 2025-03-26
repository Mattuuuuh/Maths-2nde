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

    INPUTS = "\input{preamble.tex} \input{"+FILE_NAME+"} \input{dm1.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"

    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    # compile twice if references are required
    
    return 0

###############################################
############# GENERATE FUNCTION ###############
###############################################

# random pythagorean triple with generating formula (m²-n²)² + (2mn)² = (m²+n²)²
# where 2<=n+1<=m<=15 (to keep things small)
def pythagorean_triple():
    m = int(np.random.rand()*13)+3
    n = int(np.random.rand()*(m-2))+2
    assert 2 <= n+1 <= m <= 15, "Bounds 2 <= n+1 <= m <= 15 not verified."
    
    # triple (u,v,w)
    u = m**2 - n**2
    v = 2*m*n
    w = m**2+n**2

    # coin toss to swap u and v
    if np.random.rand()<.5:
        u,v=v,u
   
    assert u**2 + v**2 == w**2, "Pythagorean triple ain't one."
    return u, v, w

def generate(seed):
    """
    Generates f(x) = ax+b, g(x) = a'x+b', and h(x) = a'' x + b'' such that
    f and h cross at A, g and h cross at B, and ||A|| = ||B|| = L.
    The triangle formed by the three lines is isosceles.

    a, a', a'' are rationnal
    A, B are rationnal (implying a, a' are pythogorean ratios)
    L is integer between 5 and 15.
    x_offset and y_offset is integer between -10 and 10, nonzero.
    """

    ### EX 1 ###

    CONTENT = newcommand("\seed", seed)

    [u1, v1, w1] = pythagorean_triple()
    [u2, v2, w2] = pythagorean_triple()
    assert u1*u2 != 0, "v1 or v2 is zero?"
    a1 = v1/u1
    a2 = v2/u2

    # must keep slopes different!
    # must keep angles at least pi/6-far away from each other
    while v1/u1 == v2/u2 or np.abs(np.arctan(a1) - np.arctan(a2)) < np.pi/6 :
        [u1, v1, w1] = pythagorean_triple()
        [u2, v2, w2] = pythagorean_triple()
        assert u1*u2 != 0, "v1 or v2 is zero?"
        a1 = v1/u1
        a2 = v2/u2

    assert w1 != 0 and w2 != 0, "w is zero in Pythagorean triple?"

    # slopes of f and g: a = v/u 
    CONTENT += newcommand_mult("\\aI", v1, u1)
    CONTENT += newcommand_mult("\\aII", v2, u2)
   

    # length L = ||A|| = ||B||
    L = int(np.random.rand()*11)+5
    assert 5 <= L <= 15, "Bound 5 <= L <= 15 is not verified."

    # points A and B

    assert L*u1/w1 != -L*u2/w2, "A and B have same x-coordinate: function h is ill-defined."
    # coin toss for sign of x (such that xA*xB < 0 to keep things interesting)
    sign=+1
    if np.random.rand()<.5:
        sign=-1

    # coordinates of A and B: x = sign*L*u/w and y = sign*L*v/w
    # not needed and will be offset
    """
    CONTENT += newcommand_dfrac("\\xA", sign*L*u1, w1)
    CONTENT += newcommand_dfrac("\\yA", sign*L*v1, w1)
    
    CONTENT += newcommand_dfrac("\\xB", -sign*L*u2, w2)
    CONTENT += newcommand_dfrac("\\yB", -sign*L*v2, w2)
    """

    # creating h going through A and B
    # signs cancel out to make a = (v1*w2+v2*w1)/(u1*w2+u2*w1), denominator nonzero already asserted (xA != xB).
    # b = sign*(L*u2*v1-L*u1*v2) / (u1*w2 + u2*w1), denominator nonzero
    a3_numerator = v1*w2+v2*w1
    a3_denominator = u1*w2+u2*w1
    CONTENT += newcommand_mult("\\aIII", a3_numerator, a3_denominator)
    
    a3 = a3_numerator/a3_denominator
    assert a3 != u1/v1 and a3 != u2/v2, "Slopes are identical."
    
    b3_numerator = sign*(L*u2*v1-L*u1*v2) 
    b3_denominator = u1*w2 + u2*w1

    # offset everything to make nonlinear functions
    # new functions are a*(x-x_offset) + b + y_offset = a*x + b + y_offset - a*x_offset
    x_offset, y_offset = (np.random.rand(2)*20 - 9).astype(int)
    if x_offset <= 0:
        x_offset -= 1
    if y_offset <= 0:
        y_offset -= 1

    assert -10 <= x_offset <= 10 and x_offset != 0, "-10 <= x_offset <= 10 and x_offset != 0 is not verified."
    assert -10 <= y_offset <= 10 and y_offset != 0, "-10 <= y_offset <= 10 and y_offset != 0 is not verified."

    CONTENT += newcommand("\\xC", x_offset)
    CONTENT += newcommand("\\yC", y_offset)

    # defining the y-intercepts
    # for f, g, b = 0 + y_offset - x_offset*v/u = (u*y_offset-x_offset*v)/u
    CONTENT += newcommand_add("\\bI", u1*y_offset-v1*x_offset, u1)
    CONTENT += newcommand_add("\\bII", u2*y_offset-v2*x_offset, u2)

    # for h, b = b3_num/b3_denom + y_offset - a3_num/a3_denom*x_offset ...
    # = (b3_num*a3_denom + y_offset*a3_denom*b3_denom - a3_num*x_offset*b3_denom)/(b3_denom*a3_denom)
    CONTENT += newcommand_add("\\bIII", b3_numerator*a3_denominator + y_offset*b3_denominator*a3_denominator - a3_numerator*x_offset*b3_denominator, b3_denominator*a3_denominator)

    # real values for graphs, etc...
    xA, yA = sign*L*u1/w1+x_offset, sign*L*v1/w1+y_offset
    xB, yB = -sign*L*u2/w2+x_offset, -sign*L*v2/w2+y_offset

    xmin = int(min(xA, xB, x_offset,0))-2
    xmax = int(max(xA, xB, x_offset,0))+2
    ymin = int(min(yA, yB, y_offset,0))-2
    ymax = int(max(yA, yB, y_offset,0))+2

    CONTENT += newcommand("\\xmin", xmin)
    CONTENT += newcommand("\\xmax", xmax)
    CONTENT += newcommand("\\ymin", ymin)
    CONTENT += newcommand("\\ymax", ymax)
   
    ### SOLS ###

    CONTENT += newcommand("\\aIfloat", v1/u1)
    CONTENT += newcommand("\\aIIfloat", v2/u2)
    CONTENT += newcommand("\\aIIIfloat", a3_numerator/a3_denominator)
    CONTENT += newcommand("\\bIfloat", (u1*y_offset-v1*x_offset)/u1)
    CONTENT += newcommand("\\bIIfloat", (u2*y_offset-v2*x_offset)/u2)
    CONTENT += newcommand("\\bIIIfloat", (b3_numerator*a3_denominator + y_offset*b3_denominator*a3_denominator - a3_numerator*x_offset*b3_denominator)/b3_denominator/a3_denominator)

    CONTENT += newcommand_dfrac("\\xA", sign*L*u1+w1*x_offset, w1)
    CONTENT += newcommand_dfrac("\\yA", sign*L*v1+w1*y_offset, w1)
    
    CONTENT += newcommand_dfrac("\\xB", -sign*L*u2+w2*x_offset, w2)
    CONTENT += newcommand_dfrac("\\yB", -sign*L*v2+w2*y_offset, w2)
    
    CONTENT += newcommand("\\xAfloat", xA)
    CONTENT += newcommand("\\yAfloat", yA)
    
    CONTENT += newcommand("\\xBfloat", xB)
    CONTENT += newcommand("\\yBfloat", yB)

    CONTENT += renewcommand("\\L", L)
    AB = np.sqrt((xA-xB)**2 + (yA-yB)**2)
    CONTENT += newcommand("\\AB", comma(np.round(AB,3)))

    """
    # troubleshooting
    print(sign)
    print(L)
    print(u1,v1,w1)
    print(u2,v2,w2)

    print(xA, yA)
    print(xB, yB)
    print(x_offset, y_offset)
    """

    ### EX 2 ###
    """
    Generates f(x) = ax where 0,20 <= a <= 0,30 is the slope.
    Angle is tan(slope) and slope is arctan(angle)

    Point A of absciss 300 <= xA <= 600
    Max slope of 0,05 <= a' <= a-0,05
    
    Example slope percent 60 <= s <= 100
    Example angle 5 <= angle <= 35
    """
    
    slope1 = .2 + int(np.random.rand()*11)*.01
    slope1 = round(slope1,2)
    slope1_percent = int(100*slope1)
    Ax = int(np.random.rand()*301)+300
    Ay = slope1*Ax
    Ay = round(Ay, 2)

    slope2 = 0.05+int(np.random.rand()*(slope1-.05)*100)/100
    slope2 = round(slope2,2)
    slope2_percent = int(100*slope2)

    slope_percent = 60 + int(np.random.rand()*41)
    angle = 5 + int(np.random.rand()*31)

    CONTENT += newcommand("\\slopeI", comma(slope1)) 
    CONTENT += newcommand("\\slopeIpercent", slope1_percent)
    CONTENT += newcommand("\\Ax", Ax) 
    CONTENT += newcommand("\\Ay", Ay) 
    CONTENT += newcommand("\\slopeII", comma(slope2)) 
    CONTENT += newcommand("\\slopeIIpercent", slope2_percent)
    CONTENT += newcommand("\\slopepercent", slope_percent) 
    CONTENT += newcommand("\\angle", angle)

    ### SOLS ###

    CONTENT += newcommand("\\Ayfloat", comma(Ay)) 
    CONTENT += newcommand("\\graphoffset", int(Ax/10))
    
    alpha = np.arctan(slope1)*180/np.pi
    alpha = comma(round(alpha,2))
    CONTENT += newcommand("\\alphaI", alpha)

    Cy = slope2*Ax
    Cy = comma(round(Cy,2))
    CONTENT += newcommand("\\Cy", Cy)
    
    beta = np.arctan(slope2)*180/np.pi
    beta = comma(round(beta,2))
    CONTENT += newcommand("\\betaI", beta)
    
    gamma = np.arctan(slope_percent/100)*180/np.pi
    gamma = comma(round(gamma,2))
    CONTENT += newcommand("\\gammaI", gamma)

    penteI = np.tan(angle*np.pi/180)
    penteI_percent = np.round(penteI*100,1)
    CONTENT += newcommand("\\penteIpercent", penteI_percent)

    return CONTENT    


### main ###

if __name__=="__main__":

    N = 1
    # always the same N to recompile if needed
    np.random.seed(51) # not a prime 

    for _ in range(N):
        ## SEED ##
        seed = int(np.random.rand() * (2**16 - 1))

        # uncomment to fix seed
        seed=36729

        np.random.seed(seed)
        
        CONTENT = generate(seed)
        write(CONTENT, seed)
        pdflatex(seed)




