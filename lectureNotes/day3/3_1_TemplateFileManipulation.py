# -*- coding: utf-8 -*-

#==============================================================================
# Day 3: Programming with Python

# 3.1 File manipultation

# Until now, we used the standard input and output to read and write. 
# However, almost always we have our data in files and we want to read data from files and also write to them.

# In this unit we will see basic functions and methods necessary to manipulate files in Python. 
# Most of the file manipulation can be done with a file object.
#==============================================================================

#conda install pandas (if not installed)

import csv
import pandas as pd

#==============================================================================
# 1. Reading and writing to a file
# 
# Key points:
# 
# - open() - Opens the file in a spcific mode
# - write() - Writes to file
# - read() - Reads the file
# - readlines() - Returns all lines in the file as list
# - readline() - Returns the current line in the file
# - with open() - When we use the statement with we do not have to close the file
#==============================================================================

# Open a file cities.txt and write 'Utrecht' into it
#code line# 

# Create the list cities with ["Paris", "Rome", "Athens", "Utrecht", "Berlin"]
# and write the cities list into the cities.txt
#code line# cities =

# Use loop to write the cities
#code line#

# Write to the file again by adding a newline 
#code here#

# Read the file cities.txt with read() (mode r)
#code line# f = 

# Read a file with the readlines() function
#code here#

# Read a file line by line with the readline() function (for loop)
#code here#

# Open and read a file using the with statement
#code here#

# Write the cities.txt using the with statement
#code here#

# Exercise  1-4
#==============================================================================
# 2. Reading and writing to CSV files
# Key points:
# 
# - csv.writer(file) - Creates the writer object
# - csv_writer.writerow() - Writes the data row by row
# - csv.reader(file) - The reader object
# 
# A common file that is used to store the data is the CSV file. CSV stands for Comma Separated Values and is a plain text file that stores tables and spreadsheet information. CSV files can be easily imported and exported using programs that store data in tables. We can open a CSV file with a text editor to view the data.
#==============================================================================

data = ["country, capital, continent",
        "France, Paris, Europe",
        "Japan, Tokyo, Asia",
        "Greece,Athens, Europe",
        "Cuba, Havana, America"
        ]

# Open the file in write mode and then create a writer object (csv_writer) with the csv.writer() 
# to write on it the list of the cities
#code here#

# Create the csv_reader reader object with the csv.reader(myFile) and print the capitals (for loop)
#code here#

# Split the line of every row of the data when you write to file (use writerow)
#code here#

# Read the file and print the capitals
#code here#

# Exercise  5-6  
#==============================================================================
# 3. Reading and writing csv files with Pandas
# 
# Key points:
# - pd.read_csv()** - Read the csv file
# - df.to_csv()** - Writes the dataframe to csv
# 
# The read_csv() function provides a variety pf different parameters, a description of which can be found here: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
#==============================================================================

# Read the cities.csv file 
#code line# 

# Set header parameter to None the following will happen
#code line# 

# Export the data to CSV format
#code line# 

# Exercise  7
#==============================================================================
# Exercises
# 
# 1. During the tutorial, we created the cities.txt. Read the file and print only line 3 from the file
# 
# 2. Append to this file (cities.txt) two more cities (London and Florence)
# 
# 3. Read the file and print its content. Print it in a way that every city is printed in a row without additional newlines
# 
# 4. Read the cities.txt file and write its content to a new file (cities2.txt) after skipping line 2
# 
# 5. Create a csv file called employers.csv (in the data folder) and write the data. Use as delimiter the symbol ;

# data = ["name,department",
#         "John,IT",
#         "Anna,IT",
#         "James,Management",
#         "Peter,Accounting",
#         "Luis,IT"
#         ]
# 
# 6. Now read the employers.csv file and print only the names of those that are in IT
# 
# 7. Read the employers.csv file again with Pandas and print it

#==============================================================================




