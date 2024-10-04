import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import hip_one_data_treatment as hp 
import hip_one_graphics as hg

filepath = "reductdata.csv"

Base = pd.read_csv(filepath)
df_Base = pd.DataFrame(Base)

filepath2 = 'severity.xlsx'
severity = pd.read_excel(filepath2)
df_severity = pd.DataFrame(severity)

df_grupos = df_Base.groupby("Crm Cd")["AREA NAME"].value_counts()

df_newdata = pd.DataFrame(sorted(df_Base["AREA NAME"].unique()), columns=["AREA NAME"])


# Retiramos os crimes que não aparecem em todas as cidades
for crime in df_Base['Crm Cd'].unique():
    if len(df_grupos[crime]) == 21:
        df_newdata[crime] = df_grupos[crime].sort_index(ascending=True).values

df_newdata = hp.groups(df_Base,'Crm Cd', 'AREA NAME', 0)
    
hp.severity(df_newdata, df_severity, "Crime", "Gravidade")

hg.plot_graphic(df_newdata['A'], 'al', df_newdata['AREA NAME'])
    
exit()

def crime_graphbar(crime,areas,data):

    plt.bar(data[areas], data[crime] , edgecolor='black')
    plt.title(crime)
    plt.savefig(f'{crime}.png')
    plt.close()

#crime_graphbar('low', "AREA NAME", df_newdata)
#crime_graphbar('medium', "AREA NAME", df_newdata)
#crime_graphbar('high', "AREA NAME", df_newdata)
#crime_graphbar('all', "AREA NAME", df_newdata)


def crime_heatmap(data):

    df_data_numeric = data.select_dtypes(include=['float64', 'int64'])

    plt.figure(figsize = (9,21))
    df_coordinates = df_coordinates[(df_coordinates['LON'] != 0) & (df_coordinates['LAT'] != 0)]
    sns.heatmap(df_data_numeric,annot = True, fmt = "d", cmap = "coolwarm",yticklabels = data['AREA NAME'])

    plt.title("Crimes")
    plt.xlabel("Crimes")
    plt.ylabel("Areas")

    plt.savefig('crimes.png')

#crime_heatmap(df_newdata)

df_coordinates = df_Base[['LON','LAT']]

df_coordinates = df_coordinates[(df_coordinates['LON'] != 0) & (df_coordinates['LAT'] != 0)]

# Load the GeoDataFrame with your map data
LA_map = gpd.read_file('Stormwater_Capture_Master_Plan_(SCMP)_Priority_Infiltration_Areas.geojson')

# Create a GeoDataFrame for your coordinates
geometry = gpd.points_from_xy(df_coordinates['LON'], df_coordinates['LAT'])
geo_df = gpd.GeoDataFrame(df_coordinates ,geometry= geometry )

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(35, 35))  # Consider a smaller figure size for better visibility
ax.set_aspect('equal')

# Plot the LA map and the points
LA_map.plot(ax=ax, color='lightgrey', edgecolor='black')  # Customize the map color
geo_df.plot(ax=ax, color='red', markersize=50, label='Coordinates')  # Customize points
# Add a legend
ax.legend("No legend")

# Save the plot to a file
plt.savefig("LA_map.png", dpi=300, bbox_inches='tight')


