import pandas as pd
import geopandas as gpd
import plotgraphics_h1 as pg

#Lendo os arquivos
filepath = "reductdata.csv"
Base = pd.read_csv(filepath)
df_Base = pd.DataFrame(Base)

map = gpd.read_file('LAPD_Division_1980236667069515482.zip')
df_map = gpd.GeoDataFrame(map).sort_values(by = ['APREC'], ascending = True)

pg.plot_h1(df_Base, df_map)

