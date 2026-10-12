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

    
if __name__ == "__main__": 
    df = read_file(FILEPATH) 
    num_rows = count_rows(df)
    print(f"Number of rows: {num_rows}")
    #print(df.head()) 
    #df.info()
   

    
    
   






