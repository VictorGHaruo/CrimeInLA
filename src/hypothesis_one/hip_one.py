import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geoplotlib
from geoplotlib.utils import read_csv


filepath = "reductdata.csv"

Base = pd.read_csv(filepath)
df_Base = pd.DataFrame(Base)

filepath2 = 'severity.xlsx'
severity = pd.read_excel(filepath2)
df_severity = pd.DataFrame(severity)

df_grupos = df_Base.groupby("Crm Cd Desc")["AREA NAME"].value_counts()

df_newdata = pd.DataFrame(sorted(df_Base["AREA NAME"].unique()), columns=["AREA NAME"])


# Retiramos os crimes que não aparecem em todas as cidades
for crime in df_Base['Crm Cd Desc'].unique():
    if len(df_grupos[crime]) == 21:
        df_newdata[crime] = df_grupos[crime].sort_index(ascending=True).values


# def gravidade_lookup(crm_cd):
#     if crm_cd in df_severity['Crime'].values:
#         return df_severity.loc[df_severity['Crime'] == crm_cd, 'Gravidade'].values[0]
#     else:
#         return None  

# df_high = np.zeros(21)
# df_medium = np.zeros(21)
# df_low = np.zeros(21)

# for i in df_newdata.columns:
#     if gravidade_lookup(i) == 'A':
#         df_low += df_newdata[i]
#     elif gravidade_lookup(i) == 'B':
#         df_medium += df_newdata[i]
#     elif gravidade_lookup(i) == 'C':
#         df_high += df_newdata[i]

# df_newdata["low"] = df_low
# df_medium['medium'] = df_medium
# df_high['high'] = df_high

def crime_graphbar(crime,areas,data):

    plt.bar(data[areas], data[crime] , edgecolor='black')
    plt.xlabel(data[areas])
    plt.ylabel(data[crime])
    plt.title(crime)
    plt.savefig(f'{crime}.png')

#crime_graphbar(510, "AREA NAME", df_newdata)

def crime_heatmap(data):

    df_data_numeric = data.select_dtypes(include=['float64', 'int64'])

    plt.figure(figsize=(86,21))

    sns.heatmap(df_data_numeric,annot = True, fmt = "d", cmap = "coolwarm")

    plt.title("Crimes")
    plt.xlabel("Crimes")
    plt.ylabel("Areas")

    plt.savefig('crimes.png')

geoplotlib.dot(df_Base)
geoplotlib.show()







