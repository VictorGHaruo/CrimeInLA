import unittest
import pandas as pd
import sys
import os
import pandas.testing as pt
import numpy as np

# Creating the files that will be used to check the function responses
test = [
    [1, 'A', 'a', .2],
    [2, 'B', 'b', .4],
    [3, 'C', 'c', .2],
    [4, 'D', 'd', .8],
    [5, 'E', 'e', .2]
]

test2 = [
    [1, 'A', 'a', .2],
    [2, 'B', 'b', .4],
    [4, 'D', 'd', .8],
]

test3 = [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [3, 6, 9, 12],
    [4, 8, 12, 16],
    [5, 10, 15, 20]
]

test4 = [
    [1, '2', '3', '4'],
    ['2', 4, '6', '8'],
    ['3', '6', 9, '12'],
    ['4', '8', 12, '16'],
    ['5', '10', '15', 20]
]

df_test = pd.DataFrame(test, columns=['ID', 'LETTER', 'letter', 'float'])
df_test2 = pd.DataFrame(test2, columns=['ID', 'LETTER', 'letter', 'float'])
df_test3 = pd.DataFrame(test3, columns=[110, 510, 330, 884])
df_test4 = pd.DataFrame(test4, columns=['A', 'B', 'B', 'D'])

df_r1 = pd.DataFrame(df_test['letter'])
df_r2 = pd.DataFrame(df_test2['float'])
r3 = (df_test3[510] + df_test3[330]) / 1.0
df_r3 = pd.Series(r3, index=(0, 1, 2, 3, 4), name=510)
r4 = (df_test3[110] + df_test3[510] + df_test3[330] + df_test3[884]) / 1.0  
df_r4 = pd.Series(r4, index=(0, 1, 2, 3, 4), name=110)
r5 = (df_test['ID'] + df_test['float']) / 1.0 
df_r5 = pd.Series(r5, index=(0, 1, 2, 3, 4), name='ID')

sys.path.append(os.path.abspath('..'))
import src.hypothesis_one.data_treatment_h1 as h1

# Tests for the groups function

class testGroups(unittest.TestCase):
    # Testing the groups() function when there are no repetitions.

    def test_unique_groups(self):
        pt.assert_frame_equal(h1.groups(df_test, 'LETTER', 'letter', 0), df_r1)

    # Testing the groups() function when there are repetitions.

    def test_not_unique_groups(self):
        pt.assert_frame_equal(h1.groups(df_test, 'LETTER', 'float', 0), df_r2)

    # Testing the groups() function with "restriction" > 0.

    def test_restriction_groups(self):
        pt.assert_frame_equal(h1.groups(df_test, 'LETTER', 'float', 10), df_r2)

    # Testing the groups() function when an invalid key is passed.

    def test_not_key_groups(self):
        with self.assertRaises(KeyError):
            h1.groups(df_test, 'Letter', 'float', 0)

    # Testing the groups() function when "restriction" is not a number.

    def test_not_key_groups(self):
        with self.assertRaises(TypeError):
            h1.groups(df_test, 'LETTER', 'float', "a")

# Tests for the severity() function

class testSeverity(unittest.TestCase):

    # Testing with a value that is in the dictionary

    def test_in_dict_severity(self):
        pt.assert_series_equal(h1.severity(df_test3, 'low'), df_r3)

    # Testing with a value that is not in the dictionary

    def test_out_dict_severity(self):
        self.assertIsNone(h1.severity(df_test3, 'LOW'), None)

    # Testing when a non-dictionary is passed as the third argument

    def test_fake_dict(self):
        with self.assertRaises(TypeError):
            h1.groups(df_test3, 'low', 'a')

# Tests for the sum_columns() function

class test_Sum_columns(unittest.TestCase):

    # Testing when ideally all columns are formed by numbers

    def test_sum_columns(self):
        pt.assert_series_equal(h1.sum_columns(df_test3), df_r4)

    # Testing when there are columns without numbers

    def test_have_letters(self):
        pt.assert_series_equal(h1.sum_columns(df_test), df_r5)

    # Testing when there are columns with numbers and non-numbers

    def test_number_and_non_numbers(self):
        self.assertIsNone(h1.sum_columns(df_test4), None)

if __name__ == '__main__':
    unittest.main()
