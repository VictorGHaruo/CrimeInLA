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
    num_crimes = pd.Series(num_crimes)
    num_crimes = num_crimes.set_axis(crime_list)
    return num_crimes

def order_data(crime_list, m_crimes, f_crimes, size):
    diference = aux(crime_list,m_crimes) - aux(crime_list,f_crimes)
    diference = diference.iloc[np.r_[0:size]]
    return diference

def plot_graphic(graphic_data, graphic_name, gs: dict):
    fig = plt.figure()
    fig.patch.set_facecolor(gs["face_color"])
    plt.title(graphic_name)
    plt.xlabel(gs["x_name"])
    plt.ylabel(gs["y_name"])
    plt.yticks(range(-30000, 30000, 5000))
    graphic_data.plot.bar(color=np.where(graphic_data < 0, gs["f_color"], gs["m_color"]), edgecolor=gs["edge_color"])
    plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Adiciona uma grade mais visível 
    #plt.show()
    plt.savefig(f"{graphic_name}.png", dpi=gs["dpi"],bbox_inches='tight')
    plt.close()






graph_settings = {"dpi": 1000,
                  "x_name": "Crime Code",
                  "y_name": "Quantities",
                  "edge_color": "teal",
                  "face_color": "powderblue",
                  "f_color": "mediumturquoise",
                  "m_color": "cadetblue"

                 
                  
                  
                  
                  }


general_analysis = ranking(file,gender, "G", 20)
female_analysis = ranking(file,gender, "F", 20)
men_analysis = ranking(file,gender, "M", 20)



plot_graphic(general_analysis, "General Crimes", graph_settings)
plot_graphic(men_analysis, "Men Crimes", graph_settings)
plot_graphic(female_analysis, "Female Crimes", graph_settings)
