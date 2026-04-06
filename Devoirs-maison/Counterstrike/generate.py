# importing DM class one folder above 
import sys
sys.path.append("..")
from DM import *

import numpy as  np

###############################################
############# GENERATE FUNCTION ###############
###############################################


def generate():
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
    
    R = ""
    
    
    # below is commented because something simpler is possible i think
    """
    ###### l/L = ratio UNIFORM IN [.66, .76]
    ratio = np.random.rand()*.1 + .66
    ratio = np.round(ratio,5)
    # look for good integer approximations of ratio: diophantine approximations! continued fractions :)
    convergents = list(contfrac.convergents(ratio))
    l, L = convergents[5 if len(convergents)>5 else -1]
    # not all l, L are possible here since (l,L)=1, 
    # so we can always take 2l, 2L or modify them slightly
    k=np.random.rand()*5+1
    k=int(k)
    l, L = k*l, k*L
    """
    # if i'm correct, q~unif(0,1) and p~unif(0,q) implies p/q~unif(0,1).
    # shown with total probability formula. P(p/q <= t) = int_0^1 P(p <= tq) dq = int_0^1 tq/q dq = t
    # implying that p/q*.1+0.66 ~ unif(.66,.76)
    # then make p, q integer are you're done imo
    #q = np.random.rand()
    #p = np.random.rand()*q
    #p=p*.1 + .66*q
    #
    #l = int(p*1000)
    #L = int(q*1000)

    # actually since alphastar = arccos(l/L), i'd rather have alphastar uniformly around [0,90].
    # so let x~U([10,80]) and set y = cos(x). Then arccos(y) is uniform.
    # now we have to set y ~ p/q. The error |y-p/q| is at most 1/q, so we can pick q uniformly in like [100, 1000] 
    # and let p = int(y·q).
    x = np.random.rand()*70 + 10
    y = np.cos(np.deg2rad(x))
    q = int(np.random.rand()*900+100)
    p = int(q*y)

    l = p
    L = q

    f = lambda x: np.arctan(l*np.sin(x)/(L-l*np.cos(x)))

    ratio = l/L
    xmax = np.arccos(ratio)*180/np.pi
    ymax = f(np.arccos(ratio))*180/np.pi

    R += renewcommand("l", l)
    R += renewcommand("L", L)
    R += newcommand("ratio", ratio)
    R += newcommand("xmax", xmax)
    R += newcommand("ymax", ymax)
    R += newcommand("ymaxplot", ymax*1.2)

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

    # REMOVED because samples are removed for now (p/q was between .66 and .76)
    #assert len(samples) == 20, "Not exactly 20 unique samples?"

    # sort the samples and ship them :)
    samples = np.sort(samples)

    ROMAN_NUMERALS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII",
        "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII",
        "XVIII", "XIX", "XX"]

    for roman, arabic in zip(ROMAN_NUMERALS, range(20)):
        R += newcommand(f"sample{roman}", comma(samples[arabic]))
    
    # compute the images and ship them
    f = lambda x: np.arctan(l*np.sin(x)/(L - l*np.cos(x)))
    # using deg2rag is actually key for accuracy for some reason.
    # see cos(pi/100) vs cos(deg2rad(18))
    fdeg = lambda x: f(np.deg2rad(x))*180/np.pi
    images = fdeg(np.array(samples, dtype=float))
    images = np.round(images, 4)

    for roman, arabic in zip(ROMAN_NUMERALS, range(20)):
        R += newcommand(f"image{roman}", comma(images[arabic]))
    #print(ratio, xmax)

    #for i in range(20):
    #    print(samples[i], images[i])
    
    return R

###############################################
############## USING DM LIBRARY ###############
###############################################

dm = DM(
        FOLDER="Counterstrike/",
        generating_function=generate,
        double_compile=True,
        initial_seed=666,
        a5=False,
    )

# for testing (seed 0)
#dm.write_adr()
#dm.compile_pdf()

# for generating seeds
dm.generate_seeds(40)
dm.write_adrs()
dm.compile_pdfs()

# for reading adr files in case initial seed is missing or NumPy changes something
#dm.read_adrs()
# compile
#dm.compile_pdfs()




