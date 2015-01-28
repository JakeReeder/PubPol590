## CLASS 3 DATA CLEANING: 01/28/2014

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/Data"
git_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/PubPol590"
csv_file ="sample_data_clean.csv"

#OS Module ------------------------

df = pd.read_csv(os.path.join(main_dir, csv_file))
