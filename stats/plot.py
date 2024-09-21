import pandas as pd
import matplotlib.pyplot as plt
from config import NUM_STUDENTS, FILE_NAME

NUM_MARK = 1

d = pd.read_csv(FILE_NAME, index_col="Élève n°")

# histogramme d'un contrôle
def hist_exam(NUM_MARK):
    """
    Histogramme du contrôle "Note {NUM_MARK}"
    """
    COLUMN_NAME = f"Note {NUM_MARK}"
    assert COLUMN_NAME in d.columns, f"Pas de colonne {COLUMN_NAME}"

    d[COLUMN_NAME].hist(bins=20)
    plt.show()
    return 0

# évolution des N derniers contrôles
def evo_exam_N(N):
    # TODO
    return 0

# évolution par élève
def evo_eleve(N):
    #TODO
    return 0

if __name__ = "__main__":
    hist_exam(1)
