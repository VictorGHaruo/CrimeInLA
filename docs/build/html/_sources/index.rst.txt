.. f documentation master file, created by
   sphinx-quickstart on Sat Sep 28 19:23:15 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Crime in Los Angeles - Data Analysis
====================================
by Victor Iwamoto, Eric Ribeiro and Lucas Menezes.

Introduction
------------

During the development of the project, all members remained consistently active, as evidenced by the commits made. 
Each member was responsible for creating their specific functions, developing unit tests, and writing the analyses 
for the hypotheses.

In the graphic design aspect, Victor Iwamoto took charge of creating an aesthetic identity for Sphinx and the graphs, 
ensuring visual standardization and harmony. Overall, there was full participation from the members in organizing the 
project modules and in creating the documentation with Sphinx.

Hypothesis
----------
* Gender & Crimes by Victor Iwamoto
* Pandemic by Eric Ribeiro
* Location & Crimes by Lucas Menezes

Challenges
----------

* The dataset was incomplete and, at times, even incorrect. Therefore, it was necessary to use data treatment methods 
  to ensure that problematic information would not negatively influence the proposed analysis.

* The use of Sphinx presented a challenge when trying to document the main function, as Sphinx was generating generic 
  errors — without much description — when executing the make html command. Consequently, it required research to 
  understand the cause of the error.

* The implementation of libraries was also challenging. Initially, the main file and auxiliary modules were in the 
  same folder, which caused severe errors when using the command for automatic documentation 
  `sphinx-apidoc -o <output_dir> <source_dir>`. Thus, it was necessary to create a subdirectory for the libraries and include 
  an `__init__.py`` file to clarify to Python that this subdirectory is a library. As a result, when the main file changed its 
  directory, the import of libraries had to be done using absolute paths, because using relative paths caused errors in 
  Sphinx’s autodocumentation.

Documentation
-------------
.. code-block:: text

    CrimeInLA/
    ├── src/                  
    │   ├── main.py                               #Main source code
    │   ├── hypothesis_one/                       #All function from Hypothesis One   
    │   │   ├── data_treatment_h1.py
    │   │   ├── graphics_h1.py       
    │   ├── hypothesis_two/                       #All function from Hypothesis Two 
    │   │   ├── ploter.py
    │   │   ├── categorizer.py
    │   ├── hypothesis_three/                     #All function from Hypothesis Three
    │   │   ├── data_cleaning.py
    │   │   ├── data_treatment.py
    ├── tests/                                    #UnitTests
    │   ├── test_data_cleaning.py                 
    │   ├── test_data_treatment.py    
    │   ├── test_data_unittests_h2.py
    ├── docs/                                     #Documentation
    │   ├── source/                               #.rst files
    │   │   ├── Arquivos .rst
    │   ├── build/                                #html files
    │   │   ├── Arquivos .html
    │   ├── Makefile
    ├── data/                                     #All data generated/utilized at project, images and .csv files
    │   ├── dataset.csv
    │   ├── cleaned_dataset.csv
    │   ├── final_dataset.csv
    │   ├── test.csv                              #File used at Unit Test
    │   ├── Lucas/                                #Graphics for Hypothesis One
    │   │   ├── Gráficos Hipótese 1
    │   ├── Pandemic/                             #Graphics for Hypothesis Two
    │   │   ├── Gráficos Hipótese 2 
    │   ├── gender_and_crime/                     #Graphics for Hypothesis Three
    │   │   ├── Gráficos Hipótese 3
    ├── requirements.txt                          #Dependencies of the project
    ├── README.md                                 #General view of the project


Structured
^^^^^^^^^^

Initially, the main function executes a general cleaning of the dataset, preparing it for analysis. 
This involves removing data columns that are not used in any of the three developed hypotheses, with 
the result saved in a .csv file. After this initial cleaning, the main function executes specific 
cleaning functions for each hypothesis, aiming to improve the quality of the data used in the analysis.

Furthermore, when the main function is executed, the graphs that will be used in the Sphinx report are 
generated, along with the intermediate .csv files that are essential for the analysis. In the src directory, 
there are subfolders named after each hypothesis, containing the functions specifically created for the 
corresponding analysis.

In the data directory, all generated files are stored, including images and .csv files, as well as the main 
dataset, which contains all the data used throughout the analysis. The tests directory includes unit tests 
for the functions, except for those intended for graph plotting.

Finally, in the docs directory, there are .rst and .html files used for developing the documentation with 
Sphinx. In the root of the project, there is a requirements.txt file that lists the libraries needed for the 
proper execution of the project.

What Each One Have Done
------------------------

During the development of the project, all members remained consistently active, as observed through the commits 
made. Each member was responsible for creating their specific functions, developing unit tests, and writing the 
analyses of the hypotheses.

In the graphic design aspect, Victor Iwamoto took charge of creating an aesthetic identity for Sphinx and the graphs, 
standardizing and harmonizing the visual elements. Overall, there was full participation from the members in organizing 
the project modules and in the development of Sphinx documentation. 

References
----------
* `Dataset Download <https://catalog.data.gov/dataset/crime-data-from-2020-to-present>`_
* `Column Description <https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/about_data>`_

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   documentation
   hypothesis_one
   hypothesis_two
   hypothesis_three

