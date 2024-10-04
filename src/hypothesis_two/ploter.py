import pandas as pd
from matplotlib import pyplot as plt

def save_png(df: pd.DataFrame, by:str, comp: str, path: str):
    '''
    Função que cria o gráfico da quantidade de crimes para dois modos, por ano ou por crime.
    Já fazendo o ano de 2024 como a média anual.
    
    Parametros
    ----------
    df: pd.DataFrame
        Data frame cujo o numero de casos está
    by; str
        Nome da coluna do modo que vai ser serapado os gráficos
    comp: str
        Nome da coluna que vai ser comparada
    path: str
        Caminho para onde salvar a png
    
    Exemplo
    -------
    >>> df = np.DataFrame({'a': [2], 'b': [1]})
    >>> save_png(df, 'a', 'b', './')
    
    '''
    
    comparison = df.groupby(by)[comp].value_counts().sort_index()
    
    if by == 'DATE OCC':
        comparison[2024] = comparison[2024].apply(lambda x: (x*12)//8)
    
    for i in df[by].unique():
        
        if by == 'category':
            n = comparison.loc[(i, 2024)]
            comparison.loc[(i,2024)] = (n * 12)//8
        
        fig, ax = plt.subplots()
        comparison[i].plot.bar(color = 'darkcyan')
        
        fig.patch.set_facecolor('blueviolet')
        ax.set_facecolor('lightgray')
        
        if by == 'DATE OCC':
            plt.xlabel('Crimes')
        else:
            plt.xlabel('Year') 
        plt.ylabel('Quantities')
        n = comparison[i].max().astype(int)
        plt.yticks(range(0, n, n//8))
        
        plt.title(i)
        plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha = 0.3)
        
        plt.savefig(f'{path}{i}.png', dpi= 300, bbox_inches='tight')
        plt.close()
    
    
    