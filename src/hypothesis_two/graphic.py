import pandas as pd
from matplotlib import pyplot as plt

graph_settings = {"dpi": 1000,
                  "y_name": "Quantities",
                  "edge_color": "teal",
                  "face_color": "powderblue",
                  "f_color": "mediumturquoise",
                  "m_color": "cadetblue"
                  }

def save_png(df: pd.DataFrame, x: str, y:str, path: str, gs: dict = graph_settings):
    x_by_y = df.groupby(y)[x].value_counts().sort_index()
    
    for i in df[y].unique():
        
        fig, ax = plt.subplots()
        x_by_y[i].plot.bar(color = 'darkcyan')
        
        fig.patch.set_facecolor('blueviolet')
        ax.set_facecolor('lightgray')
        
        if y == 'DATE OCC':
            plt.xlabel('Crimes')
        else:
            plt.xlabel('Anos') 
        plt.ylabel('Quantities')
        n = x_by_y[i].max().astype(int)
        plt.yticks(range(0, n, n//8))
        
        plt.title(i)
        plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha = 0.3)
        
        plt.savefig(f'{path}/{i}.png', dpi= 300, bbox_inches='tight')
        plt.close()
    
    
    