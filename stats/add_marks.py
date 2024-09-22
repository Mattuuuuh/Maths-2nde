import pandas as pd
from config import NUM_STUDENTS, FILE_NAME
import numpy as np

MARKS = np.array([
        9.5, 10, 8, 8.5, 6, 13.5, 9.5, 8.5,
        4.5, 10.5, 5, 6.5, 8.5, 3.5, 15.5, 2, 8.5,
        9, 5, 8.5, 11.5, 4.5, 7.5, 5.5, 1.5, 9.5, 
        11.5, 12, 11, 11, 8.5, 10.5, 14, 7])/15*20

assert len(MARKS) == NUM_STUDENTS, "Number of studnets does not match that of marks."

d = pd.read_csv(FILE_NAME, index_col = "Élève n°")

COLUMN_NAME = "Arithmétique"

assert not COLUMN_NAME in d.columns, f"This will overwrite column {COLUMN_NAME}" 

notes = pd.DataFrame({
    "Élève n°": range(1,NUM_STUDENTS+1),
    COLUMN_NAME: MARKS,
    }).set_index("Élève n°")

d = d.join(notes)

d.to_csv(FILE_NAME)
print(f"Saved marks to relative path {FILE_NAME}.")
