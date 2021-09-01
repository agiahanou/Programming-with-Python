#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#==============================================================================
# Day 3: Programming with Python

# 3.2 Pandas Basics

# Pandas is one of the most used open-source Python libraries to work with structured 
# tabular data for analysis. Pandas is widely used for data science, machine learning, 
# and many more. It offers data structures and operations for manipulating numerical tables and time series. 

# In this unit we will see some of the basic functionalities of Pandas like 
# how we can create Pandas data structures, view information on the data and columns, 
# working with index, and how to combine different pandas data structures.
#==============================================================================

import pandas as pd

#==============================================================================
# 1. Pandas datatypes
# Key points:
# 
# - pd.Series(): Creates a Series
# - pd.DataFrame(): Creates a DataFrama
# 
# Series is a one-dimensional data structure. It holds data of many types including objects, 
# floats, strings and integers. 
# DataFrame is a more complex data structure and is designed to contain data with several dimensions.


#==============================================================================

# Create a Series s from a list (listItems) that contains the numbers [1,3,6,9]
#code here#

# Create a Series from the list [1.1,3.1,6.1,9.1] and check the type of the data 
#code here#

# Create a Series from ["Anna", "John", "Mark"]
#code here#


#==============================================================================
# Until now we talked about the Series that is a 1-dimension data structure. 

# The DataFrame is a tabular data structure and is similar to a spreadsheet. 
# It is a 2-dimensional data structure where each column contains data of the same type. 
# DataFrames are great for representing real data: rows correspond to instances, and 
# columns correspond to features of these instances. 

# For example, in a case of movies, we can have movies as rows and 
# different metadata (title, release year, duration etc.) for each movie in the columns.
#==============================================================================

# Create a simple DataFrame from a single list, [1,3,6,9]
#code here#

# Create a DataFrame from a dictionary

data = {'title': ['The Pianist', 'Gladiator', 'The Godfather', 'Inception', 'Titanic'],
                    'year':[2002, 2000, 1972, 2010, 1997],
                   'duration':[150, 155, 177, 148, 195]}

print(data)

#code here#

#==============================================================================
# 2. Index
# 
# Key points:
# 
# - pd.Series(list, index): Creates a series and assigns index
# - series.index: Assigns index to a series
# - pd.DataFrame(dict, index): Creates a DataFrame and assigns index
# - df.index: Returns the index of the DataFrame
# - df.values - Returns the values of the DataFrame

# Until now, every time we created a Series from a list there was an additional column on the left. 
# This axis is called index and is added into the pandas Series and DataFrames. 
# Index is like an address for the stored data, and can be used to access any data pointacross the DataFrame or Series.
# 
# The index can be specified at the creation of the Series or the DataFrame. 
# If we do not specify any index during the construction of the Pandas object then, by default, 
# Pandas will assign numerical values increasing from 0 as labels.

#==============================================================================

# Create a Series that contains grades of a student (listItems) regarding ['Math', 'Physics','Chemistry', 'History']. 
# Set the courses as index with the parameter index
#code here#

# The index can also be defined later with the s.index attribute
s = pd.Series(listItems)
print(s)
#code here#
print(s)

# In a similar way we define the index in DataFrames
df = pd.DataFrame({'year':[2002, 2000, 1972, 2010, 1997],
                  'duration':[150, 155, 177, 148, 195]},
                    #code here#
                  )

# With the df.values and the df.index attributes we view the value and index arrays
#code here#

 
#==============================================================================
#  3. Knowing my data
# Key points:
# 
# - df.info(): Prints a concise summary of a DataFrame
# - df.shape: Returns a tuple representing the dimensionality of the DataFrame
# - df.columns: Returns the column labels of the DataFrame
# - df.head(n): Returns the first n rows (default is 5)
# - df.tail(n): Returns the last n rows (default is 5)

#==============================================================================

df = pd.DataFrame({'year':[2002, 2000, 1972, 2010, 1997, 2001, 2016, 2004],
                  'duration':[150, 155, 177, 148, 195, 130, 128, 124]},
                  index=['The Pianist', 'Gladiator', 'The Godfather', 'Inception', 'Titanic', 
                         'Moulin Rouge', 'La La Land', 'The Notebook'])

print(df)

# With the info() we see general information on the DataFrame
#code here#

# With the shape we get the dimensions of the DataFrame
#code here#

