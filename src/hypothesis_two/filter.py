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

crimes = {
    "homicidios": [110, 113],
    "estupro": [121, 122, 815, 820, 821, 237, 890],
    "roubo": [210, 220, 850],
    "agressoes": [230, 231, 235, 236, 250, 251, 761, 926, 354, 245, 668, 860, 626],
    "invasão": [310, 320, 812],
    "roubo de carro": [510, 520, 433, 330, 331, 410, 420, 421, 624, 625, 946],
    "furto pessoal": [350, 351, 352, 353, 450, 451, 452, 453],
    "furtos propiedade": [341, 343, 345, 440, 441, 442, 443, 444, 445, 470, 471, 472,
                          473, 474, 475, 480, 485, 487, 491, 740, 946, 662, 649],
    "incidentes de trânsito": [901, 903, 956],
    "posse de arma ou drogas" : [745, 753, 886],
    "desaparecimento" : [627, 940]
}

def categoria(cod, crimes: dict):
    for cate, nums in crimes.items():
        if cod in nums:
            return cate
    return "OUTROS"


df_cleaned = date_to_year(df, 'DATE OCC')
df_cleaned = df_cleaned[['DATE OCC', 'Crm Cd']]
df_cleaned['categoria'] = df_cleaned['Crm Cd'].apply(lambda x: categoria(x, crimes))
df_cleaned.to_csv("../../data/hip_two.csv")