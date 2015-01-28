##Class 3: FOR LOOPS 01/28/2014


from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/Data"
git_dir = "/Users/Jake/Desktop/Duke/Energy and Big Data/PubPol590"
csv_file ="sample_data_clean.csv"

# FOR LOOPS 

df = pd.read_csv(os.path.join(main_dir, csv_file))

list1 = range(10,15)
list2 = ['A','B','C',]
list3 = [1,'a', True]

## iterating over elements (for loops)

for v in list1:
    v
    
for v in list2:
    print(v)
    
for v in list3:
    print(v,type(v))
    
for v in list3:
    print(v,type(v), 'haha')
    
## Populating Lists
    
list1 # all integers
list4 = [] #empty list
list5 = []

for v in list1:
    v2 = v**2
    v3 = v+20
    list4.extend([v2]) #extend requries a list object using []
    list5.append(v3) #append can accept any type

list4
list5

[v**2 for v in list1]

list6 = [v**2 < 144 for v in list1]
list6

##iterating using enumerate

list7 = [ [i, v] for i, v in enumerate(list1)]
list7

#Add divide by 2 for shits and giggles. Note that v/2 delivers integers currently
list7a = [ [i, v/2] for i, v in enumerate(list1)]
list7a

#Add float in there to get decimals
list7b = [ [i, float(v)/2] for i, v in enumerate(list1)]
list7b

## Iterate througgh a series -------------
s1=df['consump']
[v > 2 for v in s1]
[[ i, v] for i, v in s1.iteritems()]

## ITERATE THROUGH A DATAFRAME -------------------

[v for v in df]
[df[v] for v in df]
[[i, v] for i, v in df.iteritems()]