"""
This module is responsible for cleaning the data for analysis in the project.

Functions
---------
groups(df ,xlabel ,ylabel ,restriction ) 
    Cria um Dataframe com o número de ocorrências de um crime por LAPD.

severity(df_groups , category)
    Soma colunas cujos crimes possuem mesma gravidade 

sum_columns(df)
    Soma as colunas que possuem somente valores numéricos.

Examples
--------
    >>> import hip_one_data_treatment as hp
    >>> hp.groups(df,'Crm cd' ,'AREA NAME', 50000)
    >>> hp.severity(df, 'low')
    >>> hp.sum_columns(df_Base)

Author
------
    Lucas Lima <luquinhasnm035@gmail.com>

License:
--------
    FGV License
"""

import numpy as np
import pandas as pd
from typing import Union

crime_severity = {
    110: "medium",
    113: "medium",
    121: "medium",
    122: "high",
    210: "high",
    220: "medium",
    230: "high",
    231: "high",
    235: "high",
    236: "medium",
    237: "high",
    250: "medium",
    251: "high",
    310: "low",
    320: "low",
    330: "low",
    331: "medium",
    341: "medium",
    343: "low",
    345: "medium",
    347: "high",
    349: "high",
    350: "high",
    351: "high",
    352: "high",
    353: "high",
    354: "high",
    410: "high",
    420: "high",
    421: "low",
    432: "high",
    433: "low",
    434: "medium",
    435: "high",
    436: "high",
    437: "high",
    438: "medium",
    439: "medium",
    440: "high",
    441: "medium",
    442: "high",
    443: "high",
    444: "medium",
    445: "low",
    446: "high",
    450: "low",
    451: "medium",
    452: "high",
    453: "high",
    470: "medium",
    471: "high",
    473: "medium",
    474: "medium",
    475: "medium",
    480: "high",
    485: "high",
    487: "high",
    510: "low",
    520: "high",
    522: "high",
    622: "low",
    623: "medium",
    624: "medium",
    625: "high",
    626: "high",
    627: "low",
    647: "high",
    648: "high",
    649: "medium",
    651: "high",
    652: "medium",
    653: "high",
    654: "high",
    660: "medium",
    661: "medium",
    662: "low",
    664: "medium",
    666: "medium",
    668: "low",
    670: "medium",
    740: "high",
    745: "high",
    753: "low",
    755: "high",
    756: "low",
    760: "high",
    761: "high",
    762: "high",
    763: "high",
    805: "medium",
    806: "medium",
    810: "high",
    812: "high",
    813: "medium",
    814: "low",
    815: "low",
    820: "high",
    821: "high",
    822: "medium",
    830: "medium",
    840: "high",
    845: "medium",
    850: "low",
    860: "medium",
    865: "high",
    870: "medium",
    880: "high",
    882: "medium",
    884: "medium",
    886: "medium",
    888: "high",
    890: "low",
    900: "low",
    901: "high",
    902: "low",
    903: "low",
    904: "low",
    906: "low",
    910: "high",
    920: "medium",
    921: "high",
    922: "high",
    924: "high",
    926: "high",
    928: "medium",
    930: "high",
    931: "high",
    932: "medium",
    933: "low",
    940: "medium",
    942: "high",
    943: "medium",
    944: "low",
    946: "high",
    948: "high",
    949: "medium",
    950: "high",
    951: "medium",
    954: "high",
    956: "medium"
}



def groups(df : pd.DataFrame ,xlabel : str ,ylabel : str , restriction : int) -> pd.DataFrame: 
    """
    Gera um novo Dataframe com nos dados do agrupamento de duas colunas

    Parameters
    ----------
    df : pd.Dataframe
        Dataframe que contém os dados originais
    xlabel : str
        Nome da coluna de df que contém os valores usados como base para agrupar o dataframe
    ylabel : str
        Nome da coluna de df que contém os valores que serão contados em cada grupo
    restriction : int
        Valor usado para filtrar colunas (dos dados agrupados) cuja soma dos valores seja menor que o mesmo 

    Returns
    -------

    pd.Dataframe
        Dataframe contendo o número de vezes que um valor de xlabel aparece junto de um ylabel em df
    """
    try:
        df_grupos = df.groupby(xlabel)[ylabel].value_counts()
    except KeyError:
        raise KeyError("Invalid key")
    
    df_newdata = pd.DataFrame(sorted(df[ylabel].unique()), columns=[ylabel])

    try:
        for crime in df[xlabel].unique():
            if df_grupos[crime].sum() > restriction and len(df_grupos[crime]) == len(df_newdata):
                df_newdata[crime] = df_grupos[crime].sort_index(ascending=True).values
    except TypeError:
        raise TypeError
        
    return df_newdata

def severity(df_groups : pd.DataFrame,category : str ,dict: dict = crime_severity) -> Union[pd.Series, None]:

    """
    Soma as colunas cujos crimes apresentam a gravidade passado como argumento

    Parameters
    ----------
    df_groups : pd.Dataframe
        Dataframe que contém os dados dos crimes
    category : str
        Gravidade do crime
    df_severity : str
    Dicionário que contém a gravidade de cada crime

    Returns
    -------
    pd.Series
        Serie contendo a soma das colunas   
        Return None se a categoria não estiver no dicionário 
    
    """

    group = np.zeros(len(df_groups))
    try: 

        if category not in dict.values():
            return None
    except TypeError:
        raise TypeError

    for crime in df_groups.columns:
        if dict.get(crime, None) == category:
            group += df_groups[crime]

    return group
def sum_columns(df : pd.DataFrame) -> Union[pd.Series, None]:

    """
    Soma as colunas de um Dataframe cujo todos os valores são numéricos

    Parameters
    ----------
    df : pd.Dataframe
        Dataframe que contém os dados.

    Returns
    -------
    pd.Series 
        Série com a soma de todas as colunas que continham valores numéricos.
        Return None se nenhuma coluna for somada.
    """
    try:
        sum = np.zeros(len(df))
    except TypeError:
        raise TypeError("Type of df has no len()")
    
    df_data_numeric = df.select_dtypes(include=['float64', 'int64'])

    for i in df_data_numeric.columns:
        sum += df_data_numeric[i]

    if sum.sum() == 0:
        return None
    

    return sum



