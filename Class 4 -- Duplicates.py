## Class 4 In Class demo!

from __future__ import division

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/Data"
git_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/PubPol590"
csv1 = "small_data_w_missing_duplicated.csv"
csv2 = "sample_assignments.csv"

#Import Data ---------------------------

df1 = pd.read_csv(os.path.join(main_dir, csv1), na_values= ['-', 'NA'])
df2 = pd.read_csv(os.path.join(main_dir, csv2))

## CLEAN DATA ---------------------------
# Clean DF1

df1 = df1.drop_duplicates()
df1 = df1.drop_duplicates(['panid','date'], take_last = True)

# Clean DF2
df2[[0,1]] ## This is the actual data that we want. Need to eliminate some BS

df2 = df2[[0,1]] #This reassigns df2 to be just the data we need

## COPY DATAFRAMES -----------------------------

df3 = df2 # creates alink/reference (changing df2 DOES AFFECT df3)
df4 = df2.copy() # creating a copy (changing df2 should not change df4)

#Replacing DATA ---------------
df2.group
df2.group = df2.group.replace(['T', 'C'], [1,0])

df3 #Note that df3 has changed!
df4 #Note that df4 has not!

## MERGE ------------------------------
#Trying to merge df1 into df2 but they have the wrong length, blah blah

pd.merge(df1, df2) # 'many-to-on' merge using the intersection. automatically finds 
                    # keys that are in common
                    
pd.merge(df1, df2, on = ['panid'])    # tells it to merge on panid (useful in case you had multuple things)

pd.merge(df1, df2, on = ['panid'], how = 'inner') #this way exludes PanID 5
pd.merge(df1, df2, on = ['panid'], how = 'outer') #this includes the PanID 5

df5 = pd.merge(df1, df2, on = ['panid'], how = 'inner') #this way exludes PanID 5

df5.group.mean()

## ROW BINDS AND COLUMN BINDS ===========

## row bind

pd.concat([df2,df4]) #default is to row bind

pd.concat([df2,df4],axis=0)
#column bind
pd.concat([df2,df4],axis=1)

pd.concat([df2,df4],axis = 0, ignore_index= True) #ignore index = false is default
        ##this comand resets the index




