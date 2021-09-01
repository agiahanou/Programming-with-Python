#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#==============================================================================
# Day 3: Programming with Python
# 
# Advanced Pandas 
# 
# In this unit we will explore more functionalities of Pandas that we can apply to analyse the data of the DataFrames. 
# We will see how we can select data that meet specific conditions and how we can perform statistical analysis on them.

# In the first part we will see how to find and deal with missing values 
# and then we will see how to calculate statistics from the data. 

# We will also explore the functionality of groupby that allows us to split the data into 
# separate groups to perform computations for better analysis.

#==============================================================================

import pandas as pd

df = pd.read_csv("../data/netherlands-population-2021-06-09_missing.csv")
df.info()
df.head()

#==============================================================================
# 1. Missing values
# 
# Key points:
# 
# - df.isnull(): Returns a boolean same-sized object indicating if the values are NA
# - df.isnull().sum(): Returns the number of missing values in the DataFrame per column
# - df.dropna(): Drops rows which contain missing values
# - df.fillna(): Fills missing values with the specified method
# - df.fillna(method = 'ffill'): Fills missing values with forward filling
# - df.fillna(method = 'bfill'): Fills missing values with backward filling

#==============================================================================


#==============================================================================
# Pandas gives us functionality to check if there are missing values in the dataset and methods to handle them. 

# There are different ways to address the missing values. 
# The first is to ignore the missing values and work with the rest of the data if there are enough. 

# The alternative is to use data imputation. There are different methods that can be used for data imputation. 

# If we are dealing with temporal data we can use the previous or the next value. 
# Another common way is to calculate the mean or median of the existing observations. 
# However, when there are many missing variables, mean or median results can result in a loss of variation in the data.

#==============================================================================

# Returns the boolean value for every item showing if there is a missing value
# code here

# With the sum() we can also see how many missing values we have per column
# code here

# The dropna() function drops all of those rows which have any missing data. 
# Print the 15 first rows to see the result
# code here

# fillna() fills the missing values with 0
# code here

# Use fillna() and set the parameter method to ffil(). 
# We will make a new dataframe df1 for that.

# code here

# Set the parameter method to bfill
# code here
#
#Exercises 1-5
#
#==============================================================================
# 2. Descriptive statistics
# Key points:
# 
# - df.describe(): Generates descriptive statistics of the DataFrame
# - df[col_name].describe(): Generates descriptive statistics of a column
# - df[col_name].mean(): Returns the mean of a column
# - df[col_name].sum(): Returns the sum of a column
# - df.col_name1[df['col_name2'] > < = x].mean(): Returns the mean of a column based on a condition
#
#
#==============================================================================

df = pd.read_csv('../data/supermarket_sales.csv')
df.head()

# Get the descriptive statistics with the describe() function 
# code here

# Get the descriptive statistics of Quantity with the describe() function 
# code here

# Calculate the mean of the Quantity
# code here

# Get the sum of the Quantity 
# code here

# Calculate the mean Quantity bought from customers that have bought at least 5 items
# code here

# exercises 6

#==============================================================================
# 3. Group by 
# 

# Key points:

# - df.groupby('col_name'): Splits the data into groups based on a column
# - df.groupby('col_name').groups: Returns the groups created after groupby
# - df_product.get_group('group_name').head(): Prints the first rows of a specific group
# - df.groupby('col_name').size(): Prints the size of groups
# - df.groupby(['col_name'])['col_name'].mean(): Returns the mean of a specific column after groupby operation
# - df.groupby(['col_name','col_name'])['col_name'].describe(): Returns descriptive statistics of of a specific column after groupby operation
# 
# The Groupby operation that is undoubtedly one of the most powerful functionalities of 
# Pandas. Groupby allows adopting a split-apply-combine approach to a data set. 
# This approach is often used to slice and dice data in such a way that a data analyst 
# can answer a specific question.
# 
# On a high-level groupby allows to:
# 1. Split the data based on column(s)/condition(s) into groups;
# 2. Apply a function/transformation to all the groups and 
# 3. Combine the results into an output

#==============================================================================

# Split the data based on their product line and print the groups
# code here

# Get the five first items of the "Fashion accessories" group with the get_group() method
# code here

# Size () gets the number of items per product line group
# code here

