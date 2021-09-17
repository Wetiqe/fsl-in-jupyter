# A Jupyter template for mri and behaviour data analysis
I believe this will be helpful if you are trying to use jupyter lab for you neuroimaging study for the first time.

# Usage
## Open the preparation notebook
This notebook contains the instructions on how to create virtual enviroment for your project and then how to install local pakage pysetup.    
You can write your own functions in pysetup and then you can use them in all notebooks within this project easily.     
If you want to use other language such as R\matlab\bash, I also included some notes for how to install these kernels in jupyter.     
If you want to isntall and run jupyter on a server, check the end of the notebook.

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
load and clean data in data_cleaning.ipynb, use %store to store cleaned data.    
Create multiple data_analysis.ipynb for different analysis.     
In plot.ipynb, there were some hints for plotting in python. In general, you do not need to create a notebook just for plotting.

## mri_analysis
create subfolders for different analysis and then a notebook in this folder.
If you installed matlab or bash kernel, you can use most of the imaging tools from the notebook and keep an record. You can use your database or %store to interact with your behaviour data. 

# Future goals
1. try eeg data using this template.
2. build a work flow for common mri analysis method using jupyter notebook just like tbss.notebook
3. write more notes about numpy\pandas\matplotlib\seaborn\scipy\markdown.
