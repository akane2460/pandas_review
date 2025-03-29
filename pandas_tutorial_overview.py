# Pandas Tutorial Overview

# import and install Pandas
import pandas as pd

# What is Pandas?
    # library used for analyzing, exploring and manipulating data in datasets

# Creating datasets
# Vehicle company, 3 types of vehicles, recording how many of each in stock
my_dataset = {
    'Vehicle': ['Car', 'Bicycle', 'Motorbike', 'Truck'],
    'In Stock': [10, 20, 15, 5]
}

my_dataframe = pd.DataFrame(my_dataset)
print(my_dataframe)

# Datasets in python are multidimensional tables
# Write as pd.DataFrame
# DataFrame is the whole table of data
# Can introduce Series (will explore in future)

# Recall elements in a dataframe----
print(my_dataframe.loc[0]) # returns first row in data frame
print(my_dataframe.loc[[0, 2]]) # returns first and third row in data frame

# Slice elements in a dataframe----
print(my_dataframe.loc[0:2])

# Creating a new dataset----
dataset2 = {
    'Cars': [20, 15, 12],
    'Bicycles': [25, 23, 15]
}
dataframe2 = pd.DataFrame(dataset2, index = ['Monday', 'Tuesday', 'Wednesday'])
print(dataframe2)

# Locating elements in dataframe using renamed index
print(dataframe2.loc['Tuesday'])

# Looking at Series----
a = [20, 15, 12]
series = pd.Series(a)
print(series)

# Can also locate elements in a series
print(series[0])

# similar to dataframes, can also relabel elements
b = [21, 10, 12]
series2 = pd.Series(b, index = ['Monday', 'Tuesday', 'Wednesday'])
print(series2)

# can locate elements using new labelled index:
print(series2['Monday'])

# Importing excel/CSV data into python----
# Pandas reading a CSV
df = pd.read_csv('my_data.csv')
print(df)
# locating rows
print(df.loc[0])
print(df.loc[[0, 3]])

# Can use head() and tail() operation in pandas
# returns first 5 rows
print(df.head())
# returns first 7 rows
print(df.head())
# returns last 5 rows
print(df.tail())
# returns last 7 rows
print(df.tail(7))

# retrieving dataset info/summary
print(df.info())

# Handling NA values in pandas----
df2 = pd.read_csv('my_data2.csv')
print(df2)

# utilizing .info() section of pandas
print(df2.info())

# can drop rows with empty entries
# complete_df = df2.dropna()
# print(complete_df)

# replacing NA values with given value
# df2.fillna(10, inplace=True)
# print(df2)

# replacing NA values with given value in a specific column
# df2['Cars'] = df2['Cars'].fillna(130)
# print(df2)

# Finding Mean, Mode, Medians of columns----
# mean and replacing entries
# mean = df2['Cars'].mean()
# print(mean)
#
# df2['Cars'] = df2['Cars'].fillna(mean)
# print(df2)

# mode
# mode = df2['Cars'].mode()[0]
# print(mode)
#
# df2['Cars'] = df2['Cars'].fillna(mode)
# print(df2)

# median
# median = df2['Cars'].median()
# print(median)
#
# df2['Cars'] = df2['Cars'].fillna(median)
# print(df2)

# simply replace an index
# df2.loc[6, 'Cars'] = 4000
# print(df2)

# Plotting dataframes using MatPlotLib----
# importing matplotlib
import matplotlib.pyplot as plt

df.plot()
plt.show()

