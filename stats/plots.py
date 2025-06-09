import pandas as pd
import plotly.express as px

df = pd.read_csv("notes.csv")

# subframe
df=df.iloc[:34, 3:26].astype('float')

# stats
stats = df.describe()

means = df.mean()

DS = ["DS"]
AUT = ["Aut"]
DM = ["DM"]
EX = ["EX"]

BAR = pd.DataFrame({
    "Évaluation": means.index,
    "Moyenne": means.values,
    "Type": DS*3+AUT+EX*2+DS+DM+AUT+EX+DM+DS*2+AUT+DS+DM+AUT+EX+AUT+DM+DS+DM+AUT,
    "Trimestre": ["Trimestre 1"]*4+["Trimestre 2"]*10+["Trimestre 3"]*9,
    "Poids": [.5,1,1,.5,.5,.5,1,1,.5,.5,1,1,1,.5,2,.5,.5,0,.5,.5,2,.5,.5],
})

# idk why but color = Type reorders shit
fig = px.bar(BAR, 
        x="Évaluation", 
        y = "Moyenne", 
        #color="Type", 
        title="Moyennes",
    )

#colour now i guess
fig.update_traces(marker_color=["#ff7f0e" if i == "DS" else "#1f77b4" if i == "DM" else "#2ca02c" if i =="Aut" else "#9467bd" for i in BAR.Type], showlegend=False)

fig.show()

##### Moyennes pondérées par trimestre avec et sans DM ####

BAR.set_index("Trimestre", inplace=True)

# toutes les notes

MOY_POND_DM = (BAR.Moyenne*BAR.Poids).groupby("Trimestre").sum()/(BAR.Poids).groupby("Trimestre").sum()
MOY_POND_DM = MOY_POND_DM.to_frame("Moyenne avec DM")

# toutes sauf les DM

BAR.query("Type != 'DM'", inplace=True)

MOY_POND_NO_DM = (BAR.Moyenne*BAR.Poids).groupby("Trimestre").sum()/(BAR.Poids).groupby("Trimestre").sum()
MOY_POND_NO_DM = MOY_POND_NO_DM.to_frame("Moyenne sans DM")

GROUP = MOY_POND_DM.merge(MOY_POND_NO_DM, left_index=True, right_index=True)

fig = px.bar(GROUP,barmode="group")

fig.show()



