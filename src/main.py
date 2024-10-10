"""
This module is responsible for generating and saving graphics for analysis in the project.

Author
------
    Eric Manoel <dekribeiro7@gmail.com>
    Lucas Menezes <luquinhasnm035@gmail.com>
    Victor Iwamoto <vitinhogabrielharuo@gmail.com>

License:
--------
    FGV License
"""
# Because the shpinx's error
import sys
import os 

sys.path.append(os.path.abspath('..'))

import pandas as pd
import geopandas as gpd

import src.hypothesis_one.plotgraphics_h1 as pg

import src.hypothesis_two.categorizer as ctg
import src.hypothesis_two.ploter as ptr

import src.hypothesis_three.data_cleaning as dc
import src.hypothesis_three.data_treatment as dt
import src.hypothesis_three.graphic as gp


def main ():

    try:
        
        df = pd.read_csv("data/Crime_Data_from_2020_to_Present.csv") 
        df = df[['DATE OCC', 'Crm Cd', 'Vict Sex', 'AREA NAME']]
        df = ctg.date_to_year(df, 'DATE OCC')
        df = ctg.category(df, 'Crm Cd')
        dc.remove_lines(df, "data/final_dataset.csv")

        df_final = pd.read_csv("data/final_dataset.csv", sep= ",")
        
    except FileNotFoundError:
        exit("file not found, verify the path folder")
    except Exception as error:
        exit(f"inesperate error: {error}")


    ## Hipothessis_One

    map = gpd.read_file('data/LAPD_Division_1980236667069515482.zip')
    df_map = gpd.GeoDataFrame(map).sort_values(by = ['APREC'], ascending = True)

    pg.plot_h1(df_final, df_map)
    
    ## Hypothesis_Two

    ptr.png_year(df_final, 'data/pandemic/')
    ptr.png_category(df_final, 'data/pandemic/')

    ## Hypothesis_Three
    
    gender = df_final.groupby("Vict Sex")

    #Data Treatment
    general_analysis = dt.ranking(df_final,gender, "G", 20)
    female_analysis = dt.ranking(df_final,gender, "F", 20)
    men_analysis = dt.ranking(df_final,gender, "M", 20)
    mc_analysis = dt.ranking(df_final,gender, "MC", 20)

    #Plot graphic
    gp.plot_graphic(general_analysis, "GeneralCrimes")
    gp.plot_graphic(men_analysis, "MenCrimes")
    gp.plot_graphic(female_analysis, "FemaleCrimes")
    gp.plot_graphic(mc_analysis, "MostCommon")

if __name__ == "__main__":
    main()