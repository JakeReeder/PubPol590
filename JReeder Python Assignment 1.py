## SETTING UP PYTHON -------------

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

## READING DATA
main_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/PubPol590"
txt_file = "/Data/File1_small.txt"

df = pd.read_table(main_dir + txt_file, sep = " ")

## EXTRACTING DATA

df[60:100]

df[df.kwh > 30]