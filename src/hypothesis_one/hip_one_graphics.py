
"""
This module is responsible for generating and saving graphics for analysis in the project.

Functions
---------
plot_heatmap(df, ylabel, title, gs)
    Plota um gráfico de calor e salva localmente no formato png.
point_map(df,LAT, LON , maps, title, gs)
    Plota uma mapa sobreposto por pontos em coordenadas específicas.
geo_heatmap(df, intensity, title, gs)
    Plota um mapa de calor geográfico.
plot_barh(data, ylabel, title, gs)
    Plota um gráfico de barras horizontal.

Examples
--------
    >>> import hip_one_graphics as hg
    >>> hg.plot_heatmap(df, 'AREA NAME', 'heatmap')
    >>> hg.ponit_map(df,'LAT','LON','Local_map.geosjon' , 'LA_map')
    >>> hg.geo_heatmap(df, 'crimes', 'La_map')
    >>> hg.plot_barh(df, df['name'], 'graph')

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

heatmap_settings = {'figsize': (21, 21),              
    'cmap': 'Purples',              
    'annot': True,                     
    'fmt': 'd',                    
    'linewidths': 0.5,                 
    'linecolor': 'white',              
    'cbar': True,                      
    'square': False,                  
    'vmin': None,                      
    'vmax': None,                     
    'xticklabels': True,              
    'yticklabels': True,             
    'annot_kws': {                  
        'size': 10,                    
        'color': 'black'}
        }

def plot_heatmap(df : pd.DataFrame ,ylabel : str ,title : str, gs : dict = heatmap_settings):
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
    gs : dict
        Dicionário com configurções básicas do gráfico.

    Returns
    -------
    None
        This function generates a .png file with the graphic.
    """
    df_data_numeric = df.select_dtypes(include=['float64', 'int64'])
        
    sns.heatmap(
        df_data_numeric,
        annot=gs['annot'],                           
        fmt=gs['fmt'],                               
        cmap=gs['cmap'],                            
        linewidths=gs['linewidths'],                 
        linecolor=gs['linecolor'],                 
        cbar=gs['cbar'],                                                
        square=gs['square'],                         
        vmin=gs['vmin'],                           
        vmax=gs['vmax'],                            
        xticklabels=gs['xticklabels'],               
        yticklabels=df[ylabel] if gs['yticklabels'] else False,  
        annot_kws=gs['annot_kws']                   
    )

    plt.title(title)

    plt.savefig(f'{title}.png')
    plt.close()
    

point_config = {
    'figsize': (12, 8),
    'marker': 'o',      
    'markersize': 10,   
    'color': 'blue',     
    'edgecolor': 'black',
    'linewidth': 0.5,    
    'alpha': 0.6,        
    'legend': True,      
    'categorical': True, 
    }

