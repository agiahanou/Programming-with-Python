#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#==============================================================================

# Day 4: Programming with Python
# 
# Data visualization
# 
# Data visualization is a way to show a complex data in a form that is graphical and 
# easy to understand. This can be especially useful when one is trying to explore the data.
# 
# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. 
# It is one of the most widely used, if not the most popular data visualization library in Python.
# 
# Matplotlib is designed with the philosophy that you should be able to create simple 
# plots with just a few commands. Although Matplotlib is written primarily in pure Python, 
# it makes heavy use of NumPy and other extension code to provide good performance, 
# even for large arrays.
# 
# Figure

# Every plot that matplotlib makes is drawn on something called Figure. Figure object is as a canvas 
# that holds all the subplots and other plot elements inside it. It is the top level container for all the plot elements.

# pyplot
# The pyplot module contains command-style functions and each of them makes some changes 
# to the Figure object. Pyplot tracks the status of the current figure and its plotting area. 
# The functions called act on the current figure.

#==============================================================================


import matplotlib.pyplot as plt
import pandas as pd
import random

#==============================================================================
# 1. Basic plotting
# Key points:
# 
# plt.plot(): Creates a plot 
# plt.title(): Sets a title to the plot
# plt.xlabel(): Sets a label at the x-axis 
# plt.ylabel(): Sets a label at the y-axis 
# plt.figure(figsize=(x,y)): Creates a figure of width x and height y
# plt.subplot(nrows, ncols, index): Creates a subplot
# fig.suptitle(): Sets a title to the figure

#==============================================================================

# create an array y and plot it
random.seed(0)
y = []

for i in range(10):
    y.append(random.randint(0, 20))

# code here
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

# plot x, y
# code here

# Add the title to the plot
# Add the labels with the xlabel() and ylabel()
# Add a legend

# Make the same plot but now use the Figure - plt.figure(figsize=(10,7))
# code here

# I want to get two lines in the same plot (x, y) and (a, y2)

y2 = []
for i in range(10):
    y2.append(random.randint(10, 30))

#==============================================================================
# Subplots
# Sometimes we want to show different plots and place them next to each other.
# We do that with the subplot() function. The subplot() takes as arguments the number of rows and colums. 
#==============================================================================

# ax1 = plt.subplot(1, 2, 1)
# Plot y and y2 but now side by side
# 
# Exercises 1-5
#==============================================================================
# 2. Scatter Plots
# 
# plt.scatter(): Plots a scatter plot
# 
# Scatterplot is used to visualise the relationship between two columns/series of data. 
# The graph displays the collection of data points without connecting. 
# The chart needs two variables, one variable shows X-position and the second variable 
# shows Y-position.

#==============================================================================

# Create a simple scatter plot with some data (x, y)
# Change the size with the s parameter and the color of the dots with color parameter
# Change the shape of the points with the marker parameter
#
# code here
#
#Exercise 6
#
#==============================================================================
# 3. Bar graphs
# 
# plt.bar(): Plots a bar graph
# 
# Bar graph represents the data using bars either in horizontal or vertical directions. 
# Bar graphs are used to show two or more values and typically the x-axis should be 
# categorical data. The length of the bar is proportional to the counts of the 
# categorical variable on x-axis. 
# 
# The function used to show bar graph is plt.bar(). The bar() function expects two lists 
# of values one on x-coordinate and another on y-coordinate.

#==============================================================================

# Create the bar graph for the products sold in March

# Note that we have to transform the product to integers list and then say to the plot that each number corresponds to a product.

product = ['camera','phone','laptop','screen','tablet']
March =[700, 800, 950, 300, 250]
April =[600, 900, 920, 130, 210]
x = range(len(product))

df = pd.DataFrame({'product': product, 'March': March, 'April': April})

# code here

# Change the width of the columns
# Change the color of the bars
# code here

# Create multiseries bars for sales in March and April

product = ['camera','phone','laptop','screen','tablet']
March =[700, 800, 950, 300, 250]
April =[600, 900, 920, 130, 210]
x = range(len(product))

df = pd.DataFrame({'product': product, 'March': March, 'April': April})

x_March = [0.1, 1.1, 2.1, 3.1, 4.1] 
x_April = [-0.1, 0.9, 1.9, 2.9, 3.9]

# code here

#==============================================================================
# 4. Pie chart

# plt.pie(): Plots a pie chart


# A pie chart is a circular statistical graphic, which is divided into slices to illustrate numerical proportion.

#==============================================================================

# Create the pie chart for the products sold in March. Labels are the product list

# code here

#==============================================================================
# 5. Box Plots
# 
# plt.boxplot(): Plots a boxplot
# 
# Box plots visually show the distribution of numerical data and skewness 
# through displaying the data quartiles (or percentiles) and averages. 

# A boxplot is a graph that gives you a good indication of how the values in the data 
# are spread out.
#==============================================================================

# Create the boxplot of the sales in March
# Create the boxplot of the sales in March and April

# code here

#==============================================================================

# 6. Save a plot

# plt.savefig(path): Saves the plot to an image at path

#==============================================================================

# Save the boxplot with the savefig() function 
# code here

# Exercises 7-9

#==============================================================================
# Exercises
# 1. Read the file greece-population-2021-06-09.csv and save it in a DataFrame df_GR
# 
# 2. Plot the distribution of the population growth in Greece (greece-population-2021-06-09.csv) as changed in years (date and population columns)
# 
# 3. Load the netherlands-population-2021-06-09.csv as well. Plot the distribution of the population growth in Greece (greece-population-2021-06-09.csv) and Netherlands (netherlands-population-2021-06-09.csv) in the same plot
# 
# 4. Add title, xlabel and ylabel to the plot
# 
# 5. Let's say we have some ratings from users towards some movies. 

# a. Make a scatter plot of x (ratings) and y (movies_ids)
# b. Increase the size of the points to 250
# c. We also have colors that show the satisfaction regarding the inital expectations. Change the color of the points in order to reflect the satisfaction (search online for colorbar)
#
# 6. Load the greece-population-2021-06-09.csv file and create a boxplot of the Population
#
# 7. Load the netherlands-population-2021-06-09.csv file as well and plot the boxplots of population in Greece and the Netherlands
# 
# 8. Make the boxplots of the previous exercise horizontal
# 
# 
# 9. Bonus: Create a heatmap with Seaborn
# 
# Seaborn is an open-source Python library built on top of matplotlib and is used for data visualization and exploratory data analysis.
# 
#     a. Import seaborn as sns and load the iris dataset (use the load_dataset("iris"))
# 
#     b. Create the Correlogram of iris features
# 
#==============================================================================