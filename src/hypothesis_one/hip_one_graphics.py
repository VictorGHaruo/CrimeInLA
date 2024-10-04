
"""
This module is responsible for generating and saving graphics for analysis in the project.

Functions
---------
plot_heatmap(df, ylabel, title)
    Plota um gráfico de calor e salva localmente no formato png.
point_map(df,LAT, LON , map, title)
    Plota uma mapa sobreposto por pontos em coordenadas específicas

Examples
--------
    >>> import hip_one_graphics as hg
    >>> hg.plot_heatmap(df, 'AREA NAME', 'heatmap')
    >>> hg.ponit_map(df,'LAT','LON','Local_map.geosjon' , 'LA_map')

Author
------
    Lucas Lima <luquinhasnm035@gmail.com>

License:
--------
    FGV License
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import numpy as np


def plot_heatmap(df : pd.DataFrame ,ylabel : str ,title : str):
    """
    Cria um mapa de calor para a análise dos dados.

    Parameters
    ----------
    df: pd.Dataframe
        Dataframe que contém os dados do gráfico.
    ylabel : str
        Nome da coluna cujos valores representam o eixo y do gráfico.
    title : str
        Título do gráfico. 

    Returns
    -------
    None
        This function generates a .png file with the graphic.
    """

    df_data_numeric = df.select_dtypes(include=['float64', 'int64'])

    plt.figure(figsize = (9,21))

    sns.heatmap(df_data_numeric,annot = True, fmt = "d", cmap = "coolwarm",yticklabels = df[ylabel])

    plt.title(title)
    plt.ylabel(ylabel)

    plt.savefig(f'{title}.png')
    plt.close
    

def point_map(df : pd.DataFrame ,LAT : str ,LON : str ,map : str ,title : str):

    """
    Cria um mapa com sobreposição de pontos em coordenadas específicas

    Parameters
    ----------
    df: pd.Dataframe
        Dataframe que contém os dados do gráfico.
    LAT : str
        Nome da coluna de df que contém os dados da latitude dos pontos.
    LON : str
        None da coluna de df que contém os dado da longitude dos pontos . 
    map : str
        Endereço do arquivo que contém os dados do mapa.
    title : str
        Título do gráfico.

    Returns
    -------
    None
        This function generates a .png file with the graphic.
    """
    
    df_coordinates = df[[LON,LAT]]

    df_coordinates = df_coordinates[(df_coordinates['LON'] != 0) & (df_coordinates['LAT'] != 0)]

    map = gpd.read_file('Stormwater_Capture_Master_Plan_(SCMP)_Priority_Infiltration_Areas.geojson')

    geometry = gpd.points_from_xy(df_coordinates['LON'], df_coordinates['LAT'])
    geo_df = gpd.GeoDataFrame(df_coordinates ,geometry= geometry )

    fig ,ax = plt.subplots(figsize=(35, 35))
    ax.set_aspect('equal')

    map.plot(ax=ax, color='lightgrey', edgecolor='black')  
    geo_df.plot(ax=ax, color='red', markersize=50, label='Coordinates')  

    plt.savefig(f"{title}.png", dpi=300, bbox_inches='tight')
    plt.close

graph_settings = {"dpi": 1000,
                  "x_name": "Areas",
                  "y_name": "Quantities",
                  "edge_color": "teal",
                  "face_color": "powderblue",
                  "f_color": "mediumturquoise",
                  "m_color": "cadetblue"
                  }

def plot_graphic(graphic_data: pd.Series , graphic_name: str,xticks : pd.Series, gs: dict = graph_settings):
    """
    Creates a bar graph for data analysis and saves the figure in a specified folder.

    Parameters
    ----------
    graphic_data : pd.Series
        Series with crime codes as the index and their corresponding quantities as values to be graphed.
    graphic_name : str
        Title of the graphic, which is used as the name of the file.
    gs : dict
        Visual settings of the graphic. 

    Returns
    -------
    None
        This function generates a .png file with the graphic.

    """
    fig = plt.figure()
    fig.patch.set_facecolor(gs["face_color"])
    plt.title(graphic_name)
    plt.xlabel(gs['x_name'])
    plt.ylabel(gs["y_name"])
    plt.yticks(range(-45000,45000, 5000))
    plt.xticks(xticks)
    graphic_data.plot.bar(color=np.where(graphic_data < 0, gs["f_color"], gs["m_color"]), edgecolor=gs["edge_color"])
    plt.grid(color='gray', linestyle='--', linewidth=0.5) 
    plt.savefig(f"{graphic_name}.png", dpi=gs["dpi"],bbox_inches='tight')
    plt.close()