def point_map(df : pd.DataFrame ,LAT : str ,LON : str ,maps : str ,title : str, gs : dict = point_config):

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
    maps : str
        Endereço do arquivo que contém os dados do mapa.
    title : str
        Título do gráfico.
    gs : dict
        Dicionário com configurações básicas para os pontos.
    Returns
    -------
    None
        This function generates a .png file with the graphic.
    """
    
    df_coordinates = df[[LON,LAT]].copy()

    df_coordinates = df_coordinates[(df_coordinates[LON] != 0) & (df_coordinates[LAT] != 0)]

    map = gpd.read_file(maps)

    geometry = gpd.points_from_xy(df_coordinates[LON], df_coordinates[LAT])
    geo_df = gpd.GeoDataFrame(df_coordinates ,geometry= geometry )

    fig, ax = plt.subplots(figsize=gs.get('figsize', (12, 8)))
    ax.set_aspect('equal')

    map.plot(ax=ax, color='lightgrey', edgecolor='black') 

    geo_df.plot(
        ax=ax, 
        marker=gs.get('marker', 'o'), 
        color=gs.get('color', 'blue'), 
        markersize=gs.get('markersize', 10), 
        edgecolor=gs.get('edgecolor', 'black'), 
        linewidth=gs.get('linewidth', 0.5), 
        alpha=gs.get('alpha', 0.6),
        label='Coordinates'
    )

    plt.title(title)
    plt.savefig(f"{title}.png", dpi=300, bbox_inches='tight')
    plt.close()

graph_settings = {'figsize': (10, 8),                
    'cmap': 'YlOrRd',                  
    'column': 'intensidade',           
    'legend': True,                    
    'alpha': 0.6,                      
    'edgecolor': 'none',               
    'linewidth': 0.5,                  
    'scheme': 'quantiles'}
          
def geo_heatmap(df: gpd.GeoDataFrame, intensity: str, title: str, gs: dict = graph_settings):
    """
    Gera um mapa de calor geográfico

    Parameters
    ----------
    df : gpd.GeoDataFramee
        GeoDataFrame que contém os dados do mapa
    intensity : str
        Nome da coluna de df que contém os dados usados como base para o mapa de calor
    title : str
        Nome do gráfico
    gs : dict
        Configuração gráfica padrão.

    Returns
    -------
    None
        This function generates a .png file with the graphic.

    """

    fig, ax = plt.subplots(figsize=gs['figsize'])
    ax.set_aspect('equal')
    
    df.plot(
        column=intensity,                 
        cmap=gs['cmap'],                  
        legend=gs['legend'],              
        alpha=gs['alpha'],                
        edgecolor=gs['edgecolor'],        
        linewidth=gs['linewidth'],        
        ax=ax,                                             
    )

    plt.title(title)                      
    plt.savefig(f"{title}.png")           
    plt.close()

graph_settings = {"dpi": 1000,
                  "x_name": "Crime Code",
                  "y_name": "Quantities",
                  "edge_color": "teal",
                  "face_color": "powderblue",
                  "f_color": "mediumturquoise",
                  "m_color": "cadetblue"
                  }

barh_settings = {
    'figsize': (10, 7),          
    'color': 'blue',           
    'edgecolor': 'black',         
    'linewidth': 1,               
    'alpha': 0.8,                
    'title': 'Título do Gráfico', 
    'xlabel': 'Eixo X',          
    'ylabel': 'Eixo Y',           
    'fontsize': 12,              
    'grid': True,                 
    'grid_alpha': 0.5,            
    'grid_axis': 'x',             
    'bar_height': 0.7,            
    'label_color': 'darkblue'     
}

def plot_barh(data: pd.Series, ylabel: pd.Series, title: str, gs: dict = barh_settings):
    """
    Função para plotar gráfico de barras horizontal com configurações personalizadas.

    Parameters
    ----------
    data : pd.Series
        Série com os dados (valores) para o eixo X.
    xlabel : pd.Series
        Série com os rótulos do eixo Y.
    title : str
        Título do gráfico.
    gs : dict
        Dicionário com configurações gráficas opcionais.
    """

    fig, ax = plt.subplots(figsize=gs.get('figsize', (10, 7)))

    ax.barh(
        ylabel, 
        data, 
        color=gs.get('color', 'maroon'), 
        edgecolor=gs.get('edgecolor', 'black'), 
        linewidth=gs.get('linewidth', 1), 
        alpha=gs.get('alpha', 0.8), 
        height=gs.get('bar_height', 0.7)
    )

    ax.set_title(gs.get('title', title), fontsize=gs.get('fontsize', 12))
    ax.set_xlabel(gs.get('xlabel', 'Eixo X'), fontsize=gs.get('fontsize', 12))
    ax.set_ylabel(gs.get('ylabel', 'Eixo Y'), fontsize=gs.get('fontsize', 12))

    if gs.get('grid', True):
        ax.grid(True, axis=gs.get('grid_axis', 'x'), alpha=gs.get('grid_alpha', 0.5))

    plt.title(title)                      
    plt.savefig(f"{title}.png")           
    plt.close()
