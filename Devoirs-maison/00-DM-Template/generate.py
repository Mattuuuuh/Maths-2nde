# importing DM class one folder above 
import sys
sys.path.append("..")
from DM import * 

import numpy as  np

###############################################
############# GENERATE FUNCTION ###############
###############################################

def generate():
    return newcommand("HW", "Hello World! hiya")

###############################################
############## USING DM LIBRARY ###############
###############################################

dm = DM(
        FOLDER="00-DM-Template/",
        generating_function=generate,
        double_compile=True,
        initial_seed=0,
    )

# for testing (seed 0)
dm.write_adr()
dm.compile_pdf()

# for generating seeds
#dm.generate_seeds(15)
#dm.write_adrs()
#dm.compile_pdfs()

# for reading adr files in case initial seed is missing or NumPy changes something
# TODO




