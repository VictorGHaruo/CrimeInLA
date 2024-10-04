import pandas as pd

crimes = {
    "Homicidios": [110, 113],
    "Estupro": [121, 122, 815, 820, 821, 237, 890],
    "Roubo": [210, 220, 850],
    "Agressões": [230, 231, 235, 236, 250, 251, 761, 926, 354, 245, 668, 860, 626],
    "Invasão": [310, 320, 812],
    "Roubo de carro": [510, 520, 433, 330, 331, 410, 420, 421, 624, 625, 946],
    "Furto pessoal": [350, 351, 352, 353, 450, 451, 452, 453],
    "Furtos propiedade": [341, 343, 345, 440, 441, 442, 443, 444, 445, 470, 471, 472,
                            473, 474, 475, 480, 485, 487, 491, 740, 946, 662, 649],
    "Incidentes de trânsito": [901, 903, 956],
    "Posse de arma ou drogas" : [745, 753, 886],
    "Desaparecimento" : [627, 940]
}
    
def category(cod: int, crimes: dict = crimes) -> str:
    
    '''
    Retorna o tipo de crime baseado no código 'Crm Cd'
    
    Parametros
    ----------
    cod: int
        Código do crime
    crimes: dict
        Dicionario com a categorização dos crimes (Por padrão o passado pelo site do dataset)
        
    Exemplo
    -------
    >>> crimes = { 'assalto' : [1, 2], 'homicido' : [3, 4]}
    >>> tipo_crime = categoria(2, crimes)
    >>> print(tipo_crime)
    assalto
    >>> tipo_crime = categoria(4, crimes)
    >>> print(tipo_crime)
    homicido
    
    '''
    
    
    for cate, nums in crimes.items():
        if cod in nums:
            return cate
    return "Outros"

def add_category (df: pd.DataFrame) -> pd.DataFrame:
    df['category'] = df['Crm Cd'].apply(lambda x: category(x))
    return df
    