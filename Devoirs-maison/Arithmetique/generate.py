# importing DM class one folder above 
import sys
sys.path.append("..")
from DM import *

import numpy as  np

###############################################
############# GENERATE FUNCTION ###############
###############################################

def construct_number(remove_primes=[]):
    # create n, m with with
    # one prime that's more difficult
    # and primes 2, 3, 5, as many as possible to keep between 2k and 10k.
    
    hard_primes = [7, 11, 13, 17, 19, 23]
    hard_choice = int_between(0,len(hard_primes)-1)
    prime = hard_primes[hard_choice]
    while prime in remove_primes:
        hard_choice = int_between(0,len(hard_primes)-1)
        prime = hard_primes[hard_choice]


    n = 1
    # n = primes**powers
    primes = [2,3,5,prime]
    powers = [0,0,0,0]
    choice = 3
    while n*prime < 1e4:
        n*= prime
        powers[choice]+=1
        choice = int_between(0,2)
        prime = [2,3,5][choice]
    
    return n, primes, powers


def generate():
    R = ""
    
    # EX 1

    # a<b coprime not unit
    a = int_between(2,10)
    b = int_between(a+1,a+10)
    d = np.gcd(a,b)
    while d==a:
        a = int_between(2,15)
        b = int_between(2,15)
        d = np.gcd(a,b)

    a //= d
    b //= d

    R += newcommand("aI", a)
    R += newcommand("bI", b)
    R += newcommand("abI", a*b)
    
    # size of AnB
    size = 4
    R += newcommand("bornesup", int((a*b*size)/10)*10)

    # SOL 1
    
    # finding au + bv = 1
    v = 1
    while (1-b*v)%a != 0:
        v+=1
    u = (1-b*v)//a

    R += newcommand("uI", u)
    R += newcommand("vI", v)

    # EX 2
    
    n, n_primes, n_powers = construct_number()
    # primes should be [2, 3, 5, hardprime]
    # n_powers should be [*, *, * , 1]

    R += newcommand("nII", n)
    R += newcommand("npowtwoII", n_powers[0])
    R += newcommand("npowthreeII", n_powers[1])
    R += newcommand("npowfiveII", n_powers[2])
    R += newcommand("nhardprimeII", n_primes[-1])
    
    m, m_primes, m_powers = construct_number(remove_primes=[n_primes[-1]])
    
    R += newcommand("mII", m)
    R += newcommand("mpowtwoII", m_powers[0])
    R += newcommand("mpowthreeII", m_powers[1])
    R += newcommand("mpowfiveII", m_powers[2])
    R += newcommand("mhardprimeII", m_primes[-1])

    # toss whether divisors divide n and not m XOR divide m and not n
    if np.random.rand()<.5:
        # divide n and not m
        R+= newcommand("dividenII", 1)
        
        # first divisor
        d1_powers = [
                int_between(0,n_powers[k])
                if n_powers[k]<=1
                else
                int_between(1,n_powers[k])
                for k in range(4)
            ]
        # force hard prime to appear because otherise multiplication sign is alone and i don't want to deal with it (3 x 5 x)
        d1_powers[-1]=1

        R += newcommand("dIpowtwoII", d1_powers[0])
        R += newcommand("dIpowthreeII", d1_powers[1])
        R += newcommand("dIpowfiveII", d1_powers[2])
        R += newcommand("dIpowhardprimeII", d1_powers[3])

        # second divisor
        d2_powers = [
                int_between(0,m_powers[k])
                if n_powers[k]<=1
                else
                int_between(1,m_powers[k])
                for k in range(4)
            ]
        # force hard prime to appear because otherise multiplication sign is alone and i don't want to deal with it (3 x 5 x)
        d2_powers[-1]=1
        
        # make some power too large
        k = int_between(0,3)
        d2_powers[k] = m_powers[k] + int_between(1,2)

        R += newcommand("dIIpowtwoII", d2_powers[0])
        R += newcommand("dIIpowthreeII", d2_powers[1])
        R += newcommand("dIIpowfiveII", d2_powers[2])
        R += newcommand("dIIpowhardprimeII", d2_powers[3])
        

    else:
        # divide m and not n
        R+= newcommand("dividenII", 0)
        
        # first divisor
        d1_powers = [
                int_between(0,n_powers[k])
                if n_powers[k]<=1
                else
                int_between(1,n_powers[k])
                for k in range(4)
            ]
        # force hard prime to appear because otherise multiplication sign is alone and i don't want to deal with it (3 x 5 x)
        d1_powers[-1]=1
        
        # make some power too large
        k = int_between(0,3)
        d1_powers[k] = n_powers[k] + int_between(1,2)
        
        R += newcommand("dIpowtwoII", d1_powers[0])
        R += newcommand("dIpowthreeII", d1_powers[1])
        R += newcommand("dIpowfiveII", d1_powers[2])
        R += newcommand("dIpowhardprimeII", d1_powers[3])

        # second divisor
        d2_powers = [
                int_between(0,m_powers[k])
                if n_powers[k]<=1
                else
                int_between(1,m_powers[k])
                for k in range(4)
            ]
        # force hard prime to appear because otherise multiplication sign is alone and i don't want to deal with it (3 x 5 x)
        d2_powers[-1]=1

        R += newcommand("dIIpowtwoII", d2_powers[0])
        R += newcommand("dIIpowthreeII", d2_powers[1])
        R += newcommand("dIIpowfiveII", d2_powers[2])
        R += newcommand("dIIpowhardprimeII", d2_powers[3])

    # SOL 2
    
    R += newcommand("sumIpowtwoII", n_powers[0]+m_powers[0])
    R += newcommand("sumIpowthreeII", n_powers[1]+m_powers[1])
    R += newcommand("sumIpowfiveII", n_powers[2]+m_powers[2])

    R += newcommand("sumIIpowtwoII", n_powers[0]+2*m_powers[0])
    R += newcommand("sumIIpowthreeII", n_powers[1]+2*m_powers[1])
    R += newcommand("sumIIpowfiveII", n_powers[2]+2*m_powers[2])

    R += newcommand("sumIIIpowtwoII", 3*n_powers[0])
    R += newcommand("sumIIIpowthreeII", 3*n_powers[1])
    R += newcommand("sumIIIpowfiveII", 3*n_powers[2])

    return R

###############################################
############## USING DM LIBRARY ###############
###############################################

dm = DM(
        FOLDER="Arithmetique-star/",
        generating_function=generate,
        double_compile=True,
        initial_seed=666,
        a5=True,
    )

# for testing (seed 0)
dm.write_adr()
dm.compile_pdf()

# for generating seeds
#dm.generate_seeds(80)
#dm.write_adrs()
#dm.compile_pdfs()

# for reading adr files in case initial seed is missing or NumPy changes something
#dm.read_adrs()
# compile
#dm.compile_pdfs()




