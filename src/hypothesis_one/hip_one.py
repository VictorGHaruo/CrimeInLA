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

# map = gpd.read_file('LAPD_Division_1980236667069515482.zip')
# df_map = gpd.GeoDataFrame(map).sort_values(by = ['APREC'], ascending = True)

df_grupos = hp.groups(df_Base, 'Crm Cd', 'AREA NAME', 0)

A = hp.severity(df_grupos, df_severity,'A', 'Crime', 'Gravidade')

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
hg.plot_barh(A, df_grupos['AREA NAME'], "barh")
exit()

hg.point_map(df_Base, 'LAT', 'LON','LAPD_Division_1980236667069515482.zip', 'LA_map2' )