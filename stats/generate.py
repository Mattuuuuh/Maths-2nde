import pandas as pd
from config import NUM_STUDENTS, FILE_NAME, NAMES

d = pd.DataFrame({
    "Élève n°": range(1, NUM_STUDENTS+1),
    "Nom": NAMES,
    "Groupe": [1]*17 + [2]*17,
    }).set_index("Élève n°")

d.to_csv(FILE_NAME)
print(f"Saved marks to relative path {FILE_NAME}.")

