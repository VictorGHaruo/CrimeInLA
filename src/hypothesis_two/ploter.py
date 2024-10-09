'''
Module responsible for generating PNGs of crimes and years.

Functions
---------
png_year(df, path)
    Function that creates graphs for each year.
png_category(df, path)
    Function that creates graphs for each category.

Example
-------
>>> import ploter as pl
>>> pl.png_year(df, './')
>>> pl.png_category(df, '../../folder/')

'''

import pandas as pd
from matplotlib import pyplot as plt

def png_year(df: pd.DataFrame, path: str):
    '''
    Function that creates graphs for each year.
    
    Parameters
    ----------
    df: pd.DataFrame
        DataFrame with 'year' and 'category' columns.
    path: str
        Path where the PNG files will be saved.
    
    Example
    -------
    >>> df = pd.DataFrame({'year': [2, 1], 'category': [1, 2]})
    >>> png_year(df, './')
    '''
    
    comparison = df.groupby('year')['category'].value_counts().sort_index(ascending=False)
    
    for i in df['year'].unique():
        fig, ax = plt.subplots()
        comparison[i].plot.barh(color = 'darkcyan')
        
        fig.patch.set_facecolor('#1E182F')
        ax.set_facecolor('#1E182F')
        ax.tick_params(axis="x", colors="linen")
        ax.tick_params(axis="y", colors="linen")

        plt.ylabel('Crimes', color= "linen")
        plt.xlabel('Quantities', color= "linen")
        # n = comparison[i].max().astype(int)
        # if n != 0 and n//8 > 0 :
        #     plt.xticks(range(0, n, n//8))
        
        plt.title(i, color = "linen")
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        
        plt.savefig(f'{path}{i}.png', dpi= 300, bbox_inches='tight')
        plt.close()
        
def png_category(df: pd.DataFrame, path: str):
    '''
    Function that creates graphs for each category.
    
    Parameters
    ----------
    df: pd.DataFrame
        DataFrame with 'year' and 'category' columns.
    path: str
        Path where the PNG files will be saved.
    
    Example
    -------
    >>> df = pd.DataFrame({'year': [2, 1], 'category': [1, 2]})
    >>> png_category(df, './')
    '''
    
    comparison = df.groupby('category')['year'].value_counts().sort_index()
    
    for i in df['category'].unique():
        fig, ax = plt.subplots()
        comparison[i].plot.bar(color = 'darkcyan')
        
        fig.patch.set_facecolor('#1E182F')
        ax.set_facecolor('#1E182F')
        ax.tick_params(axis="x", colors="linen")
        ax.tick_params(axis="y", colors="linen")

        plt.xlabel('Year', color= "linen")
        plt.xticks(rotation=0)
        plt.ylabel('Quantities', color= "linen")
        # n = comparison[i].max().astype(int)
        # plt.yticks(range(0, n, n//8))
        
        plt.title(i, color = "linen")
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        
        plt.savefig(f'{path}{i}.png', dpi= 300, bbox_inches='tight')
        plt.close()