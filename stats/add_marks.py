import pandas as pd
from config import NUM_STUDENTS, FILE_NAME
import numpy as np

MARKS = [
        1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12,
        13, 14, 15, 16,
        17, 18, 19, 20,
        21, 22, 23, 24,
        25, 26, 27, 28,
        29, 30, 31, 32,
        33, 34,
        ]

MARKS = np.random.uniform(0, 20, NUM_STUDENTS)
MARKS = np.ceil(MARKS)

assert len(MARKS) == NUM_STUDENTS, "Number of studnets does not match that of marks."

d = pd.read_csv(FILE_NAME, index_col = "Élève n°")

NUM_MARK = len(d.columns)
COLUMN_NAME = f"Note {NUM_MARK}"

assert not COLUMN_NAME in d.columns, f"This will overwrite column {COLUMN_NAME}" 

notes = pd.DataFrame({
    "Élève n°": range(1,NUM_STUDENTS+1),
    COLUMN_NAME: MARKS,
    }).set_index("Élève n°")

d = d.join(notes)

d.to_csv(FILE_NAME)
print(f"Saved marks to relative path {FILE_NAME}.")
