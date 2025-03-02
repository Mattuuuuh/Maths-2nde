import subprocess
import numpy as  np
import contfrac

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
    
    # case val is integer
    if denominator == 1:
        return newcommand(command, numerator)

    # else
    # sign is separated
    sign = "+" if numerator>=0 else "-"
    numerator = np.abs(numerator)
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

    INPUTS = "\input{preamble.tex} \input{"+FILE_NAME+"} \input{dm2.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"

    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    #subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    # compile twice if references are required
    
    return 0

###############################################
############# GENERATE FUNCTION ###############
###############################################

def generate(seed):
    """
    Generate a ratio l/L uniformly in (.66, .76) and take l, L a convergent of this ratio.
    We're being hopeful that l, L aren't trivial (l=1 would suck since l isn't always a multiplicative constant).
    We pick around 0.71 such that arccos(ratio) is around .5, since sqrt(2)/2 = 0.7071.
    This makes it so that the max is around the middle. If xmax is too close to either end, then the values around it are really close and it's not super fun to compare/draw.

    Set f(x) = l*sin(x)/(L-l*cos(x)) on [0, pi/2] (up to pi actually but only quarter trig circle is defined for now).
    Let xmax = arccos(l/L)*180/pi, the maximum of f in degrees. xmax belongs in [0, 90°].

    Pick 11 samples, every 9°. 
    Add samples every .5° around xmax to finally get 20 samples.
    Samples are ordered and their images computed to partially fill the table (and for solutions).
    """
    
    CONTENT = newcommand("\seed", seed)

    ###### l/L = ratio UNIFORM IN [.65, .75]
    ratio = np.random.rand()*.1 + .66
    ratio = np.round(ratio,5)
    # look for good integer approximations of ratio: diophantine approximations! continued fractions :)
    convergents = list(contfrac.convergents(ratio))
    l, L = convergents[3 if len(convergents)>3 else -1]
    newratio = l/L
    xmax = np.arccos(newratio)*180/np.pi

    CONTENT += renewcommand("\l", l)
    CONTENT += renewcommand("\L", L)
    CONTENT += newcommand("\\ratio", newratio)
    CONTENT += newcommand("\\xmax", xmax)

    ###### 20 SAMPLES IN [0,90°] WITH FOCUS AROUND XMAX

    # start with 11 samples every 9 outside xmax
    samples = [9*i for i in range(11) if np.abs(9*i - xmax) > 4.5]

    num_samples = len(samples)
    assert num_samples <= 20, "Already more than 20 samples?"
    num_to_add = 20 - num_samples

    # take a, b integers st. [-a, b[ is centered around 0 and has a+b = num_to_add integers 
    a = num_to_add//2
    b = num_to_add-a
    if num_to_add%2 != 0:
        b+=1 # or a+=1 for that matter.
    
    roundedxmax = int(np.rint(xmax))
    samples += [roundedxmax + (.5*i if i%2!=0 else int(.5*i)) for i in range(-a, b)]
    
    samples = np.array(samples, dtype=object) # to prevent typecasting ints to float
    samples = np.unique(samples) # remove duplicates before checking size.
    assert len(samples) == 20, "Not exactly 20 unique samples?"

    # sort the samples and ship them :)
    samples = np.sort(samples)

    ROMAN_NUMERALS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII",
        "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII",
        "XVIII", "XIX", "XX"]

    for roman, arabic in zip(ROMAN_NUMERALS, range(20)):
        CONTENT += newcommand(f"\\sample{roman}", comma(samples[arabic]))
    
    # compute the images and ship them
    f = lambda x: np.arctan(l*np.sin(x)/(L - l*np.cos(x)))
    # using deg2rag is actually key for accuracy for some reason.
    # see cos(pi/100) vs cos(deg2rad(18))
    fdeg = lambda x: f(np.deg2rad(x))*180/np.pi
    images = fdeg(np.array(samples, dtype=float))
    images = np.round(images, 4)

    for roman, arabic in zip(ROMAN_NUMERALS, range(20)):
        CONTENT += newcommand(f"\\image{roman}", comma(images[arabic]))
    print(ratio, xmax)

    for i in range(20):
        print(samples[i], images[i])

    return CONTENT    


### main ###

if __name__=="__main__":

    N = 10
    # always the same N to recompile if needed
    np.random.seed(650587708) # int("arccos",36)

    for _ in range(N):
        ## SEED ##
        seed = int(np.random.rand() * (2**16 - 1))

        # uncomment to fix seed
        #seed=1

        np.random.seed(seed)
        
        CONTENT = generate(seed)
        write(CONTENT, seed)
        pdflatex(seed)




