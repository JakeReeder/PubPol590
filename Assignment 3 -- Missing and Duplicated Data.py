## ASSIGNMENT 3: Missing and Duplicated Data

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/Data"
git_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/PubPol590"
csv1 = "small_data_w_missing_duplicated.csv"

#IMPORT THE DATA
df = pd.read_csv(os.path.join(main_dir, csv1))
df = pd.read_csv(os.path.join(main_dir, csv1), na_values= ['-'])

#Drop the duplicates
df1 = df.drop_duplicates()

#Explore
df1[df1.consump.isnull()] ## shows just the rows where consump is empty

df1[df1.duplicated(['panid','date'])] # Looks at duplicated
df1[df1.duplicated(['panid','date'], take_last=True)] # Looks at duplicated from bottom

t_b = df1.duplicated(['panid','date'])
b_t = df1.duplicated(['panid','date'], take_last=True)

df1[ (t_b | b_t) ]     #shows both sets. useful for deciding which to keep
                        # we've decided to keep the bottom to top, as they have consump values

df2 = df1.drop_duplicates(['panid', 'date'], take_last=True)

df2 #df2 is 16 rows shorter than df1

df2[df2.duplicated(['panid','date'])] #check it -- nothing returned!

df2.consump.mean() # get that mean


