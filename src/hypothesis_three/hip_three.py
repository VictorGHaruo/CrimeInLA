import pandas as pd

file = pd.read_csv("../../data/cleaned_dataset.csv", sep= ";")

print (file["Crm Cd"].unique())