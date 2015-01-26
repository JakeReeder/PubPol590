from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# IMPORTING DATA -----------------------------------------

## Assigning the file paths to variables

main_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/PubPol590"
txt_file = "/Data/sample_data_clean.txt"
csv_file = "/Data/sample_data_clean.csv"

main_dir + csv_file

##read_csv and read_table are the two functions
df = pd.read_csv(main_dir + csv_file)
df2 = pd.read_table(main_dir + txt_file)

## check obj type
type(df)

## EXPLORING DATA FRAME -----------------------------

list(df)

## extracting column data (Series)

c = df.consump
c2 = df['consump']

type(c)

## BOOLEAN OPERATORS (LOGICAL OPERATORS) -----------------------------------
c == c2 #double equals sign is super important for testing equality
c > c2 # test greater than
c >= c2 # test greater than

#other boolean operators <. <=, !=

## ROW EXTRACTION ---------------------

## row slicing

df[5:10] #df[m:n] yields rows m to n-1
df[0:10] == df[:10] 
df[10:11]

# row slicing from series
c[5:10] # or equivalently

df.consump[5:10]


## extraction by boolean indexing

# only look at participant 4

df.panid == 4

df[df.panid == 4] # extract subset of df where panid == 4
df[df.consump > 2]

df.panid[df.panid >2]


















