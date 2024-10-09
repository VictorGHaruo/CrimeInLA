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
    try:
        comparison = df.groupby('year')['category'].value_counts().sort_index(ascending=False)
    except KeyError:
        raise KeyError('png_year : DataFrame don\'t have the columns \"year\" and/or \"category\"' )
    except AttributeError:
        raise AttributeError("png_year : The passed argument \"df\" is not a dataframe")
    
    # Because 2024 has just 8 months of data
    comparison[2024] = comparison[2024].apply(lambda x: (x//8)*12)
    
    for i in df['year'].dropna().unique():
        
        fig, ax = plt.subplots()
        
        try:
            comparison[i].plot.barh(color = 'darkcyan')
        except KeyError:
            raise KeyError(f'png_year : The column \'year\' has some np.nan')
            
        fig.patch.set_facecolor('#1E182F')
        ax.set_facecolor('#1E182F')
        ax.tick_params(colors="linen")

        plt.ylabel('Crimes', color= "linen")
        plt.xlabel('Quantities', color= "linen")
        
        plt.title(i, color = "linen")
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        
        try:
            plt.savefig(f'{path}{i}.png', dpi= 600, bbox_inches='tight')
        except FileNotFoundError:
            raise FileNotFoundError(f'png_year : The path isn\'s corret, file not found')
            
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
    try:
        comparison = df.groupby('category')['year'].value_counts().sort_index()
    except KeyError:
        raise KeyError('png_category : DataFrame don\'t have the columns \"year\" and/or \"category\"' )
    except AttributeError:
        raise AttributeError("png_category : The passed argument \"df\" is not a dataframe")
    
    # Because 2024 has just 8 months of completed data
    for i in df['category'].unique():
        comparison.loc[i, 2024] = (comparison.loc[i, 2024] // 8) * 12
    
    for i in df['category'].dropna().unique():
        fig, ax = plt.subplots()
        comparison[i].plot.bar(color = 'darkcyan')
        
        fig.patch.set_facecolor('#1E182F')
        ax.set_facecolor('#1E182F')
        ax.tick_params(colors="linen")

        plt.xlabel('Year', color= "linen")
        plt.xticks(rotation=0)
        plt.ylabel('Quantities', color= "linen")
        
        plt.title(i, color = "linen")
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        
        try:
            # If the category is compost name, need to put to name1_name2.png
            if len(i.split()) == 1:
                plt.savefig(f'{path}{i}.png', dpi= 600, bbox_inches='tight')
            else:
                str = i.split()
                name = '_'.join(str)
                plt.savefig(f'{path}{name}.png', dpi= 600, bbox_inches='tight')
        except FileNotFoundError:
            raise FileNotFoundError(f'png_category : The path isn\'s corret, file not found')
        
        plt.close()