import unittest
import pandas as pd
import sys
import os
from pandas.testing import assert_frame_equal

sys.path.append(os.path.abspath('..'))
import src.hypothesis_two.categorizer as ct

class testPloter (unittest.TestCase):
    
    def test_Others_aux_category(self):
        self.assertEqual(ct.aux_category(200), 'Others')
        
    def test_Assaults_aux_category(self):
        self.assertEqual(ct.aux_category(231), 'Assaults')
        
    def test_negative_aux_category(self):
        self.assertEqual(ct.aux_category(-200), 'Others')
        
    def test_category(self):
        testin_df = pd.DataFrame({'cod': [100, 120, 121, 745, 872, 190, 999, 320]})
        expeted_df = pd.DataFrame({'cod': [100, 120, 121, 745, 872, 190, 999, 320], 'category':['Others', 'Others', 'Rape', 'Possession of Weapons or Drugs', 'Others', 'Others', 'Others', 'Burglary']})
        assert_frame_equal(ct.category(testin_df, 'cod'), expeted_df)
    
    def test_date_to_year(self):
        testin_df = pd.DataFrame({'Date': ['00/00/0000 00:00:00 AM', '11/11/1111 11:11:11 PM']})
        expeted_df = pd.DataFrame({'day': [00, 11], 'month': [00, 11], 'year': [0000, 1111]})
        assert_frame_equal(ct.date_to_year(testin_df, 'Date'), expeted_df)
    
    
if __name__ == '__main__':
    unittest.main()