# With the columns we get the names of the columns
#code here#

# Get the first 5 rows of the DataFrame
#code here#

# Get the first 3 rows of the DataFrame
#code here#

# Get the last 5 rows of the DataFrame
#code here#

# Exercises 1-2

#==============================================================================
# 4. Working with columns
# 
# Key points:
# - df.column: Returns the data of a column
# - df['column']: Returns the data of a column
# - df[['column1', 'column2']]: Returns the data of multiple columns
# - df['new_column'] = list: Creates a new column and assigns data to it
# - del df['column']: Deletes a column

#==============================================================================

df = pd.DataFrame({'year':[2002, 2000, 1972, 2010, 1997, 2001, 2016, 2004],
                  'duration':[150, 155, 177, 148, 195, 130, 128, 124]},
                  index=['The Pianist', 'Gladiator', 'The Godfather', 'Inception', 'Titanic', 
                         'Moulin Rouge', 'La La Land', 'The Notebook'])

print(df.head())

# Select the column year
#code here#

# Select the columns year and duration
#code here# 

# Add the column of genre
genre = ['drama','action','crime','action','romance', 'drama', 'romance', 'romance']
#code here#

# Delete the column of genre with the del keyword
#code here#

#==============================================================================
# 5. Working with rows
# 
# Key points:
# - df.loc['index']:  Returns data of the row with index label index
# - df.loc[['index1', 'index2']]: Returns data of multiple rows
# - df.loc['index1': 'index2']: Returns data from row index1 until index2
# - df.loc['index1': 'index2', 'column']: Returns data of a column and from row index1 until index2
# - df.loc[df['column'] >/</>=/<=/==]: Returns data of a column based on a condition
# - df.iloc[indexID]: Returns data of a row with specific index id 

#==============================================================================

df = pd.DataFrame({'year':[2002, 2000, 1972, 2010, 1997, 2001, 2016, 2004],
                  'duration':[150, 155, 177, 148, 195, 130, 128, 124]},
                  index=['The Pianist', 'Gladiator', 'The Godfather', 'Inception', 'Titanic', 
                         'Moulin Rouge', 'La La Land', 'The Notebook'])

print(df.head())

# Return the data of the row of Gladiator with the loc
#code here#

# Return the data for Gladiator and Titanic
#code here#

# Return the data from Gladiator until Inception
#code here#

# Return the duration of the movies from Gladiator until Inception
#code here#

# Return the data of movies that last more that 2.5 hours (150 minutes)
#code here#

# Return the third row with iloc
#code here#

# Exercises: 3-5
#==============================================================================
# 6. Combining DataFrames
# 
# Key points:
# - pd.concat([df1, df2]): Concatenates two DataFrames along axis 0
# - pd.concat([df1,df2], axis = 1): Concatenates two DataFrames along axis 1
# - pd.merge(df1, df2): Merges two DataFrames similar to relational algebra
# 

# Pandas provides various facilities for combining together Series or DataFrames with 
# various kinds of set logic for the indexes and relational algebra functionality 
# in the case of join / merge-type operations.

#==============================================================================

# pd.concat([df1, df2]) performs concatenation operations along an axis

df = pd.DataFrame({'year':[2002, 2000, 1972, 2010, 1997],
                  'duration':[150, 155, 177, 148, 195]},
                  index=['The Pianist', 'Gladiator', 'The Godfather', 'Inception', 'Titanic'])

print(df)

df_new = pd.DataFrame({'year': [2021, 2019],
                   'duration': [108, 132]},
                  index=['Nomadland', 'Parasite'])

print(df_new)

# Concatenate the two dataframes, create the df_conc variable
#code here#

# Concatenate the genre of the movies
df_new = pd.DataFrame({'genre': ['drama','action','crime','action','romance']},
                   index=['The Pianist', 'Gladiator', 'The Godfather', 
                          'Inception', 'Titanic'])

df_new

#==============================================================================
# We use the merge() function to combine data objects based on one or more keys 
# in a similar way to a relational database. 
# More specifically, merge() is most useful when we want to combine rows that share data.

# We can achieve both many-to-one and many-to-many joins with merge(). 
# In a many-to-one join, one of your DataFrames will have many rows in the merge column that 
# repeat the same values while the merge column in the other DataFrame will not have repeat values.
#==============================================================================

