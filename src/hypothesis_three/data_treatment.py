"""
This module is responsible for cleaning the data for analysis in the project.

Functions
---------
ranking(df, gender_group, mode, graphic_size)
    The main function of this module, use the others functions to prepare the data to be plotted.

aux(crime_list, freq_serie)
    Order the occurrence in the same order of crime_list.

order_data(crime_list, m_crimes, f_crimes, size)
    Calculates the difference between crimes committed against women and men.

Examples
--------
    >>> import data_cleaning as dc
    >>> dc.ranking(df, gender_group, "M", 20)
    >>> dc.aux(crime_list, freq_serie)
    >>> dc.order_data(crime_list, m_crimes, f_crimes, 20)


Author
------
    Victor Iwamoto <vitinhogabrielharuo@gmail.com>

License:
--------
    FGV License
"""

import pandas as pd
import numpy as np
from typing import Union

def ranking(df: pd.DataFrame, gender_group: pd.DataFrame, mode: str, graphic_size: int) -> Union[pd.Series, None]:

    """
    Prepares the data for graphing by converting it into a Series.

    Parameters
    ----------
    df : pd.DataFrame
        Data to be analyzed.
    gender_group : pd.DataFrame
        Groups separated by gender.
    mode : str
        Choose the parameters for data analysis. If "G" is selected, 
        the function will use the top graphic_size most frequently occurred 
        crimes in general and compare the differences in crimes committed 
        against women and men. For "F," it does the same but focuses on the 
        most occurred crimes against women, and for "M," it focuses on those against men. 
        For "MC", it does the 10 most common crimes against women and men. 
    graphic_size : int
        How many lines will be used for comparison.

    Returns
    -------
    pd.Series or None
        Data prepared for plotting, as a Series with quantities of crimes occurred as values and crime codes as the index.
        Returns None if the mode is invalid.
    """


    # frequency of the crimes against women and men in order by value
    m_crimes = gender_group.get_group("M").value_counts("Crm Cd")
    f_crimes = gender_group.get_group("F").value_counts("Crm Cd")

    #list with the crime codes organized by quantities, most common crimes by x_list
    #x can be f (female), g (general) or m (men)
    g_list = df.value_counts("Crm Cd").index.to_list()
    m_list = m_crimes.index.to_list()
    f_list = f_crimes.index.to_list()
    
    if mode == "G":
        graphic = order_data(g_list,m_crimes,f_crimes, graphic_size)

        return graphic
    elif mode == "M":
        graphic = order_data(m_list,m_crimes,f_crimes, graphic_size)
        return graphic
    elif mode == "F":
        graphic = order_data(f_list,m_crimes,f_crimes, graphic_size)
        return graphic
    elif mode == "MC":
        m_crimes = m_crimes.iloc[np.r_[0:int(graphic_size/2)]]
        f_crimes = f_crimes.iloc[np.r_[0:int(graphic_size/2)]] * (-1)
        f_crimes.sort_values(ascending=False, inplace=True)
        graphic = pd.concat([m_crimes, f_crimes],axis= 0)

        return graphic

    else:
        print(f"Mode{mode} doesn't exist")


def aux(crime_list: list, freq_serie: pd.Series) -> pd.Series:
    """
    Orders the quantities of occurrences in the order specified by the crime_list.

    Parameters
    ----------
    crime_list : list
        List with all crimes in decreasing order of the quantities of occurrence.
    freq_serie : pd.Series
        Series with how many crimes occurred in values and the code crime in index ordered by values.

    Returns
    -------
    pd.Series
        Occurrences ordered according to the crime_list.

    """
    num_crimes = []
    for code in crime_list:
        if code not in freq_serie:
            num_crimes.append(0)
        else:
            num_crimes.append(int(freq_serie[code]))
    num_crimes = pd.Series(num_crimes)
    num_crimes = num_crimes.set_axis(crime_list)
    return num_crimes

def order_data(crime_list: list, m_crimes: pd.Series, f_crimes: pd.Series, size: int) -> pd.Series:
    """
    Calculates the difference in crimes committed against women and men, taking the first 
    "size" elements of the `pd.Series`.

    Parameters
    ----------
    crime_list : list
        List with all crimes in decreasing order of the quantities of occurrence.
    m_crimes : pd.Series
        Series with how many crimes occurred with men in values and the code crime in index.
    f_crimes : pd.Series
        Series with how many crimes occurred with women in values and the code crime in index.
    size : int
        How many columns it will be considered when plotting the graphic.    

    Returns
    -------
    pd.Series
        Difference in the number of crimes committed against men and women, indexed by crime code.
    """
        
    difference = aux(crime_list,m_crimes) - aux(crime_list,f_crimes)
    difference = difference.iloc[np.r_[0:size]]
    return difference
