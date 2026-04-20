# number of dimensions
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Number of dimensions :", arr.ndim)
print("Number of elements :", arr.size)
print("Shape of array :", arr.shape)
print("Data type of array :", arr.dtype)
print("Size of each element in bytes:", arr.itemsize)
print("Total size in bytes :", arr.nbytes)
print("Transpose of the array :")
print(arr.T)


# indexing and slicing

# 1D array
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])

# 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[1, 2])

# 3D array
tensor = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print(tensor)
print(tensor[1, 0, 2])
print(tensor[0, 1, 0])


# slicing

# 1D array
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])
print(arr[:3])
print(arr[::2])

# 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[1:, 1:])
print(matrix[:, 1])
print(matrix[0, :])
print(matrix[:, ::2])

# 3D array
tensor = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print(tensor[:, 1, :])


# advanced indexing

# boolean indexing
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 30])

# fancy indexing
arr = np.array([10, 20, 30, 40, 50])
indices = [1, 2, 3]
print(arr[indices])

# multi-dimensional fancy indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rows = np.array([0, 1, 2])
cols = np.array([0, 1, 2])
print(matrix[rows, cols])


# modifying elements using indexing and slicing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix[:, 1] = [10, 20, 30]
print(matrix)


# array copy and view
original = np.array([1, 2, 3, 4, 5])
view = original[1:4]
view[0] = 99
print(original)

# using reshape does not create a copy
reshaped = original.reshape(1, 5)   # changed from (3, 4) to (1, 5)
print(reshaped)

# array copies
copy_array = original.copy()
copy_array[0] = 100
print(copy_array)
print(original)


# example of broadcasting

# scalar and array
arr = np.array([1, 2, 3, 4, 5, 6])
result = arr + 10
print(result)

# array and array with same shape
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[10, 20, 30], [40, 50, 60]])
result = arr1 + arr2
print(result)

# array and array with different shapes
arr1=np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[10,20,30]])
result = arr1 + arr2
print(result)

# iterating over array
# 1D array
import numpy as np
arr=np.array([1,2,3,4,5])
for element in arr:
    print(element)
# 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
for row in matrix:
    print(row)
# nnumerated iteration using ndenumerate
import numpy as np
arr = np.array([[1, 2, 3]])
for idx,x in np.ndenumerate(arr):
    print(idx,x)
# using np.nditer for more control
import numpy as np
arr=np.array([[1, 2, 3], [4, 5, 6]])
for x in np.nditer(arr):
    print(x, end='')
# iterating with multiple arrays
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
for x,y in np.nditer([arr1,arr2]):
    print(x,y, end='')

# iterating array with different data types
import numpy as np
arr=np.array([1,2,3])
for x in np.nditer(arr,flags=['buffered'], op_dtypes=['S']):
    print(x)
# sorting using np.sort()
import numpy as np
arr=np.array([3,2,1])
sorted_arr=np.sort(arr)
print(sorted_arr)

matrix = np.array([[3,2,1], [6,5,4]])
sorted_matrix=np.sort(matrix,axis=1)
print(sorted_matrix)
# np.argsort()
arr=np.array([3,1,2,4])
indices=np.argsort(arr)
print(indices)
# np.lexsort()
names=np.array(['Charlie','Alice','Bob'])
scores=np.array([85,92,88])
sorted_indices=np.lexsort((scores,names))
print(sorted_indices)

# np.where()
arr=np.array([1,2,3,4,5])
indices=np.where(arr>3)
print(indices)

#
arr=np.array([1,2,3,4,5])
new_arr=np.where(arr>3,arr*10,arr)
print(new_arr)



# np.extract()
arr=np.array([1,2,3,4,5])
condition=arr>3
extracted=np.extract(condition,arr)
print(extracted)

# statistical functions
# measure of central tendency
# np.array()
import numpy as np
arr=np.array([1,2,3,4,5])
mean=np.mean(arr)
print(mean)

