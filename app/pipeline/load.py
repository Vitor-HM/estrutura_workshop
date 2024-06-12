import pandas as pd
import os

"""
receber um dataframe e salvar em excel

args: 
p_dataframe: pd.DataFrame, dataframe que vai ser salvo em excel
p_local_gravacao: str, caminho onde quer salvar
p_nome_arquivo: str, nome do arquivo 

return arquivo salvo com sucesso
"""

def carrega_excel(p_dataframe: pd.DataFrame, p_local_gravacao: str, p_nome_arquivo: str):
    """
    receber um dataframe e salvar em excel

    args: 
    p_dataframe: pd.DataFrame, dataframe que vai ser salvo em excel
    p_local_gravacao: str, caminho onde quer salvar
    p_nome_arquivo: str, nome do arquivo 

    return arquivo salvo com sucesso
    """
    if not os.path.exists(p_local_gravacao):
        os.mkdir(p_local_gravacao)
    p_dataframe.to_excel(f"{p_local_gravacao}/{p_nome_arquivo}.xlsx", index=False)
    return "Arquivo salvo com sucesso"

