import pandas as pd
import hypothesis_two.categorizer as ctg
import hypothesis_two.ploter as ptr

df = pd.read_csv("../data/Crime_Data_from_2020_to_Present.csv")
df = df[['DATE OCC', 'Crm Cd']]

df = ctg.date_to_year(df, 'DATE OCC')
df = ctg.category(df, 'Crm Cd')

ptr.png_year(df, '../data/pandemic/')
ptr.png_category(df, '../data/pandemic/')