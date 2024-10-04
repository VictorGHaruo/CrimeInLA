"""
This module is responsible for cleaning the data for analysis in the project.

Functions
---------
groups(df ,xlabel ,ylabel ,restriction ) 
    Cria um Dataframe com o número de ocorrências de um crime por LAPD.

severity_lookup(df ,crm_cd ,colunm1 :,colunm2 )
    Função auxiliar que retorna a gravidade de um crime.

severity(df_groups , df_severity :,colunm1 ,colunm2 )
    Soma colunas cujos crimes possuem mesma gravidade e adiciona ao Dataframe principal

Examples
--------
    >>> import hip_one_data_treatment as hp
    >>> hp.groups(df,'Crm cd' ,'AREA NAME', 50000)
    >>> hp.severity_lookup(df,'510','Crime', 'Gravidade')
    >>> hp.severity(df, df_severity, 'Crime', 'Gravidade')


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

    df_grupos = df.groupby(xlabel)[ylabel].value_counts()

    df_newdata = pd.DataFrame(sorted(df[ylabel].unique()), columns=[ylabel])

    for crime in df[xlabel].unique():
        if df_grupos[crime].sum() > restriction and len(df_grupos[crime]) == 21:
            df_newdata[crime] = df_grupos[crime].sort_index(ascending=True).values

    return df_newdata

def severity_lookup(df : pd.DataFrame ,crm_cd : str ,colunm1 : str ,colunm2 : str) -> Union[str, None]:

    """
    Retorna a gravidade de um crime

    Parameters
    ----------
    df : pd.Dataframe
        Dataframe que contém as informações de gravidade de cada crime
    crm_cd : str
        Descrição do crime
    colunm1 : str
        Nome da coluna que contém a descrição de cada crime
    colunm2 : str
        Nome da coluna que contém a gravidade de cada crime

    Returns
    -------
    str ou None
        Gravidade do crime
        Retorna None se o crm_cd não estiver na base de dados
    
    """
    if crm_cd in df[colunm1].values:
        return df.loc[df[colunm1] == crm_cd, colunm2].values[0]
    else:
        return None  
    
def severity(df_groups : pd.DataFrame, df_severity : pd.DataFrame ,colunm1 : str ,colunm2 : str):

    """
    Soma as colunas cujos crimes apresentam a mesma gravidade a as adiciona no Dataframe principal 

    Parameters
    ----------
    df_groups : pd.Dataframe
        Dataframe que contém os dados dos crimes
    df_severity : str
        Dataframe que contém a gravidade de cada crime
    colunm1 : str
        Nome da coluna que contém a descrição de cada crime
    colunm2 : str
        Nome da coluna que contém a gravidade de cada crime
    
    """
     
    for groups in df_severity[colunm2].unique():

        group = np.zeros(len(df_groups))

        for crime in df_groups.columns:
            if severity_lookup(df_severity,crime,colunm1,colunm2) == groups:
                group += df_groups[crime]

        df_groups[groups] = group



