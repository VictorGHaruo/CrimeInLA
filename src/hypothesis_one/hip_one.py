import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import hip_one_data_treatment as hp 
import hip_one_graphics as hg

filepath = "reductdata.csv"
Base = pd.read_csv(filepath)
df_Base = pd.DataFrame(Base)

filepath2 = 'severity.xlsx'
severity = pd.read_excel(filepath2)
df_severity = pd.DataFrame(severity)

map = gpd.read_file('LAPD_Division_1980236667069515482.zip')
df_map = gpd.GeoDataFrame(map).sort_values(by = ['APREC'], ascending = True)

df_grupos = hp.groups(df_Base, 'Crm Cd', 'AREA NAME', 0)

df_map['crime'] = df_grupos[110]

hg.geo_heatmap(df_map, 'crime', 'La_map')
