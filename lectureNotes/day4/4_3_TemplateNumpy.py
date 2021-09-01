#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#==============================================================================
# Day 4: Programming with Python
# 
# NumPy (https://numpy.org/) is the fundamental package for numeric computing with Python. 
# It is a Python library that provides a multidimensional array object, and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, basic linear algebra, basic statistical operations, random simulation and much more.

# Why use NumPy?

# Numpy data structures perform better in:

# Size - Numpy data structures take up less space.
# Performance - they have a need for speed and are faster than lists.
# Functionality - NumPy has optimized functions such as linear algebra operations built in.

# NumPy arrays are faster and more compact than Python lists. An array consumes less memory and is convenient to use. 
# NumPy uses much less memory to store data and it provides a mechanism of specifying the data types. 
# This allows the code to be optimized even further. Overall a task executed in Numpy is around 5 to 100 times faster than the standard python list.
#==============================================================================

#conda install numpy
import numpy as np

#==============================================================================

# 1. NumPy arrays
# 
# Key points:
# 
# - np.array(): Creates an numpy array
# - np.size: Returns the number of elements
# - np.shape: Returns the number of rows and columns
# - np.dtype: Returns the type of elements
# - np.ndim: Returns the dimensions of the array
# - np.reshape(): Converts an array to a new one of the specified dimensions
# 
# The NumPy library is based on one main object: ndarray (which stands for N-dimensional array). 
# This object is a multidimensional homogeneous array with a predetermined number of items: homogeneous because virtually all the items in it are of the same type and the same size. 
#==============================================================================

# Create an array A from a list, containing the numbers from 1 to 6 ([1, 2, 3, 4, 5, 6])
# code here

# Create an 2-d array B from a list with floats, the [1.1, 2.9] and [3.1, 4.2]
# code here

# Check the attributes of the A and B arrays with ndim, dtype, size and shape attributes 
# code here

# Change the shape of array A using the reshape() method
# code here

#==============================================================================
# 2. Creation routines
# 
# Key points:
# 
# - np.zeros(): Returns a new array of given shape, filled with zeros
# - np.random.random(size=(x, y)): Returns a new array of shape (x, y) filled with random numbers in (0, 1)
# - np.random.randint(N, M, size=(x, y)): Returns a new array of shape (x, y) filled with random integers from N to M
# - np.arange(): Returns evenly spaced values within a given interval of a specified step
#==============================================================================

# Create an array of dimensions (2,4) and fill it with zeros 
shape = (2, 4)
# code here

# Create an array with random values with the random() of size (2,4)
# code here

# Create an array with random integer numbers with the randint() of size (2,4)
# code here

# Create an array A that contains all the even numbers from 0 to 20 with the arange()
# code here

# exercises 1-4
#==============================================================================  
    
# 3. Access matrix elements, rows and columns

# Similar like lists, we can access matrix elements using index
    
#==============================================================================   
    
# Get the first and last element of array A
A = np.arange(2, 21, 2)
# code here


#==============================================================================
# 4. Sort arrays
# 
# Key points:
# 
# - np.sort(): Returns a sorted copy of an array
# 
# The method we can use to sort an array is the np.sort(). 

#============================================================================== 


# Sort the array [2, 1, 5, 3, 7, 4, 6, 8]

A = np.array([2, 1, 5, 3, 7, 4, 6, 8])
# code here

# Sort a 2-d array

A = np.array([[1, 0, 5], [3, 4, 1]])
# code here


#==============================================================================
# 5. Array operations

# With NumPy we can also perform matices operations, like addition, subtraction, square and matrix multiplication.

#============================================================================== 

# Create a list and then add each element by 3.
# code here
listNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create an array A and then add each element by 3.
A = np.arange(10)
print("A =",A)
# code here

# Add, subtract and multiple two arrays

A = np.array([[1, 2], [3, 4]])
print("A =",A)

B = np.array([[5, 6], [7, 8]])
print("B =", B)

# code here

#============================================================================== 
# NumPy provides mathematical functions such as sqrt(), and exp(). 
# Within NumPy, these functions operate elementwise on an array, producing an array as output.
#==============================================================================

# Get the exp and square root of the array A
A = np.arange(0, 5, 2)
print("A =", A)

# code here

#==============================================================================
# Aggregate functions perform an operation on an array and produce a single result 

#==============================================================================

# Return the min and max of an array A
A = np.array([[3, 6, 7], [5, -3, 0]])
print("A =", A)  

# code here

# Return the range between maximim and minimum with the ptp() function
# code here

# Return the mean, std and variance of A
# code here

# Exercises 5-6
#==============================================================================
# 6. Save and load NumPy objects

# It is more efficient to save our arrays to a file and load them back without having to re-run the code. 
# This is especially convenient when we have to calculate features from a huge amount of data that takes some time. 

# The .npy stores data, shape, dtype, and other information required to reconstruct the ndarray in a way that allows the array to be correctly retrieved, even when the file is on another machine with different architecture.

# If we want to store a single ndarray object, we can store it as a .npy file using np.save().

#==============================================================================

# Create a simple array A and save it to data folder
A = np.array([1, 2, 3, 4, 5, 6])
# code here

# Use np.load() to reconstruct the array and print the type of the array 
# code here

#==============================================================================

# All together
#==============================================================================

# Let's finally see how we can put everything together. Let's load the supermarket_sales and print Quantity
import pandas as pd

df = pd.read_csv("../data/supermarket_sales.csv")
df.head()

print(df['Quantity'])

# Convert the Quantity column to numpy array with to_numpy()
# code here

# Add to the Quantity the value of 5 
# code here

# Exercise 7-8
#==============================================================================
# Exercises
# 
# 1. Create an array A that contains all the odd numbers from 20 to 50
# 
# 2. Try to reshape A to a new 2d array with 5 rows and 2 columns. Name the new array B. How can you fix the error?
#   
# 3. Reshape A to a new 2d array with 8 rows and 2 columns. Name the new array B. 
# 
# 4. Create a random array (4, 4) with integer values from 100-120 
#
# 5. Create two random arrays (4, 4) with integers from 0-50 and then first add and then subtract them 
#
# 6. Create the A = [[3, 6, np.NaN, 7], [5, -3, 0, np.NaN]] that contains two NA values as well. Print the max and the mean of the whole array. What do you notice? Find a function to calculate the max and mean excluding the NaN values
# 
# 7. NumPy provides a lot of functions that can be applied on the DataFrame. 
#
# a. Read the supermarket_sales.csv file
# b. Normalise the Unit price with values from 0 to 1. First turn the df['Unit price'] to numpy and then create a new column df['normalisedPrice'] for the normalised values
# c. Create a new column `df['NewTotal']` that will contain the value of total after you subtract 2 from it


# 8. Bonus

# Create two lists and two numpy arrays of the size 10,000,000 containing all the numbers from 0 to 10,000,000. You can use range for the list and arange for the numpy arrays. Once you created the two lists, multipy them and print the execution time. Do the same for the numpy arrays and compare the diffence in performance. 

#==============================================================================