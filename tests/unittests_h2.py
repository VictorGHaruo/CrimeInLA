import unittest
import numpy as np
import pandas as pd
import sys
import os
from pandas.testing import assert_frame_equal

sys.path.append(os.path.abspath('..'))
import src.hypothesis_two.categorizer as ct

class testPloter (unittest.TestCase):
    
    def test_Others_aux_category(self):
        # Testing generic number
        self.assertEqual(ct.aux_category(200), 'Others')
        
    def test_Assaults_aux_category(self):
        # Testing especific number
        self.assertEqual(ct.aux_category(231), 'Assaults')
        
    def test_negative_aux_category(self):
        # Testing what happen number is negative
        self.assertEqual(ct.aux_category(-200), 'Others')
        
    def test_category(self):
        # Testing with the cod being a np.nan or str
        testin_df = pd.DataFrame({'cod': [np.nan, "nada", 121, 745, 872, 190, 999, 320]})
        expeted_df = pd.DataFrame({'cod': [np.nan, "nada", 121, 745, 872, 190, 999, 320], 'category':['Others', 'Others', 'Rape', 'Possession of Weapons or Drugs', 'Others', 'Others', 'Others', 'Burglary']})
        assert_frame_equal(ct.category(testin_df, 'cod'), expeted_df)
    
    def test_date_to_year(self):
        # Testing the correct way
        testin_df = pd.DataFrame({'Date': ['00/00/0000 00:00:00 AM', '11/11/1111 11:11:11 PM']})
        expeted_df = pd.DataFrame({'day': [00, 11], 'month': [00, 11], 'year': [0000, 1111]})
        assert_frame_equal(ct.date_to_year(testin_df, 'Date'), expeted_df)
    
    def test_wrong_date_to_year(self):
        # Testing the wrong way
        testin_df = pd.DataFrame({'Date': ['00/00', '11/11 PM']})
        with self.assertRaises(ValueError):
            ct.date_to_year(testin_df, 'Date')
    
    
if __name__ == '__main__':
    unittest.main()