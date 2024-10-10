"""
This module is responsible for generating and saving graphics for analysis in the project.

Functions
---------
plot_heatmap(df, ylabel, title, gs)
    Plots a heatmap and saves it locally in PNG format.
geo_heatmap(df, intensity, title, gs)
    Plots a geographic heatmap.
plot_barh(data, ylabel, title, gs)
    Plots a horizontal bar chart.

Examples
--------
    >>> import hip_one_graphics as hg
    >>> hg.plot_heatmap(df, 'AREA NAME', 'heatmap')
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
    'linewidths': 0.4,                 
    'linecolor': 'white',              
    'cbar': False,                      
    'square': False,                  
    'vmin': None,                      
    'vmax': None,                     
    'xticklabels': True,              
    'yticklabels': True,             
    'annot_kws': {                  
        'size': 10,                    
        'color': 'black'},
    'xtick_label_size': 8,          
    'xtick_label_color': 'linen',
    'ytick_label_size': 8,          
    'ytick_label_color': 'linen'
        }

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

heatmap_settings = {
    'figsize': (12, 12),              
    'cmap': 'Blues',              
    'annot': True,                     
    'fmt': 'd',                    
    'linewidths': 0.4,                
    'linecolor': 'white',             
    'cbar': False,                    
    'square': False,                  
    'vmin': None,                     
    'vmax': None,                    
    'xticklabels': True,              
    'yticklabels': True,             
    'annot_kws': {                   
        'size': 20,                   
        'color': 'gray'
    },
    'xtick_label_size': 15,        
    'xtick_label_color': 'linen',    
    'ytick_label_size': 15,        
    'ytick_label_color': 'linen', 
    'background_color': "#1E182F"    
}

def plot_heatmap(df: pd.DataFrame, ylabel: str, title: str, gs: dict = heatmap_settings):
    """
    Creates a heatmap for data analysis.

    Parameters
    ----------
    df: pd.DataFrame
        DataFrame containing the data for the plot.
    ylabel : str
        Name of the column whose values represent the y-axis of the plot.
    title : str
        Title of the plot.
    gs : dict
        Dictionary with basic settings for the plot.

    Returns
    -------
    None
        This function generates a .png file with the graphic.
    """

    df_data_numeric = df.select_dtypes(include=['float64', 'int64'])
    
    fig, ax = plt.subplots(figsize=gs['figsize'])
    fig.patch.set_facecolor(gs.get('face_color','#1E182F'))
    ax.set_facecolor(gs['background_color'])  

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
        annot_kws=gs['annot_kws'],
        ax=ax                  
    )

    plt.title(title)
    
    plt.xticks(fontsize=gs['xtick_label_size'], color=gs['xtick_label_color'])
    plt.yticks(fontsize=gs['ytick_label_size'], color=gs['ytick_label_color'])

    plt.savefig(f"data/Crime_&_Location/{title}.png")
    plt.close()

    

graph_settings = { 
    'figsize': (8, 8),                
    'cmap': 'Blues',                            
    'legend': True,                    
    'alpha': 0.6,                      
    'edgecolor': 'black',               
    'linewidth': 0.5,                  
    'scheme': 'quantiles',
    'xtick_label_size': 15,        
    'xtick_label_color': 'linen',
    'face_color': '#1E182F',  
    'legend_font_size': 12,  
    'legend_orientation': 'horizontal',
    'legend_font_color': 'linen', 
    'legend_orientation': 'horizontal'
    }
          
def geo_heatmap(df: gpd.GeoDataFrame, intensity: str, title: str, gs: dict = graph_settings):
    """
    Generates a geographic heatmap.

    Parameters
    ----------
    df : gpd.GeoDataFrame
        GeoDataFrame containing the data for the map.
    intensity : str
        Name of the column in df that contains the data used as the basis for the heatmap.
    title : str
        Title of the plot.
    gs : dict
        Default graphic settings.

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
        scheme="quantiles",              
        cmap=gs['cmap'],                  
        legend=gs['legend'],              
        alpha=gs['alpha'],                
        edgecolor=gs['edgecolor'],        
        linewidth=gs['linewidth'],        
        ax=ax,  
        missing_kwds={'color': 'lightgrey'}                                           
    )

    legend = ax.get_legend()
    if legend:
        legend.set_bbox_to_anchor((0, 0))  
        legend._legend_box.align = "right"

    plt.title(title, color='linen', fontsize=16)                   
    plt.savefig(f"data/Crime_&_Location/{title}.png")           
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
    'font_color': 'linen'     
}

def plot_barh(data: pd.Series, ylabel: pd.Series, title: str, gs: dict = barh_settings):
    """
    Function to plot a horizontal bar chart with custom settings.

    Parameters
    ----------
    data : pd.Series
        Series containing the data (values) for the X-axis.
    xlabel : pd.Series
        Series containing the labels for the Y-axis.
    title : str
        Title of the plot.
    gs : dict
        Dictionary with optional graphic settings.
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
    plt.savefig(f"data/Crime_&_Location/{title}.png")           
    plt.close()