# np.median
median=np.median(arr)
print(median)
# np.mode
from scipy import stats
arr=np.array([1,2,2,4,5])
mode=stats.mode(arr)
print(mode)



# measure of dispersion
# np.std()
arr=np.array([1,2,3,4,5])
std=np.std(arr)
print(std)

# np.var()
arr=np.array([1,2,3,4,5])
variance=np.var(arr)
print(variance)

# np.ptp()
arr=np.array([1,2,3,4,5])
range_val = np.ptp(arr)
print(range_val)
# percentile and quantile
# np.percentile
arr=np.array([1,2,3,4,5])
percentile_50=np.percentile(arr,50)
print(percentile_50)

# np.quantile
arr=np.array([1,2,3,4,5])
quantile_25=np.quantile(arr,0.25)
print(quantile_25)

# correlation and covariance
arr1=np.array([1,2,3,4,5])
arr2=np.array([5,4,3,2,1])
corr_matrix=np.corrcoef(arr1,arr2)
print(corr_matrix)

# cov()
arr1=np.array([1,2,3,4,5])
arr2=np.array([5,4,3,2,1])
cov_matrix=np.cov(arr1,arr2)
print(cov_matrix)

# creating a sseries
import pandas as pd
s=pd.Series([1,2,3,4,5])
s=pd.Series([1,2,3],['a','b','c',])
print(s)

# dataframes
# creating a dataframes
import pandas as pd
data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [25,30,35],
    'Occupation ': ['Engineer', 'Doctor', 'Artist']
}
df = pd.DataFrame(data)
print(df)


# accessing data in dataframes
# selecting a single column (return a series)
print(df['Name'])
# selecting a multiple columns
print([['Name','Age']])

# selecting rows by position
print(df.iloc[0])
# selecting rows by label
print(df.loc[0])
# conditional seection
print(df[df['Age']>25])
# adding a new column
df['Salary']=[70000,80000,75000]
# dropping a column
df=df.drop("Salary", axis=1)

#  from a list of dictionaries
data =[
    {"Name": 'Alice', "Age": 25, "Occupation ": "Engineer"},
    {"Name": 'Bob', "Age": 30, "Occupation ": "Doctor"},
    {"Name": "Charlie", "Age": 30, "Occupation ": "Artist"}
]
df = pd.DataFrame(data)
print(df)

# from a data frame
df_filtered = df[df['Age']>25]
print(df_filtered)

#  from a list of list of 2D arrays
import numpy as np
data =[
    ['Alice', 25, 'Engineer'],
    ['Bob', 30, 'Doctor'],
    ['Charlie', 30, 'Artist']
]

df=pd.DataFrame(data , columns=['Name', 'Age', 'Occupation'])
print(df)

#  creating a dataframe from a 2D numpy array
array_data=np.array([
    ['Alice', 25, 'Engineer'],
    ['Bob', 30, 'Doctor'],
    ['Charlie', 30, 'Artist']
])
df = pd.DataFrame(array_data, columns=['Name', 'Age', 'Occupation'])
print(df)

