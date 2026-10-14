#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on ...

@author: ...

"""

from pathlib import Path
import pandas as pd

FILEPATH = "hjerte_ekg_data.csv"


def get_path(filepath):
    path = Path(filepath)
    if not path.is_file():         
        raise FileNotFoundError(f"File not found: {path.resolve()}")
    return path

def read_file(filepath):
    path = get_path(filepath)
    return pd.read_csv(path) 

def count_rows(df):
    return len(df.index)


def count_unique(df, column):
    values = df[column].dropna()      
    unique_values = values.unique()   
    return len(unique_values)

    
if __name__ == "__main__": 
    df = read_file(FILEPATH) 
    num_rows = count_rows(df)
    print(f"Number of rows: {num_rows}")
    num_patients = count_unique(df, "pasient_id")
    print(f"Number of unique patients: {num_patients}")
    #print(df.head()) 
    #df.info()
   

    
    
   






