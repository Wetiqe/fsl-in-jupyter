# A Jupyter template for mri and behaviour data analysis
I believe this will be helpful if you are trying to use jupyter lab for you neuroimaging study for the first time.

# Usage
## Preparation notebook
This notebook contains the instructions on how to create virtual enviroment for your project and then how to install local pakage pysetup.    
You can write your own functions in pysetup and then you can use them in all notebooks within this project easily.     
If you want to use other language such as R\matlab\bash, I also included some notes for how to install these kernels in jupyter.     
If you want to isntall and run jupyter on a server, check the end of the notebook.

## FSL in Jupyter notebook
This notebook explains how to run neuroimaging analysis in jupyter notebook using fsl and shell command.

The contents includes the benefits of doing this, how to run fsl command in jupyter notebook and 
how to interact with python syntax.


## database folder
Put your data base in here such as xlsx file, sql db file dtc. in pysetup.general, there was a function for connecting to xlsx file and sqlite3 db.

## pysetup folder
This folder is a local package which includes four modules. 
* general module includes the functions for data cleaning, creating data tables etc.
* stat module includes some functions for statistical analysis.
* plot moudle includes some functions for plotting figures using seaborn and matplotlib
* r moudle includes some r functions created using rpy2 moudle.

you can also create and put your own moudle and function here.

# Data analysis folder
## behaviour_data_analysis
data_cleaning.ipynb: load, clean and group the data, use %store to store cleaned data.    
data_analysis.ipynb: Create multiple ones for different analysis.     
plot.ipynb: in this this notebook, there were some hints for plotting in python. 
In general, a seperate notebook for plotting is not necessary .

## mri_analysis
create subfolders for different analysis and then a notebook in this folder.
If you installed matlab or bash kernel, you can use most of
the imaging tools from the notebook and keep an record. 
You can use your database or %store to interact with your behaviour data. 

# Future goals
build a work flow for basic mri analysis method using jupyter notebook just like tbss.notebook

