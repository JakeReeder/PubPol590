#ASSIGNMENT 2

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/Data"
git_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/PubPol590"
csv_file = "sample_missing.csv"

#IMPORTING DATA: SETTING MISSING VALUES (SENTINELS) ----------------------------

df = pd.read_csv(os.path.join(main_dir, csv_file))
df.head() #returns top five values
df.head(10) #top n rows
df.tail(10)
df[:10]

#Determine data type
df['consump'].head(10)

df['consump'].head(10).apply(type) #applies the function type to the top rows

##WE DONT WANT STIRNG DATA. periods are common placeholders being interpreted as 
## Strings when we want them to be numbers. need to create new missing value sentinels
## USE 'na_values' to use sentinels

missing = ['.', 'NA', 'NULL', ' ']
df = pd.read_csv(os.path.join(main_dir, csv_file),na_values = missing)

df['consump'].head(10).apply(type)

# MISSING DATA (USING SMALLER DATAFRAME) ----------------------------

#quick tip: you can repeat lists by multiplying
[1,2,3]
[1,2,3]*3

#types of missing data

None
np.nan
type(None)
type(np.nan)

## create a small sample data set

zip1 = zip([2,4,8], [np.nan,5,7], [np.nan, np.nan, 22])
df1 = DataFrame(zip1, columns = ['a', 'b', 'c'])

## search for missing data using

df1.isnull() #pandas method to find missing data
np.isnan(df1) #numpy way

##subet of columns
cols =['a', 'c']
df1[cols]
df1[cols].isnull()

## find non missing values
df1.notnull()

#FILLING IN OR DROPPING VALUES

## Pandas method 'fillna'

df1.fillna(999)
df2 = df1.fillna(999)

## Pandas method 'dropna'

df1.dropna() # drop ROWS with ANY missing values e.g., does the below auto
df1.dropna(axis = 0, how = 'any') drop ROWS with ANY missing values

df1.dropna(axis = 1, how = 'any') drop COLUMNS with ANY missing values

df1.dropna(axis = 0, how = 'all') drop ROWS that have ALL missing values

## try it out with df

df.dropna(how = 'all')

#SEEING ROWS WITH MISSING DATA -----------------------------------------
df3 = df.dropna(how = 'all')
df3.head(10)

df3.isnull()
rows = df3['consump'].isnull()
df3[rows]