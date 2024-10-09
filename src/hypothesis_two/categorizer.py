'''
This module is responsible for extra data cleaning for hypothesis 2, 
which involves transforming the date into a year and adding a category 
for each crime.

Functions
---------

date_to_year(df, column)
    Takes the column of the dataframe in the format "XX/XX/XXXX 00:00:00 XM" 
    and returns only the year.

aux_category(code, crimes)
    Auxiliary function that, given a crime code, returns its category.

category(df)
    Function responsible for adding the 'category' column to the dataframe.

Examples
--------

>>> import categorizer as ctg
>>> df_dated = ctg.date_to_year(df, 'Date')
>>> crime_type = ctg.aux_category(2, crimes)
>>> ctg.category(df)
'''

import pandas as pd

def date_to_year(df: pd.DataFrame, column: str) -> pd.DataFrame:
    '''
    Extracts the day, month, and year from a column in the format "dd/mm/yyyy 00:00:00 XM".
        
    Parameters
    ----------
    df: pd.DataFrame
        DataFrame with a column in the format "dd/mm/yyyy 00:00:00 XM".
    column: str
        Name of the column with this format.
    
    Returns
    -------
    pd.DataFrame
        DataFrame without the passed column, but with 3 new ones: 'day', 'month', and 'year'.
    
    Example
    -------
    >>> df = pd.DataFrame({'Date': ['26/11/2004 08:00:00 PM', '10/10/2024 07:00:00 AM']})
    >>> df_clean = date_to_year(df, 'Date')
    >>> print(df_clean)
        day  month  year
    0   26      11  2004
    1   10      10  2024
    '''
    
    df_new = df.copy()
    df_new['day'] = df_new[column].str.split('[ /]').str[0].astype(int)
    df_new['month'] = df_new[column].str.split('[ /]').str[1].astype(int)
    df_new['year'] = df_new[column].str.split('[ /]').str[2].astype(int)
    df_new = df_new.drop(column, axis=1)
    return df_new

crimes = {
    "Homicides": [110, 113],
    "Rape": [121, 122, 237, 815, 820, 821, 890],
    "Robbery": [210, 220, 850],
    "Assaults": [230, 231, 235, 236, 245, 250, 251, 354, 626, 668, 761, 860, 926],
    "Burglary": [310, 320, 812],
    "Car Theft": [330, 331, 410, 420, 421, 433, 510, 520, 624, 625, 946],
    "Personal Theft": [350, 351, 352, 353, 450, 451, 452, 453],
    "Property Theft": [341, 343, 345, 440, 441, 442, 443, 444, 445, 470, 471, 472, 
                       473, 474, 475, 480, 485, 487, 491, 649, 662, 740, 946],
    "Traffic Incidents": [901, 903, 956],
    "Possession of Weapons or Drugs": [745, 753, 886],
    "Disappearance": [627, 940]
}
    
def aux_category(cod: int, crimes: dict = crimes) -> str:
    '''
    Returns the crime type based on the code.
    
    Parameters
    ----------
    code: int
        Crime code.
    crimes: dict
        Dictionary with crime categorization (by default, the one provided by the dataset).
    
    Returns
    -------
    str
        Name of the category according to the crime, or 'Others' if not in the dictionary.  
        
    Example
    -------
    >>> crimes = { 'Robbery': [1, 2], 'Homicide': [3, 4]}
    >>> crime_type = aux_category(2, crimes)
    >>> print(crime_type)
    Robbery
    >>> crime_type = aux_category(4, crimes)
    >>> print(crime_type)
    Homicide
    >>> crime_type = aux_category(5, crimes)
    >>> print(crime_type)
    Others
    '''
    
    for cate, nums in crimes.items():
        if cod in nums:
            return cate
    return "Others"

def category (df: pd.DataFrame, column: str) -> pd.DataFrame:
    '''
    Function responsible for creating the 'category' column, using the auxiliary function 
    aux_category for each row.
    
    Parameters
    ----------
    df: pd.DataFrame
        DataFrame with the specified column from which the function will create the new column.
    column: str
        Name of the column containing the codes.
    
    Returns
    -------
    pd.DataFrame
        DataFrame with an additional 'category' column.
    
    Example
    -------
    >>> df = pd.DataFrame({'victim': ['A', 'B'], 'codes': [100, 745]})
    >>> df_with_category = category(df, 'codes')
      victim  codes                        category
    0      A    100                          Others
    1      B    745  Possession of Weapons or Drugs
    '''
    
    df['category'] = df[column].apply(lambda x: aux_category(x))
    return df
    