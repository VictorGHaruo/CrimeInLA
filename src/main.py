"""
This module is responsible for generating and saving graphics for analysis in the project.

Functions
---------
plot_graphic(graphic_data, graphic_name, gs)
    Plots the graphic and saves it in the data folder. The "gs" parameter contains default settings
    for the graphic's appearance.

Examples
--------
    >>> import graphic as gp
    >>> gp.plot_graphic(series, "My graphic")

Author
------
    Victor Iwamoto <vitinhogabrielharuo@gmail.com>

License:
--------
    FGV License
"""

import pandas as pd
# main.py
import src.hypothesis_three.data_cleaning as dc
import src.hypothesis_three.data_treatment as dt
import src.hypothesis_three.graphic as gp


def main ():
    df = pd.read_csv('data/cleaned_dataset.csv', sep= ",")
    dc.remove_lines(df)
    new_df = pd.read_csv("data/final_dataset.csv", sep= ",")
    gender = new_df.groupby("Vict Sex")

    #Data Treatment
    general_analysis = dt.ranking(new_df,gender, "G", 20)
    female_analysis = dt.ranking(new_df,gender, "F", 20)
    men_analysis = dt.ranking(new_df,gender, "M", 20)
    mc_analysis = dt.ranking(new_df,gender, "MC", 20)

    # #Plot graphic
    gp.plot_graphic(general_analysis, "GeneralCrimes")
    gp.plot_graphic(men_analysis, "MenCrimes")
    gp.plot_graphic(female_analysis, "FemaleCrimes")
    gp.plot_graphic(mc_analysis, "MostCommon")
if __name__ == "__main__":
    main()