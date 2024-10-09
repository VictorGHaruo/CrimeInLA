import unittest
import pandas as pd
import numpy as np
import sys
import os
from pandas.testing import assert_frame_equal
sys.path.append(os.path.abspath('..'))
import src.hypothesis_three.data_cleaning as dc

# This module is responsable for testing the module "data_cleaning" from Hypothesis Three

class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        # Examples of Series and lists to be tested

        self.df = pd.DataFrame({
            "Vict Sex": ["M", "F", "X", "H", "-", "M", "F"],
            "Crm Cd" : [510, 624, 626, 120, 130, 131, 901]
        })

        # Expected results of the examples

        self.cleaned_df = pd.DataFrame({
            'Vict Sex': ["M", "F", "M", "F"],
            "Crm Cd" : [510, 624, 131, 901]
        })
        self.rm_x_df = pd.DataFrame({
            "Vict Sex": ["M", "F", np.nan, np.nan, np.nan, "M", "F"],
            "Crm Cd" : [510, 624, 626, 120, 130, 131, 901]
        }) 

    def test_remove_lines_file_creation(self):
        # Test remove lines, if the file is created when function runs

        file_path = "../data/rm_lines.csv"
        dc.remove_lines(self.df, file_path)
        self.assertTrue(os.path.exists(file_path), f"The file {file_path} must have been created.")
        if os.path.exists(file_path):
            os.remove(file_path)
    
    def test_remove_lines_wrong_path(self):
        # Test of fuction "remove_lines", test if it gives an error when using an invalid path
        
        file_path = "wrongpath/rm_lines.csv"
        self.assertRaises(FileNotFoundError, dc.remove_lines, self.df, file_path)

    def test_remove_lines_is_correct(self):
        # Test of fuction "remove_lines" if the output is correct
        
        file_path = "../data/rm_lines.csv"
        dc.remove_lines(self.df, file_path)
        rm_lines = pd.read_csv(file_path, sep= ",")
        assert_frame_equal(rm_lines, self.cleaned_df)
        os.remove(file_path)

    def test_rm_x(self):
        # Test of fuction "rm_X"

        for sex_number in range(self.df.shape[0]):
            self.df.loc[sex_number, "Vict Sex"] = dc.rm_X(self.df["Vict Sex"][sex_number])
        assert_frame_equal(self.df, self.rm_x_df)
            

if __name__ == '__main__':
    unittest.main()