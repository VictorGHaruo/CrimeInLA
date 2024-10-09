import unittest
import pandas as pd
import numpy as np
import sys
import os
from pandas.testing import assert_series_equal
sys.path.append(os.path.abspath(".."))
import src.hypothesis_three.data_treatment as dc

file_path = "../data/test.csv"

# This module is responsable for testing the module "data_treatment" from Hypothesis Three
# This test utilizes the "test.csv" as a short example to be tested, this file is at data folder

class TestDataTreatment(unittest.TestCase):
    def setUp(self):
        # Examples of Series and lists to be tested
        self.df_one = pd.Series({626 : 10,
                                 130 : 6,
                                 510 : 7,
                                 901 : 8
                                 })
        self.df_two = pd.Series({626 : 13,
                                 510 : 4,
                                 901 : 7,
                                 130 : 6
                                 })

        self.list_one = [626, 901, 510, 130]

        # Expected results of the examples
    
        self.result_aux = pd.Series({626 : 10,
                                     901 : 8,
                                     510 : 7,
                                     130 : 6
                                     })
        
        self.result_order_data = pd.Series({626 : -3,
                                            901 : 1,
                                            510 : 3,
                                            130 : 0
                                            })
        self.result_ranking_G = pd.Series({ 510 : -3,
                                            130 : 0,
                                            901 : 2,
                                            626 : -1

        })
        self.result_ranking_F = pd.Series({ 510 : -3,
                                            130 : 0,
                                            626 : -1,
                                            901 : 2

        })
        self.result_ranking_M = pd.Series({ 901 : 2,
                                            130 : 0,
                                            510 : -3,
                                            626 : -1

        })

    def test_aux(self):
        # Test of fuction "aux"

        assert_series_equal(dc.aux(self.list_one, self.df_one),self.result_aux)
        
    def test_order_data(self):
        # Test of fuction "order_data"

        assert_series_equal(dc.order_data(self.list_one, self.df_one, self.df_two, 4),self.result_order_data)

    def test_ranking_G(self):
        # Test of fuction "ranking" with mode= "G"

        df = pd.read_csv(file_path, sep= ",")
        gender = df.groupby("Vict Sex")
        assert_series_equal(dc.ranking(df, gender, "G", 4), self.result_ranking_G)

    def test_ranking_F(self):
        # Test of fuction "ranking" with mode= "F"

        df = pd.read_csv(file_path, sep= ",")
        gender = df.groupby("Vict Sex")
        assert_series_equal(dc.ranking(df, gender, "F", 4), self.result_ranking_F)
    
    def test_ranking_M(self):
        # Test of fuction "ranking" with mode= "M"

        df = pd.read_csv(file_path, sep= ",")
        gender = df.groupby("Vict Sex")
        assert_series_equal(dc.ranking(df, gender, "M", 4), self.result_ranking_M)

if __name__ == '__main__':
    unittest.main()