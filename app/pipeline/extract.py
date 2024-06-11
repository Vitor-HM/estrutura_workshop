import os
import pandas as pd
import glob
from typing import List

def extract_excel(p_path) -> List[pd.DataFrame]:
    """
    Função para ler os arquivos de 
    uma pastas date/input e returna uma lista de dataframes

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """
    todos_arquivos = glob.glob(os.path.join(p_path, '*.xlsx')) #busca todos os arquivos excel do caminho que eu especificar
    data_frame_list = []
    for arquivo in todos_arquivos:
        data_frame_list.append(pd.read_excel(arquivo))
    
    return data_frame_list

if __name__ == "__main__":
     dataframe_list = extract_excel("data/input")
     print(dataframe_list)
