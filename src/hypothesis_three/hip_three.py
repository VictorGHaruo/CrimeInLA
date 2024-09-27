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
def ranking(file, gender, mode):
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
        diference = aux(g_list,m_crimes) - aux(g_list,f_crimes)
        return g_list, diference.to_list()
    elif mode == "M":
        diference = aux(m_list,m_crimes) - aux(m_list,f_crimes)
        return m_list, diference.to_list()
    else:
        diference = aux(f_list,m_list) - aux(f_list,f_list)
        return f_list, diference.to_list()


def aux(crime_list, freq_list):
    num_crimes = []
    for code in crime_list:
        if code not in freq_list:
            num_crimes.append(0)
        else:
            num_crimes.append(int(freq_list[code]))
    return pd.Series(num_crimes)

m,n = ranking(file,gender, "G")


