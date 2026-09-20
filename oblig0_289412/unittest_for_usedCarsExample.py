#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:02:55 2026

@author: mine

unittest for usedCarsExample - used AI to help and learn to write the test
"""

import unittest
from pathlib import Path
import pandas as pd
from usedCarsExample import get_path, get_mileage_distribution


class TestGetPath(unittest.TestCase):

    def test_returns_path_when_file_exists(self):
        # Lag en midlertidig fil
        Path("used_car_sales.csv").write_text("test", encoding="utf-8")
        result = get_path("used_car_sales.csv")
        self.assertIsInstance(result, Path)

    def test_raises_when_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            get_path("no_pathname.csv")
            
            
class TestGetMileageDistributaion(unittest.TestCase):       
    
    # kjører automatisk før hver test og lager testdata på nytt
    def setUp(self):
        # Lag en liten testdataframe i stedet for å laste hele CSV-en
        self.data = pd.DataFrame({"Mileage": [0, 50_000, 100_000, 500_000, 1_000_000]})
     
    # sjekker om riktig type bli returnert
    # kan sjekke det i terminal med type(result)
    def test_returns_categorical(self):
        result = get_mileage_distribution(self.data, max_distance=1_000_000)
        self.assertIsInstance(result,pd.Categorical)
    
    def test_correct_number_og_bins(self):
        result = get_mileage_distribution(self.data, max_distance=1_000_000)
        # 10 bins - 9 intervaller
        # bilene blir delt inn i "grupper" (bins)
        self.assertEqual(len(result.categories), 9)
    
    # sjekker at ingen gyldige verdier forsvinner/ havner utenfor binsene og blir NaN
    # siden pd.cut setter verdier utenfor rekkevide til NaN og hvis max_distance er for lav vil noe bil faller ut
    def test_no_nulls_for_vallid_data(self):
        # testdatene er kjentnog innenfor 0 - 1M
        result = get_mileage_distribution(self.data, max_distance=1_000_000)
        self.assertFalse(result.isna().any)
    
    
    
            
if __name__ == "__main__":
    unittest.main()