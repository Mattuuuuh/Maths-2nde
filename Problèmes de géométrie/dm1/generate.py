import subprocess
import numpy as  np

def newcommand(current_str, command, value):
    if command in ["\d", "\k", "\Q", "\P"]:
        prefix = "\\renewcommand"
    else:
        prefix = "\\newcommand"
    return current_str+prefix+"{"+command+"}{"+str(value)+"}\n"

# write decimal separator with commas instead of dots
def comma(num):
    return f'{num}'.replace('.', ',')

def generate(seed):
    CONTENT = newcommand("", "\seed", seed)



    # WRITE TO FILE

    FILE_NAME = f"adr/vars_{seed}.adr"

    with open(FILE_NAME, 'w') as file:
        file.write(CONTENT)

    # COMPILE LATEX TWICE

    INPUTS = "\input{preamble.tex} \input{"+FILE_NAME+"} \input{dm1.tex}"
    PARAMETER1 = f"-output-directory=out"
    PARAMETER2 = f"-jobname=dm_{seed}"

    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    subprocess.run(["pdflatex",PARAMETER1, PARAMETER2, INPUTS])
    # compile twice for references 
    
    return 0

if __name__=="__main__":

    # always the same 34 to recompile if needed
    np.random.seed(1729) # taxicab number

    for _ in range(1):
        ## SEED ##

        seed = int(np.random.rand() * (2**16 - 1))
        # uncomment to fix seed
        seed="TEST"

        np.random.seed(seed)
        
        generate(seed)




