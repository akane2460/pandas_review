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

# Recall elements in a dataframe
print(my_dataframe.loc[0]) # returns first row in data frame
print(my_dataframe.loc[[0, 2]]) # returns first and third row in data frame

# Slice elements in a dataframe
print(my_dataframe.loc[0:2])

# Creating a new dataset:
dataset = {
    'Cars': [20, 15, 12],
    'Bicycles': [25, 23, 15]
}
dataframe2 = pd.DataFrame(dataset)
print(dataframe2)