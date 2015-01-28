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

## TYPES OF DATA -----------------------------------------

# Strings

str1 = "hello, computer"
str2 = 'hello, human' # this is type string
str3 = u'eep' # this is type unicode

type(str1)
type(str2)
type(str3)

# Numeric

int1= 10
float1 = 20.5329847
long1 = 9809809890234798273289471092

# Logical
bool1 = True
notbool1 = 0
bool2 = bool(notbool1)

## Creating Lists and Tuples -----------------------
# Lists can be changed, tuples cannot. We will use lists.

list1 = []
list1

list2 = [3, 9, 15]
list2[2] #looks for the second element in the list, starting at 0!

list2[2] = 5 #changes the element in the list
list2


## tuples, can't change

tup1 = (8, 3, 19)
tup1[2]
tup1[2] = 5

## convert

list2 = list(tup1)
tup2 = tuple(list1)

## lists can be appended and extended
list2.append([3, 90]) #for example, this is appending another list
list2


list3 = [8, 3, 90]
list3.extend([6, 88])
list3

Jake = "Change the game"

## CONVERTING LISTS TO SERIES AND DATAFRAMES


list4 = range(100,105) # range values (n,m) -- gives a list from n to m-1
list4

list5 = range(5)
list5

list6 = ['q','r','s','t','u']
list6

## List to series

s1 = Series(list4)
s2 = Series(list6)

## List to DataFrame

#data frames have to have the same length of all parts, 
## so the series you are combining must be the same len()

zip(list4,list6)

list7 = range(60, 65)
zip1 = zip(list4, list6, list7)
df1 = DataFrame(zip1)

df1[1]

zip2 = zip(list4, list6, list7)
df2 = DataFrame(zip2, columns =['two','apple',':)'])

df2['apple']

df3 = DataFrame(zip2, columns =[2,'apple',':)'])

df3[2]

df3[3:4]

df3[[2,'apple']][3:4]

df4 = DataFrame({ ':(' : list4, 9 : list6}) #loads in order

#dictionary objects use curly brackets { and }. They have keys and in this case
# the number 9.


