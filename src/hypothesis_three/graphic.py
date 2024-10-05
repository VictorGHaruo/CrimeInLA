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
import numpy as np
import matplotlib.pyplot as plt
import os

graph_settings = {"dpi": 1000,
                  "x_name": "Crime Code",
                  "y_name": "Quantities",
                  "edge_color": "teal",
                  "face_color": "powderblue",
                  "f_color": "mediumturquoise",
                  "m_color": "cadetblue"
                  }

def plot_graphic(graphic_data: pd.Series , graphic_name: str, gs: dict = graph_settings):
    """
    Creates a bar graph for data analysis and saves the figure in a specified folder.

    Parameters
    ----------
    graphic_data : pd.Series
        Series with crime codes as the index and their corresponding quantities as values to be graphed.
    graphic_name : str
        Title of the graphic, which is used as the name of the file.
    gs : dict
        Visual settings of the graphic. 

    Returns
    -------
    None
        This function generates a .png file with the graphic.

    """
    fig = plt.figure()
    fig.patch.set_facecolor(gs["face_color"])
    plt.title(graphic_name)
    plt.xlabel(gs["x_name"])
    plt.ylabel(gs["y_name"])
    plt.yticks(range(-45000,45000, 5000))
    try:
        graphic_data.plot.bar(color=np.where(graphic_data < 0, gs["f_color"], gs["m_color"]), edgecolor=gs["edge_color"])
    except TypeError:
        exit("Graphic Data isn't a pd.Series")
    except ValueError:
        exit("Can't plot graphic with this data type")
    except Exception as error:
        exit(f"inesperate error: {error}")
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    try:
        path_save = f"data/gender_and_crime/graphics/{graphic_name}.png"
        plt.savefig(path_save, dpi=gs["dpi"],bbox_inches='tight')
    except FileNotFoundError:
        #Criar diretório usar os
        exit(f"The directory {path_save} doesn't exist.")
    except PermissionError:
        exit(f"The program doesn't have enough permission to save in the {path_save} folder")
    
    plt.close()