df = pd.DataFrame({'title':['The Pianist', 'Gladiator', 'The Godfather', 'Inception', 'Titanic'],
                  'year':[2002, 2000, 1972, 2010, 1997],
                  'duration':[150, 155, 177, 148, 195]})



df_new = pd.DataFrame({'title':['Gladiator', 'Inception'],
                   'score':[8.9,8.5]})


# Concatenate the two dataframes, is this the result we want?
#code here#


# The pd.merge() function recognizes that each dataframe has a title column, and 
# automatically joins using this column as a key. 
# The result of the merge is a new dataframe that combines the information from the two input dataframes.


# Merge the two dataframes
#code here#


# Many-to-one joins are joins in which one of the two key columns contains duplicate entries. 
# For the many-to-one case, the resulting dataframe will preserve those duplicate entries as appropriate. 

df_movies = pd.DataFrame({'title': ['Gladiator', 'Amelie','Parasite'],
                    'duration': [155,123,132]})

df_genre = pd.DataFrame({'title': ['Gladiator', 'Gladiator', 'Amelie','Titanic'],
                    'genre': ['action', 'drama', 'romance', 'romance']})
print(df_movies)
print()

print(df_genre)
print()

# Merge the two dataframes
#code here#

# We have many-to-many merge if the key column in both the left and right array contains duplicates.


df_country = pd.DataFrame({'title': ['Gladiator', 'Gladiator', 'Amelie', 'Amelie', 'Parasite'],
                    'country': ['UK', 'USA', 'France', 'Germany', 'South Korea']})
df_genre = pd.DataFrame({'title': ['Gladiator', 'Gladiator', 'Amelie','Titanic'],
                    'genre': ['action', 'drama', 'romance', 'romance']})
print(df_country)
print()

print(df_genre)
print()

# Merge the two dataframes
#code here#

# The how argument defines the type of merge to be performed

# Let's say we have the df_country and df_genre


print(df_country)
print()
print(df_genre)

#code here#

# Exercises: 6-9
#
#==============================================================================
# Summary
# 
# In this unit, we covered basic functions of Pandas including how to create Pandas Series and DataFrames, 
# and how to access the data.
# 
# In addition, we covered the main joining functions of Pandas, namely concat() and merge().
# 
# Although these functions operate quite similar to each other, there are some fundamental differences among them.
# 
# Pandas concat() can be used for joining multiple DataFrames through both columns or rows. 
# It is considered to be the most efficient method of joining DataFrames.
# 
# Merge() function performs joins similar to SQL. With the help of merge() we can merge values 
# using a common column found in two DataFrames.
#==============================================================================

#==============================================================================
# Exercises
# 
#  
# 1. Read the IMDB_movies.csv file and print all the basic information for the data, names of colums, 
# shape and the first 5 rows
# 
# 2. Assume you have the following dictionary with some passengers of a flight. 
# Create a DataFrame df from the dictionary and assign pass_id as index. Print the basic information on the DataFrame, its index, its colums and the first 7 rows
#
# passengers = {"age":[23, 25, 78, 12, 56, 33, 67, 78, 34, 64], "priority":['y','y','n','n','n','y','y','n','n','y']}
# pass_id=[101,102,103,104,105,106,107,108,109,110]
#
# 3. Select the column age of the df
# 
# 4. Select the rows with id 105, 106 and 109
# 
# 5. Get the rows of passengers that are older than 40
# 
# 6. Assume you get additional passengers from a different source (df2). 
# Concatenate the two DataFrames and name the new DataFrame df3
# 
# 
# passengers2 = {"age":[54, 65, 12],
#              "priority":['y','y','n']}
# pass_id=[201, 202, 203]
# 
# 
# 7. Assume that for some passengers we have also some data for the flight they booked. Merge the two DataFrames (df3 and df_flights) including all the rows (outer) (assign the result to a new DataFrame df_merge). 
# 
# 8. Now you have information on flights delayed. Merge the two DataFrames (delayed with df_merge). 
# Make sure you keep the passengers id 
# 
# 
# delayed = pd.DataFrame({'flight': ['KL211','HV543', 'FR3990', 
#                                    'KL4345','KL4335', 'FR3090'], 
#                         'delay': ['y', 'n', 'y', 'n', 'y', 'y']})
# 
# 
# 9. Set the priority to 'n' for the passenger with id 205 and 210 

#==============================================================================








