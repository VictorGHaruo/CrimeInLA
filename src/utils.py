import pandas as pd


file_path = "../data/Crime_Data_from_2020_to_Present.csv"

file = pd.read_csv(file_path, sep=",")

ctk = [3,5,6,9,10,13]
save_local = "../data"
file_name = "cleaned_dataset"

def preprocessing(file, ctk:list[int], save_local:str, file_name:str):
    
    """
    ctk -> colunas que continuarão no arquivo
    save_local -> local onde o arquivo preprocessado será salvo
    file_name -> nome do arquivo preprocessado

    ----Example----
    ctk = [1,2,3]
    save_local = "../data"
    file_name = "cleaned_dataset"
    """
    
    columns = file.columns.delete([ctk])

    new = file.drop(columns,axis= 1)
    save_local = f"{save_local}/{file_name}.csv"

    new.to_csv(save_local, sep= ",", index= False)

preprocessing(file, ctk, save_local,file_name)
