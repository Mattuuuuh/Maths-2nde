import subprocess
import numpy as np

# from [roman.toRoman(i) for i in range(1,31)]
ROMAN_NUMERALS = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX']

NUMBER_OF_EXERCISES = 11
NUMBER_OF_EXAMS = 35

# shuffled range(NUMBER_OF_EXAMS), integers
def exercise_commands(shuffled_list):
    COMMANDS = ""
    assert len(ROMAN_NUMERALS) >= len(shuffled_list), "Not enough roman numerals in the list."
    for NUMERAL, INDEX in zip(ROMAN_NUMERALS, shuffled_list):
        COMMANDS += r"\newcommand{\exe" + NUMERAL + "}{"+str(INDEX+1)+"}"
    return COMMANDS

def compile_exam(EXAM_NUMBER, INDICES):
    EXERCISE_COMMANDS = exercise_commands(INDICES)

    INPUTS = EXERCISE_COMMANDS+r"\input{randomized-eval1.tex}"
    PARAMETER1 = "-output-directory=out"
    PARAMETER2 = f"-jobname={EXAM_NUMBER}"
    PARAMETER3 = "-interaction=batchmode"

    print(f"COMPILING {EXAM_NUMBER} OF {NUMBER_OF_EXAMS}")
    subprocess.run(["pdflatex", PARAMETER1, PARAMETER2, PARAMETER3, INPUTS])
    subprocess.run(["pdflatex", PARAMETER1, PARAMETER2, PARAMETER3, INPUTS])
    return 0

if __name__=='__main__':
    INDICES = [i for i in range(NUMBER_OF_EXERCISES)]
    for EXAM_NUMBER in range(NUMBER_OF_EXAMS):
        # this is in-place
        np.random.shuffle(INDICES)
       
        # first exercise cannot be in last place (space reasons)
        # exercise 3 cannot be after exercise 1
        while INDICES[-1] == 0 or ( (np.array(INDICES)==0).nonzero() > (np.array(INDICES)==2).nonzero() ):
            np.random.shuffle(INDICES)

        compile_exam(EXAM_NUMBER, INDICES)


