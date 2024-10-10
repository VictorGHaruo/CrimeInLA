import unittest
import pandas as pd
import sys
import os
import pandas.testing as pt
import numpy as np

#Criando os arquivos que serão usados para checar as repostas das funções
test = [
    [1, 'A', 'a', .2],
    [2, 'B', 'b', .4],
    [3, 'C', 'c', .2],
    [4, 'D', 'd', .8],
    [5, 'E', 'e', .2]
]

test2 =   [
    [1, 'A', 'a', .2],
    [2, 'B', 'b', .4],
    [4, 'D', 'd', .8],
]

test3 = [
    [1, 2, 3, 4   ],
    [2, 4, 6, 8   ],
    [3, 6, 9, 12  ],
    [4, 8, 12, 16 ],
    [5, 10, 15, 20]
]    

test4 = [
    [1, '2', '3', '4'   ],
    ['2', 4, '6', '8'   ],
    ['3', '6', 9, '12'  ],
    ['4', '8', 12, '16' ],
    ['5', '10', '15', 20]
] 


df_test = pd.DataFrame(test, columns=['ID', 'LETTER', 'letter', 'float'])
df_test2 = pd.DataFrame(test2, columns=['ID', 'LETTER', 'letter', 'float'])
df_test3 = pd.DataFrame(test3, columns=[110, 510, 330, 884])
df_test4 = pd.DataFrame(test4, columns=['A', 'B', 'B', 'D'])

df_r1 = pd.DataFrame(df_test['letter'])
df_r2 = pd.DataFrame(df_test2['float'])
r3 = (df_test3[510] + df_test3[330])/1.0
df_r3 = pd.Series(r3, index = (0,1,2,3,4), name = 510)
r4 = (df_test3[110] + df_test3[510] + df_test3[330] + df_test3[884])/1.0  
df_r4 = pd.Series(r4, index = (0,1,2,3,4), name = 110)
r5 = (df_test['ID'] + df_test['float'])/1.0 
df_r5 = pd.Series(r5, index = (0,1,2,3,4), name = 'ID')

sys.path.append(os.path.abspath('..'))
import src.hypothesis_one.data_treatment_h1 as h1

#Testes da função groups

class testGroups (unittest.TestCase):
    # testando a groups() quando não há repetições.

    def test_unique_groups(self):
        pt.assert_frame_equal(h1.groups(df_test, 'LETTER', 'letter', 0), df_r1)

    # testando a groups quando há repetições.

    def test_not_unique_groups(self):
        pt.assert_frame_equal(h1.groups(df_test, 'LETTER', 'float', 0), df_r2)

    # testando a groups() com "restriction" > 0.

    def test_restriction_groups(self):
        pt.assert_frame_equal(h1.groups(df_test, 'LETTER', 'float', 10), df_r2)

    # testando a groups() quando é passado uma chave inválida.

    def test_not_key_groups(self):
        with self.assertRaises(KeyError):
            h1.groups(df_test, 'Letter', 'float', 0)

    # testando a groups() quando "restriction" não é um número.

    def test_not_key_groups(self):
        with self.assertRaises(TypeError):
            h1.groups(df_test, 'LETTER', 'float', "a")

# Testes da função severity()

class testSeverity (unittest.TestCase):

    # testando com uma valor que está no dicionário

    def test_in_dict_severity(self):
        pt.assert_series_equal(h1.severity(df_test3,'low'), df_r3)

    # testando com um valor que não está no dicionário

    def test_out_dict_severity(self):
        self.assertIsNone(h1.severity(df_test3, 'LOW'), None)

    # testando quando é passado um não dicionário no terceiro argumento

    def test_fake_dict(self):
        with self.assertRaises(TypeError):
            h1.groups(df_test3, 'low', 'a')

#Testes da função sum_columns()

class test_Sum_columns ( unittest.TestCase):

    # Testando quando toda) no caso ideals as colunas são formadas por números

    def test_sum_columns(self):
        pt.assert_series_equal(h1.sum_columns(df_test3), df_r4)

    # Testando quando há colunas sem números

    def test_have_letters(self):
        pt.assert_series_equal(h1.sum_columns(df_test), df_r5)

    # Testando quando há colunas com números e não números

    def test_number_and_non_numbers(self):
        self.assertIsNone(h1.sum_columns(df_test4), None)
        

if __name__ == '__main__':
    unittest.main()
