import pandas as pd
from matplotlib import pyplot as plt
import categorizer as ctg
import cleaner as cln
import graphic as gp

df = pd.read_csv("../../data/Crime_Data_from_2020_to_Present.csv")
df = df[['DATE OCC', 'Crm Cd']]

df = cln.date_to_year(df, 'DATE OCC')
df = ctg.add_category(df)

gp.save_png(df, 'DATE OCC', 'category',  '../../data/pandemic/')
gp.save_png(df, 'category', 'DATE OCC', '../../data/pandemic/')