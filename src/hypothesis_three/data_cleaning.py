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
import os
from typing import Union

def rm_X(victim_sex: str)->Union[str, float]:
    """
    Auxiliary function that converts everything different from "F" or "M" to np.nan. 

    Parameters
    ----------
    victim_sex : str
        Gender in the cells of the "Vict Sex" column.

    Returns
    -------
    str or np.nan: return a str for "F" and "M" and np.nan for anything else 
    
    Examples
    --------
    >>> rm_X("M")
    "M"
    >>> rm_X("X")
    nan
    """

    if victim_sex == "M" or victim_sex == "F":
        return victim_sex
    else:
        return np.nan

def remove_lines(df: pd.DataFrame, file_path: str):
    """
    Transforms every value different of "F" or "M" in the "Vict Sex" column into empty cells, 
    removes all rows with np.nan in the "Vict Sex" column, and creates 
    a file named 'final_dataset.csv' containing the cleaned data.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to be cleaned.
    file_path : str
        Path to save the file

    Returns
    -------
    None
        Generate a .csv file.

    """

    df["Vict Sex"] = df["Vict Sex"].apply(lambda victim_sex: rm_X(victim_sex))
    df = df.dropna()
    
    directory = os.path.dirname(file_path)

    if os.path.exists(directory) == False:
        raise FileNotFoundError()

    df.to_csv(file_path, sep= ",", index= False)