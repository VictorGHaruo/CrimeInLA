import pandas as pd
import data_cleaning as dc
import data_treatment as dt
import graphic as gp

df = pd.read_csv("../../data/cleaned_dataset.csv", sep= ",")

dc.remove_lines(df)

new_df = pd.read_csv("../../data/final_dataset.csv", sep= ",")

gender = new_df.groupby("Vict Sex")

#Data Treatment
general_analysis = dt.ranking(new_df,gender, "G", 20)
female_analysis = dt.ranking(new_df,gender, "F", 20)
men_analysis = dt.ranking(new_df,gender, "M", 20)

#Plot graphic
gp.plot_graphic(general_analysis, "General Crimes")
gp.plot_graphic(men_analysis, "Men Crimes")
gp.plot_graphic(female_analysis, "Female Crimes")
