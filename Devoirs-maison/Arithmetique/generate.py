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


    return R

###############################################
############## USING DM LIBRARY ###############
###############################################

dm = DM(
        FOLDER="Arithmetique/",
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




