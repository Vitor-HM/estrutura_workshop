from typing import List

import pandas as pd


# Função para concatenar uma lista de data frames
def concatena_dataframe(p_dataframe_lista: List[pd.DataFrame]):
    """
    Recebo uma lista de dataframe sai um dataframe só

    args: p_dataframe_lista: List

    return pd.concat(p_dataframe_lista, ignore_index=True)
    """
    return pd.concat(p_dataframe_lista, ignore_index=True)
