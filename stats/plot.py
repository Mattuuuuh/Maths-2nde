import pandas as pd
import matplotlib.pyplot as plt
from config import NUM_STUDENTS, FILE_NAME

NUM_MARK = 1

d = pd.read_csv(FILE_NAME, index_col="Élève n°")

# histogramme d'un contrôle
def hist_exam(MARK_NAME, groups=True):
    """
    Histogramme du contrôle "Note {NUM_MARK}"
    """
    assert MARK_NAME in d.columns, f"Pas de colonne {COLUMN_NAME}"
    
    if groups:
        g1 = d[d["Groupe"]==1][MARK_NAME]
        g2 = d[d["Groupe"]==2][MARK_NAME]
        print("GROUPE 1")
        print(g1.describe())
        g1.hist(bins=20)
        plt.show()

        print("GROUPE 2")
        print(g2.describe())
        g2.hist(bins=20)
        plt.show()
    
    print("CLASSE ENTIÈRE.")
    whole_class=d[MARK_NAME]
    print(whole_class.describe())
    whole_class.hist(bins=20)
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

if __name__ == "__main__":
    hist_exam("Arithmétique")
