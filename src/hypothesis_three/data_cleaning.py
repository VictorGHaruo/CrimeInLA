"""
This module is responsible for cleaning the data for analysis in the project.

Functions
---------
rm_X(victim_sex)
    Auxiliary function that convert "X" to NaN, and everything else, return victim_sex.
remove_lines(df)
    Remove lines that disturbs the analysis, and saves the new dataframe in a .csv file.

Examples
--------
    >>> import data_cleaning as dc
    >>> dc.remove_lines(df)

Author
------
    Victor Iwamoto <vitinhogabrielharuo@.gmail.com>

License:
--------
    FGV License
"""

import pandas as pd
import numpy as np
from typing import Union

def rm_X(victim_sex: str)->Union[str, float]:
    """
    Auxiliary function that converts "X" to np.nan. 

    Parameters
    ----------
    victim_sex : str
        Gender in the cells of the "Vict Sex" column.

    Returns
    -------
    str or np.nan: np.nan for "X" or "H" or "-" and  return a str for anything else
    
    Examples
    --------
    >>> rm_X("M")
    "M"
    >>> rm_X("X")
    nan
    """

    if victim_sex == "X":
        return np.nan
    elif victim_sex == "H":
        return np.nan
    elif victim_sex == "-":
        return np.nan
    else:
        return victim_sex

def remove_lines(df: pd.DataFrame):
    """
    Transforms "X", "H" and "-" values in the "Vict Sex" column into empty cells, 
    removes all rows with np.nan in the "Vict Sex" column, and creates 
    a file named 'final_dataset.csv' containing the cleaned data.


    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to be cleaned.

    Returns
    -------
    None
        Generate a .csv file.

    """
    df["Vict Sex"] = df["Vict Sex"].apply(lambda victim_sex: rm_X(victim_sex))
    df = df.dropna()
    df.to_csv("data/final_dataset.csv", sep= ",", index= False)
