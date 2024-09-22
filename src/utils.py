import pandas as pd

file_path = "../data/dataset.CSV"

file = pd.read_csv(file_path, sep=";")


"""
ctk -> colunas que continuarão no arquivo
save_local -> local onde o arquivo preprocessado será salvo
file_name -> nome do arquivo preprocessado

----Example----
ctk = [1,2,3]
save_local = "../data"
file_name = "cleaned_dataset"
"""

ctk = [8,9,12]
save_local = "../data"
file_name = "cleaned_dataset"

def preprocessing(file, ctk:list[int], save_local:str, file_name:str):
    columns = file.columns.delete([ctk])
    new = file.drop(columns,axis= 1)
    save_local = save_local + "/" + file_name + ".csv"

    new.to_csv(save_local, sep= ";", index= False)

preprocessing(file, ctk, save_local,file_name)
