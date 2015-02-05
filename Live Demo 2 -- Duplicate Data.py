## LEARNING HOW TO DEAL WITH DUPLICATE VALUES

from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# DUPLICATED VALUES -----------------------------------

## create a new data frame
zip3 = zip(['red', 'green', 'blue', 'orange']*4, [5, 10, 20, 40]*3, [':(', ':D', ':D']*4)
df3 = DataFrame(zip3, columns = ['A', 'B', 'C'])
df3

## returns boolean vector of duplicated rows of a whole DataFrame or subset using method `duplicated`
## IMPORTANT: python, by default, searches for duplicated values from top-to-bottom
## and will not mark a row as "duplicated" until it actually finds another instance
df3.duplicated() # defaults using all rows searching top-to-bottom
df3.duplicated(take_last = True) # option `take_last = True` searches bottom-to-top

## SUBSET duplicates
# if we want the duplicated criteria to be of a subset, we can do that too
df3.duplicated(subset = ['A', 'B'])
df3.duplicated(['A', 'B']) # same as before


## HOW to get all values that have a duplicate
t_b = df3.duplicated()
b_t = df3.duplicated(take_last = True)
unique = ~(t_b | b_t) # negate where either is true
unique
unique = ~t_b & ~b_t # same as above
unique

df3[unique] ##this is things that were never duplicated at all

## DROPPING THOSE DUPLICATE ----------------------------------
df3.drop_duplicates()

df3.drop_duplicates(take_last=True)

## this is the same as....
t_b = df3.duplicated()
df3[~t_b]
df3.drop_duplicates() == df3[~t_b] ## shows that the above two are perfectly equivalent

## subset criteria

df3.drop_duplicates(['A', 'B'], take_last=True)

#WHEN TO USE ------------------
##if you want to keep the first duplicated value (from top) and remove others
df3.drop_duplicates()

#same but from bottom
df3.drop_duplicates(take_last=True)

## purge all values that are duplicated (including the first instance)

t_b = df3.duplicated()
b_t = df3.duplicated(take_last = True)
unique = ~(t_b | b_t) # negate where either is true
unique

df3[unique] ##these are the only values that are never repeated in the data set
    #contrast with
df3.drop_duplicates()