# head function
import pandas as pd
data = {
    'Name' : ['Alice','Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age' : [25,30,35,40,50,60],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Lawyer', 'Chief', 'Police']
}
df=pd.DataFrame(data)
print(df.head())
print(df.head(3))

# tail function
print(df.tail(3))
print(df.tail())

#
# import pandas aspd
data = {
    'Name' :['Alice','Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age' :[25,30,35,40,50,60],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Lawyer', 'Chief', 'Police']
}
df=pd.DataFrame(data)
# display the data frame
print("Data Frame:")
print(df)
print("\n")
#  get the dimension of the data frame
print("Shape of the Dataframe:")
print(df.shape)
print("\n")

#  get the data types of each column
print("Data Types of the DataFrame : ")
print(df.dtypes)
print("\n")

#  get the column label
print("Column of the Dataframe : ")
print(df.columns)
print("\n")
# preview the first rows
print("First 3 rows of the data frame :")
print(df.head(3))
print("\n")

# get the underlying data as numpy array
print("Values of the DataFrame: ")
print(df.values)
print("\n")




# working with missing data
# isna() or isnull()
# notna() or notnull()
import pandas as pd
data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age' : [25,35,40,45,None],
    'Occupation' : ['Engineer', 'Doctor', 'Artist', 'Lawyer', None]

}
df=pd.DataFrame(data)

# detecting missing data
print("Missing Data(isna):")
print(df.isna())
print("\n")
print("Missing Data(notna):")
print(df.notna())
print("\n")

# dropping missing data
# dropna()
# dropping rows with any missing data
import pandas as pd
data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age' : [25,35,40,45,None],
    'Occupation' : ['Engineer', 'Doctor', 'Artist', 'Lawyer', None]

}
df=pd.DataFrame(data)
df_dropped_rows=df.dropna()
print("Data Frame after dropping rows with any missing values ")
print(df_dropped_rows)
print("\n")

# dropping column s with any missing data
df_dropped_columns=df.dropna(axis=1)
print("Data Frame after dropping columns with any missing values ")
print(df_dropped_columns)
print("\n")

# filling missing data
# filling missing data
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, 35, 40, 45, None],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Lawyer', None]
}

df = pd.DataFrame(data)

# Fill missing values with 'Unknown'
df_filled_value = df.fillna(value='Unknown')

print("Data Frame after filling missing values with 'Unknown'")
print(df_filled_value)
print("\n")

# Forward filling missing values
df_filled_ffill = df.ffill()

print("Data Frame after filling missing values with 'ffill'")
print(df_filled_ffill)
print("\n")

# Backward filling missing values
df_fill_bfill = df.bfill()

print("Data Frame after filling missing values with 'bfill'")
print(df_fill_bfill)
print("\n")

# Replacing 'None' with 'Not Specified' in the DataFrame
df_replaced = df.replace({None: 'Not Specified'})

print("DataFrame after replacing None with 'Not Specified':")
print(df_replaced)
print("\n")

#
import pandas as pd
data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age' : [25,35,40,45,None],
    'Occupation' : ['Engineer', 'Doctor', 'Artist', 'Lawyer', None]

}
df=pd.DataFrame(data)
# single label indexing-accessing a specified eleemnt
print('aGE of the first person : ', df.loc[0,'Age'])
# row indexing - accessing a entire row
print("\n Row with index 2 : ")
print(df.loc[2])
# column indexing
print("\n Occupation column")
print(df['Occupation'])



# Merging and Joining DataFrames;
import pandas as pd

# Creating two sample DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Occupation': ['Artist', 'Lawyer', 'Chef', 'Pilot'],
    'Salary': [70000, 80000, 60000, 90000]
})

# Inner Join - Merging on 'ID' column
inner_merged_df = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Join:")
print(inner_merged_df)
print("\n")


# Outer Join - Merging on 'ID' column
outer_merged_df = pd.merge(df1, df2, on='ID', how='outer')
print("Outer Join:")
print(outer_merged_df)
print("\n")

# Left Join - Merging on 'ID' column
left_merged_df = pd.merge(df1, df2, on='ID', how='left')
print("Left Join:")
print(left_merged_df)
print("\n")

# Right Join - Merging on 'ID' column
right_merged_df = pd.merge(df1, df2, on='ID', how='right')
print("Right Join:")
print(right_merged_df)
print("\n")


# 2. Joining DataFrames
# The join() function in pandas is used to join DataFrames based on their indices. It's similar to the merge() function but is used when you want to join based on the index rather than columns.

# Creating two sample DataFrames with indices
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40]
}, index=[1, 2, 3, 4])

df2 = pd.DataFrame({
    'Occupation': ['Artist', 'Lawyer', 'Chef', 'Pilot'],
    'Salary': [70000, 80000, 60000, 90000]
}, index=[3, 4, 5, 6])

