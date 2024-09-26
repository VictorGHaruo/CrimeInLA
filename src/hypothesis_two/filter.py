import pandas as pd

df = pd.read_csv("../../data/Crime_Data_from_2020_to_Present.csv")

def date_to_year(df: pd.DataFrame, colum: str) -> pd.DataFrame:
    '''
    Extrai o ano da coluna no formato "dd/mm/aaaa 00:00:00 XM"
    
    Parametros
    ----------
    df: pd.DataFrame
        DataFrame com coluna com formato "dd/mm/aaaa 00:00:00 XM"
    colum: str
        Nome da coluna com essa formatação
    
    Exemplo
    -------
    >>> df = pd.DataFrame({'Date': ['26/11/2004 08:00:00 PM', '10/10/2024 07:00:00 AM']})
    >>> df_clean = date_to_year(df, ['Date'])
    >>> print(df_clean)
        Date
    0   2004
    1   2024
    
    '''
    
    df_new = df.copy()
    df_new[colum] = df_new[colum].str.split('[ /]').str[2].astype(int)
    return df_new

df_cleaned = date_to_year(df, 'DATE OCC')
df_cleaned = df_cleaned[['DATE OCC', 'Crm Cd']]
df_cleaned.to_csv("../../data/hip_two.csv")
print(df_cleaned)