# Get the mean Quantity per product line
# code here

# Get all the general statistics of Quantity per Customer type and per Gender
# code here


#==============================================================================
# 4. Map and apply a Function

# Key points:

# - df['col_name'].map({}): Substitutes each value in a Series with another value
# - df['col_name'].apply(function): Applies a given function to each item of the given column
# - df['col_name'].apply(lambda x: x + 1 if x <= 5 else x + 2): Applies a lambda function to each item of the given column
# 
# Map is used for substituting each value in a series with another value that may be derived from a function. 
#==============================================================================

# Create an additional column Gender_num that will contain the value 0 for females and 1 for males. 
# code here


# With the apply() function we can apply a function along a row or a column of the DataFrame

# Create a function freeItems() that adds one if quantity is less that six, otherwise add two
def freeItems(x):
    if x <= 5:
        x = x +1
    else:
        x = x + 2
    return x

#==============================================================================
# A lambda function is a small function containing a single expression. 
# Lambda functions can also act as anonymous functions where they don’t require any name. 

# - df['col_name'].apply(lambda x: x + 1 if x <= 5 else x + 2): 
# Applies a lambda function to each item of the given column

#==============================================================================

# Do the same but now with lambda and apply
# code here

# exercises 7-10
#==============================================================================
# 5. Correlations
# 
# Key points:
#     
# - df['column1'].corr(df['column2']) - Calculates correlation between column1 and column2
# - df1.corr(df2, method='spearman') - Calculates spearman correlation between column1 and column2
# - df.corr(method ='pearson') - Calculates pearson correlation among all numerical columns of df
# 
# Correlation coefficients quantify the association between variables or features of a dataset. 
# Python has great tools that you can use to calculate them. 
# 
# Pearson r correlation: Pearson r correlation is the most widely used correlation statistic 
# to measure the degree of the relationship between linearly related variables. 
# For example, in the stock market, if we want to measure how two stocks are related to each other, 
# Pearson r correlation is used to measure the degree of relationship between the two. 

# Spearman rank correlation is a non-parametric test that is used to measure the degree 
# of association between two variables.  The Spearman rank correlation test does not carry 
# any assumptions about the distribution of the data and is the appropriate correlation 
# analysis when the variables are measured on a scale that is at least ordinal.

#==============================================================================

# Calculate the correlation between Unit price and Quantity

# code here

# Get the correlation between Branch and Total
# code here

# Get the correlation among all the numerical columns of the DataFrame df
# code here

# exercises 11-13
#==============================================================================
# Summary

# In this tutorial, we explored functions that can be used on the data of Pandas Series and DataFrames. 

# First, we explored ways to deal with missing values. Next, we worked with group by that 
# splits that data based on values that a column contains. 
# Also, we applied methods on the data with map and apply functions. 

# Finally, we calculated the correlation between two different variables/features that can also be part of a DataFrame.
#==============================================================================


#==============================================================================
# Exercises
# 
# 1. Read the file winemag-data_first50k.csv and print some of the information of the 
# DataFrame to get familiar with it
# 
# 2. Print the number of missing values per column
# 
# 3. Drop the rows that have missing values in province and check that they have been dropped
# 
# 4. Drop columns designation, region_1 and region_2 and save the new DataFrame to df. 
# Print the columns of the new DataFrame to check whether they have been dropped
# 
# 5. Get the first ten rows of the rows that have null price value
# 
# 6. Find the mean price for the wines that have at least 87 points
# 
# 7. Group the DataFrame by points and return the mean price per group
# 
# 8. Fill the missing values of prices with the mean value per group. 
# Save the result to the price column
# 
# 9. Print one of the rows that had missing value in price (question 5) and check the row again 
# 
# 10. Group by country and check the size per group
# 
# 11. Calculate the correlation between the price and points
# 
# 12. Calculate the correlation between price and points per country only if the country has 50 items
# 
# 13. Bonus:
# 
# Another widely used statistical test is the t test that tells you how significant the 
# differences between groups are. In other words it lets you know if those differences 
# (measured in means) could have happened by chance. For the t-test we need the scipy library.
# 
# Install the scipy library and get statistical difference in the wine price between Argentina and Chile and then between Italy # and Chile
# 
# import scipy.stats as stats
# 


#==============================================================================