# Join - Joining on index
joined_df = df1.join(df2, how='inner')
print("Join on index (Inner Join):")
print(joined_df)
print("\n")

# Outer Join on index
outer_joined_df = df1.join(df2, how='outer')
print("Join on index (Outer Join):")
print(outer_joined_df)
print("\n")

# Left Join on index
left_joined_df = df1.join(df2, how='left')
print("Join on index (Left Join):")
print(left_joined_df)
print("\n")

# Right Join on index
right_joined_df = df1.join(df2, how='right')
print("Join on index (Right Join):")
print(right_joined_df)

# Working with CSV Files
#1. Reading CSV Files

# Reading a CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Display the first few rows of the DataFrame
print(df.head(50))
print (df.tail())
# Writing the DataFrame to a CSV file
df.to_csv('output.csv')

# Adding Markers to a Plot

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Create a line plot with markers
plt.plot(
    x, y,
    marker='o',
    markersize=10,
    markerfacecolor='red',
    markeredgecolor='blue',   # fixed quote here
    markeredgewidth=2
)

# Adding title and labels
plt.title("Line Plot with Circle Markers")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Show the plot
plt.show()

# line plot
import matplotlib.pyplot as plt
# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
# Creating a line plot
plt.plot(x, y, color='blue', linewidth=2, linestyle='--')
# Adding title and labels
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
# Show the plot
plt.show()

# multiple lines in a plot
# Data for multiple lines
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Plotting multiple lines
plt.plot(x, y1, label='Line 1',  color=(0.1, 0.2, 0.5, 0.7))
plt.plot(x, y2, label='Line 2', color='green')

# Adding labels, title, and legend
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multiple Lines Plot")
plt.legend()

# Show the plot
plt.show()

#
import matplotlib.pyplot as plt
# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
# Create a figure and axis
fig, ax = plt.subplots()
# Set background colors
ax.set_facecolor('#EFEFEF')      # Set plot area background color
fig.patch.set_facecolor('lightblue')  # Set figure background color
# Plotting multiple lines using the axis object
ax.plot(x, y1, label='Line 1', color=(0.1, 0.2, 0.5, 0.7))
ax.plot(x, y2, label='Line 2', marker='o', markerfacecolor='yellow', markeredgecolor='red')
# Adding labels, title, and legend
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_title("Multiple Lines Plot")
ax.legend()
# Show the plot
plt.show()

# colormaps

import matplotlib.pyplot as plt
# Data
x = [1, 2, 3, 4, 5]           # X-coordinates
y = [2, 4, 1, 3, 5]           # Y-coordinates
z = [10, 20, 30, 40, 50]      # Values that determine color

# Scatter plot
plt.scatter(x, y, c=z, cmap='viridis')  # Color points based on 'z' values
plt.colorbar(label='Value (z)')         # Add color scale

# Labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Simple Scatter Plot with Color Mapping')

# Show plot
plt.show()

#
import matplotlib.pyplot as plt
# Data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 35]
y2 = [8, 15, 22, 28, 34]
# Plotting multiple lines with labels
plt.plot(x, y1, label='Series 1', color='blue', marker='o')
plt.plot(x, y2, label='Series 2', color='red', marker='x')
# Add labels, title, and legend
plt.xlabel("Time (s)", fontsize=12, color='blue')
plt.ylabel("Distance (m)", fontsize=12, color='green')
plt.title("Comparison of Two Series Over Time", fontsize=16, fontweight='bold', color='purple')
plt.legend(loc='upper left', fontsize=10)
# Adding custom labels to data points
for i, value in enumerate(y1):
    plt.annotate(f'{value}', (x[i], y1[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, color='blue')
for i, value in enumerate(y2):
    plt.annotate(f'{value}', (x[i], y2[i]), textcoords="offset points", xytext=(0,-15), ha='center', fontsize=10, color='red')
# Show the plot
plt.show()
