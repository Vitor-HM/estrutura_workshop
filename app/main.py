import os

from pipeline.extract import extract_excel
from pipeline.load import carrega_excel
from pipeline.transform import concatena_dataframe

if __name__ == '__main__':
    dataframe_list = extract_excel('data/input')
    df = concatena_dataframe(dataframe_list)
    carrega_excel(df, 'data/output', 'output')
