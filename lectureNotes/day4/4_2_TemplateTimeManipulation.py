#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#==============================================================================
# Day 4: Programming with Python
# Working with Time and Dates
# 
# It is common in our data to have dates and times especially when we deal with temporal 
# data. The dates and time in Python need to be handled with the appropriate libraries. 
# 
# In this unit we will work with dates and times in Python. 
# 
# Python provides the datetime module that supplies classes for manipulating dates and times. 
# 
# Pandas also provides a lot of functionality to work with times and dates. 
# The most common classes in pandas that can be used to handle time/date data are 
# Timestamp and DatetimeIndex. 

#==============================================================================

from datetime import datetime
import pandas as pd

#==============================================================================
# Key points:
# 
# - datetime(year=, month=, day=): Creates a datetime object
# - d.day/hour/year: Prints the day/hour/year of a datetime object
# - datetime(year=, month=, day=, hour=, minute=, second=): Creates a datetime object
# - d.hour/minute/second: Prints the hour/minute/second of a datetime object
# - datetime.now(): Returns the current date and time
# - datetime.strptime("", "%Y-%m-%d"): Converts a string to datetime
#==============================================================================

# Create a datetime d (2021/8/25) with the datetime()
# code here

# Extract the day, month and year
# code here

# Create a date with time
# code here

# Print the hour, minute and second
# code here

# Get the current date and time
# code here

#==============================================================================
# We can also parse a string into a datetime object with the strptime() functon. 
# This function takes as imput the string and the date format of the string. 
# For example, %Y-%m-%d means that I will expect a date in the format of year-month-day. 
# Check the codes here: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

#==============================================================================

# Create a datetime object d from the string 2021-8-25 (%Y-%m-%d).
dateString = "2021-8-25"
# code here

# Create a datetime object d from the string 2021/8/25 
dateString = "2021/8/25"
# code here

# Exercises 1-2

#==============================================================================
# 2. Handling dates with Pandas
# 

# - pd.Timestamp(): Creates a Timestamp object
# - ts.day/month/year/hour/minute/second: Prints the day/hour/year/hour/minute/second of a timestamp object
# - pd.DatetimeIndex(): Creates a DateTimeIndex object
# - pd.date_range(start = , end = , freq = ): Returns a fixed frequency DatetimeIndex

# Timestamp is the pandas equivalent of python’s datetime and is interchangeable with it in most cases. The timestamp takes as input either the string date or integers. 

#==============================================================================

# Create timestamps of different styles of dates

# 2021/8/25
# 2021-8-25 10:00:00 PM
# 2021, 8, 25, 10, 00, 00
# code here

# Extract the year, month, day, hour, minute, seconds from a timestamp
# code here


#==============================================================================
# DatetimeIndex

# The index of a timestamp is the DatetimeIndex. DatetimeIndex can be used like a regular index and offers all of its intelligent functionality like selection, slicing.
#==============================================================================

# Create a series s that has as index the dates 
dates = ['8-10-2020','4-10-2020','5-10-2020','6-10-2020', '7-10-2020', '1-10-2020', '2-10-2020']
s = pd.Series([10, 12, 9, 11, 13, 14, 15], index = dates)

# Get the data until '5-10-2020' with s.loc
# code here

# Create the series again but now parse dates as DatetimeIndex 
dates = ['8-10-2020','4-10-2020','5-10-2020','6-10-2020', '7-10-2020', '1-10-2020', '2-10-2020']
s = pd.Series([10, 12, 9, 11, 13, 14, 15], index = pd.DatetimeIndex(dates))

# Get the data until '5-10-2020' with s.loc
# code here

#==============================================================================
# date_range() returns the range of equally spaced time points such that they all occur between start and end. 
# The parameter freq defines the frequency (e.g., D for day, W for week, A for year, H for hour)

# pd.date_range(start = , end = , freq = )

#==============================================================================

# Create dates from 2021-8-1 to 2021-8-31 with a frequency of a day 
# code here

# Create dates from 2021-8-1 to 2021-8-31 with a frequency of  a week
# code here

#==============================================================================
# 3. Timedelta

#==============================================================================

from datetime import timedelta

# Create two datetimes and get their difference

dateA = datetime(2020, 8, 23, 5, 20, 30)
dateB = datetime(2021, 8, 23, 5, 20, 30)
# code here

# Add 2 weeks, 10 days to 2021-8-25 10:00:00
originalDate = datetime(2021, 8, 25, 10, 0, 0)

# code here

# Exercises 3-5
#==============================================================================
# 4. Working with Dates and DataFrames
#==============================================================================

# Create a DataFrame with some random prices

import random
random.seed(0)
prices = []
dates = pd.date_range(start = '2010-1-1', end = '2019-12-31', freq = 'D')

for i in range(len(dates)):
    prices.append(random.randint(0, 20))

df = pd.DataFrame({"prices": prices}, index= dates)

df.info()
df.head()

# Slice the data to view only data from 10 to 15 of January 2010 ('10-1-2010':'15-10-2010')

# code here

#==============================================================================
# Resampling is for frequency conversion and resampling of time series. 
# So, if one needs to change the data instead of daily to monthly or weekly etc. or vice versa.
#==============================================================================

# Calculate the mean for every month (df.resample())
# code here
# 

# Calculate the mean for every year (df.resample())
# code here

# Exercise 6
#==============================================================================

# Exercises
# 
# 1. Get the datetime of the current date and time and print the month and the hour
# 
# 2. You received the following date in string format. Convert it into Python’s datetime object.
# date_string = "Apr 28 2018 5:20PM"
# 
# 3. Print a range of dates from 1-12-2019 until 31-12-2019 with a range of 
# a) 2 days and 
# b) 8 hours
# 
# 4. Add 6 days and 12 hours to the following date: 25/2/2020 10.00 am
# 
# 5. Write a function that takes as an argument the birthday of someone and outputs the age 
# of the person. Call the function to calculate the age of someone born on 12/10/1990. 
# Call the function again to calculate your own age.
# 
# 6. Bonus
# a) Read the file daily_natural_gas.csv that is stored in the data folder.
# 
# b) Calculate the mean for the range from 01-01-1997 until 25-08-1997
# 
# c) Print the max value per year
# 
# d) Find the dates that are not in the index for the year 1997 (check the DateTimeIndex difference in https://pandas.pydata.org/pandas-docs/version/0.18/generated/pandas.DatetimeIndex.difference.html)
# 
# Hint: Parse the date as dates and make it index
#==============================================================================




