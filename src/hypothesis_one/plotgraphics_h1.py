"""
This module is responsible for plotting the graphs used in the data analysis of hypothesis 1.

Functions
---------

plot_h1(df, df_map)
    Plots the graphs

Examples
--------

    >>> import plotgraphics as pg
    >>> pg.plot_h1(df, df_map) 

"""

import data_treatment_h1 as hp
import graphics_h1 as hg

def plot_h1(df_Base,df_map):

    """
    Plots a series of graphs

    Parameters
    ----------
    df : pd.DataFrame
        Original dataset
    df_map : gpd.GeoDataFrame
        Dataset used to plot the map of Los Angeles with the LAPD boundaries

    """


    df_grupos = hp.groups(df_Base, 'Crm Cd', 'AREA NAME', 0)
    df_heatmap = hp.groups(df_Base,'Crm Cd', 'AREA NAME', 50000)


    df_map['low'] = hp.severity(df_grupos, 'low' )
    df_map['medium']= hp.severity(df_grupos, 'medium' )
    df_map['high'] = hp.severity(df_grupos, 'high' )
    df_map['severity'] = df_map['low'] + 3*df_map['medium'] + 10*df_map['high']
    df_map['occorrencys'] = hp.sum_columns(df_grupos)

    hg.plot_heatmap(df_heatmap,'AREA NAME', 'Crimes_most_occorencys' )

    hg.plot_barh(df_map['occorrencys'], df_grupos['AREA NAME'], 'Crimes_Occorrencys')
    hg.geo_heatmap(df_map,'occorrencys', 'Crimes_Occorrencys_map')

    hg.plot_barh(df_map['severity'], df_grupos['AREA NAME'], 'Areas_severity')
    hg.geo_heatmap(df_map,'severity', 'Areas_severity_map')

    hg.plot_barh(df_map['low'], df_grupos['AREA NAME'], 'Low_Crimes')
    hg.geo_heatmap(df_map,'low', 'Low_Crimes_map')

    hg.plot_barh(df_map['medium'], df_grupos['AREA NAME'], 'Medium_Crimes')
    hg.geo_heatmap(df_map,'medium', 'Medium_Crimes_map')

    hg.plot_barh(df_map['high'], df_grupos['AREA NAME'], 'High_Crimes')
    hg.geo_heatmap(df_map,'high', 'High_Crimes_map')