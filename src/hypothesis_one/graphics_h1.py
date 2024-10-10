
"""
This module is responsible for generating and saving graphics for analysis in the project.

Functions
---------
plot_heatmap(df, ylabel, title, gs)
    Plota um gráfico de calor e salva localmente no formato png.
geo_heatmap(df, intensity, title, gs)
    Plota um mapa de calor geográfico.
plot_barh(data, ylabel, title, gs)
    Plota um gráfico de barras horizontal.

Examples
--------
    >>> import hip_one_graphics as hg
    >>> hg.plot_heatmap(df, 'AREA NAME', 'heatmap')
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
        Dicionário com configurções básicas do gráfossuem como crime mais ocorrente ico.

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

    plt.savefig(f"../../data/Crime_&_Location/{title}.png")
    plt.close()
    

graph_settings = {'figsize': (10, 8),                
    'cmap': 'summer',                            
    'legend': True,                    
    'alpha': 0.6,                      
    'edgecolor': 'black',               
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
    fig.patch.set_facecolor(gs.get('face_color','#1E182F'))
    ax.set_facecolor(gs.get('face_color', "#1E182F"))
    ax.set_axis_off()
    
    df.plot(
        column=intensity,                 
        cmap=gs['cmap'],                  
        legend=gs['legend'],              
        alpha=gs['alpha'],                
        edgecolor=gs['edgecolor'],        
        linewidth=gs['linewidth'],        
        ax=ax,                                             
    )

    plt.title(title, color = 'white')                    
    plt.savefig(f"../../data/Crime_&_Location/{title}.png")           
    plt.close()

barh_settings = {
    'figsize': (10, 7),          
    'color': 'skyblue',           
    'edgecolor': 'black',         
    'linewidth': 1,               
    'alpha': 0.8,                
    'title': 'Título do Gráfico', 
    'xlabel': None,          
    'ylabel': None ,           
    'fontsize': 12,              
    'grid': True,                 
    'grid_alpha': 0.5,            
    'grid_axis': 'x',             
    'bar_height': 0.7,            
    'face_color': "#1E182F",
    'font_color': 'white'     
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
    fig.patch.set_facecolor(gs.get('face_color','#1E182F'))

    ax.barh(
        ylabel, 
        data, 
        color=gs.get('color', 'skyble'), 
        edgecolor=gs.get('edgecolor', 'black'), 
        linewidth=gs.get('linewidth', 1), 
        alpha=gs.get('alpha', 0.8), 
        height=gs.get('bar_height', 0.7),
    )


    ax.set_title(gs.get('title', title), fontsize=gs.get('fontsize', 12))
    ax.set_xlabel(gs.get('xlabel', None), fontsize=gs.get('fontsize', 12))
    ax.set_ylabel(gs.get('ylabel', None), fontsize=gs.get('fontsize', 12))
    ax.set_facecolor(gs.get('face_color', "#1E182F"))
    
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.tick_params(axis='x', colors=gs.get('font_color','white'))  
    plt.tick_params(axis='y', colors= gs.get('font_color','white')) 


    if gs.get('grid', True):
        ax.grid(True, axis=gs.get('grid_axis', 'x'), alpha=gs.get('grid_alpha', 0.5))

    plt.title(title, color = gs.get('font_color', 'white'))                      
    plt.savefig(f"../../data/Crime_&_Location/{title}.png")           
    plt.close()
