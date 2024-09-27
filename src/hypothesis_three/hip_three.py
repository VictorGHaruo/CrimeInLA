import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Funções uteis

file = pd.read_csv("../../data/cleaned_dataset.csv", sep= ",")

def aux(sex):
    if sex == "X":
        return np.nan
    else:
        return sex

def remove_lines(file):
    file["Vict Sex"] = file["Vict Sex"].apply(lambda sex: aux(sex))
    file = file.dropna()
    file.to_csv("teste.csv", sep= ",", index= False)

'''

file = pd.read_csv("teste.csv", sep= ",")

#Ranking Geral


gender = file.groupby("Vict Sex")
def ranking(file, gender, mode, graphic_size):
    #frequencia de crimes para homem e mulher em ordem 
    m_crimes = gender.get_group("M").value_counts("Crm Cd")
    f_crimes = gender.get_group("F").value_counts("Crm Cd")

    number_rank_crimes = []

    #Lista com os crime codes organizados por ordem de quantidade
    #os maiores crimes em relaçao a x
    g_list = file.value_counts("Crm Cd").index.to_list()
    m_list = m_crimes.index.to_list()
    f_list = f_crimes.index.to_list()
    
    if mode == "G":
        graphic = order_data(g_list,m_crimes,f_crimes, graphic_size)
        return graphic
    elif mode == "M":
        graphic = order_data(m_list,m_crimes,f_crimes, graphic_size)
        return graphic
    elif mode == "F":
        graphic = order_data(f_list,m_crimes,f_crimes, graphic_size)
        return graphic
    else:
        print(f"Mode{mode} doesnt exist")


def aux(crime_list, freq_list):
    num_crimes = []
    for code in crime_list:
        if code not in freq_list:
            num_crimes.append(0)
        else:
            num_crimes.append(int(freq_list[code]))
    return pd.Series(num_crimes)

def order_data(crime_list, m_crimes, f_crimes, size):
    diference = aux(crime_list,m_crimes) - aux(crime_list,f_crimes)
    diference = diference.set_axis(crime_list)
    diference = diference.sort_values(inplace=False)
    diference = diference.iloc[np.r_[0:size/2, -size/2:0]]
    return diference

def plot_graph(graphic_data, graphic_name, gs:dict):



    graphic_name = f"{graphic_name}.png"
    plt.title("Teste")
    plt.xlabel(gs["x_name"])
    plt.ylabel(gs["y_name"])
    plt.yticks(range(-30000, 30000, 5000))
    graphic_data.plot.bar(color = "mediumturquoise", edgecolor = gs["edge_color"])
    plt.savefig(graphic_name, dpi=gs["dpi"])




m= ranking(file,gender, "G", 20)



graph_settings = {"dpi": 1080,
                  "x_name": "Crime Code",
                  "y_name": "Quantities",
                  "edge_color": "teal",
                  "color": (0.2, # redness
                            0.4, # greenness
                            0.2, # blueness
                            0.6 # transparency
                            )
                 
                  
                  
                  
                  }



plot_graph(m, "teste", graph_settings)


