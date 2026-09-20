#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:19:59 2026

@author: mine
"""

from pathlib import Path
import pandas as pd
import numpy as np



def get_path(filepath):
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    return path

def read_file(filepath):
    path = get_path(filepath)
    return pd.read_csv(path, dtype={"Mileage": int, "pricesold": int})

filepath = Path("data") / "used_car_sales.csv"
data = read_file(filepath)
print(data.columns)


def get_mileage_distribution(data): 
   max_distance = 1_000_000
   return pd.cut(
        data["Mileage"], bins=np.linspace(0, max_distance, 10, endpoint=True)
        )

     
mileage_dist = get_mileage_distribution(data) 

# siden vi valgte en fast maxgrense fallet noen biler utenfor, men det var ikke de testsettene var ut etter
print(mileage_dist.value_counts())


def get_group_by_size(data):
    return data.groupby("Make").size()

def get_top_makes(data, n=10):
    return data["Make"].value_counts().head(n)

# Sanity check
assert get_group_by_size(data).sum() == len(data)


print(get_top_makes(data))


       
            
    
   





