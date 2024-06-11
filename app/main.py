import os
from pipeline.extract import extract_excel


if __name__ == "__main__":
     dataframe_list = extract_excel("data/input")
     print(dataframe_list)
