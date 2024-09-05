import pandas as pd

#Display version using __version__
print(pd.__version__)

#***************Pandas Series******************
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.
print("Create a simple Pandas Series from a list :- ")
serli = [0, 1, 2, 3, 4]
print(pd.Series(serli))
ser = pd.Series(serli)
print("Fetching by index :- ")
print(ser[2])

#***************Create Labels*********************
# If nothing else is specified, the values are labeled with their index number. 
# First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.
# With the index argument, you can name your own labels.
print("Create a simple Pandas Series from a list :- ")
serli = [0, 1, 2]
print(pd.Series(serli, index=['number', 'number1', 'number2']))
ser = pd.Series(serli, index=['number', 'number1', 'number2'])
print("Return the index value of the Series:")
print(ser['number1'])

# Create a simple Pandas Series from a dictionary.
print("Create a simple Pandas Series from a dictionary using Series() method :- ")
ser_data = {
    'First Name' : "Toney",
    'Last Name' : "Stark",
    'Age' : 34,
    'Gender' : "Male"
}
print(pd.Series(ser_data)) #The keys of the dictionary become the labels.

# To select only some of the items in the dictionary, use the index argument and specify only the items you want to include in the Series.
print("Create a simple Pandas Series from a dictionary :- ")
ser_data = {
    'First Name' : "Toney",
    'Last Name' : "Stark",
    'Age' : 34,
    'Gender' : "Male"
}
print(pd.Series(ser_data, index=['First Name', 'Last Name']))

#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# To display the data in table view 
print("To display the data in table using DataFrame() method :-")
my_data = {
    'Name' : ['Avnish', 'Ananya', 'Jack'],
    'Age' : [34, 23, 28]
}
data_table = pd.DataFrame(my_data)
print(data_table)

# To remove first column
# my_data = {
#     'Name' : ['Avnish', 'Ananya', 'Jack'],
#     'Age' : [34, 23, 28]
# }
# data_table = pd.DataFrame(my_data)
# # data_table.drop(data_table.columns[0], axis=1, inplace=True)
# print(data_table)

#Pandas use the loc attribute to return one or more specified row(s)
print("To display the data in table using DataFrame() method :-")
my_data = {
    'Name' : ['Avnish', 'Ananya', 'Jack'],
    'Age' : [34, 23, 28]
}
data_table = pd.DataFrame(my_data)
print(data_table)
print("display by row") #refer to the row index:
print(data_table.loc[0]) #This example returns a Pandas Series.
# print("\n")
print("display by list of row")
print(data_table.loc[[0, 2]]) #use a list of indexes, When using [], the result is a Pandas DataFrame.

# Named Indexes
# With the index argument, you can name your own indexes.
print("Add a list of names to give each row a name :-")
my_data = {
    'Name' : ['Avnish', 'Ananya', 'Jack', 'Pater', 'Steph', 'Roger', 'Bucky', 'Caspian'],
    'Age' : [34, 23, 28, 50, 23, 30, 46, 43]
}
data_table = pd.DataFrame(my_data, index=['Person1', 'Person2', 'Person3', 'Person4', 'Person5', 'Person6', 'Person7', 'Person8'])
print(data_table)
#Use the named index in the loc attribute to return the specified row(s) :
print("Return Person2 :-")
print(data_table.loc['Person2'])

print("to return the entire DataFrame. :-")
print(data_table.to_string()) #It return the entire dataframe

print("returning the headers and the first 6 rows of a DataFrame. :- ")
print(data_table.head(6)) # It return the top 6 rows. 5 rows are returned if you do not specify the number

print("returning the last 5 rows of a DataFrame. :- ")
print(data_table.tail(5)) #it return last 5 rows

#******************Read CSV Files**********************
#A simple way to store big data sets is to use CSV files (comma separated files).
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
print("Load the CSV into a DataFrame :- ")
csv_data = pd.read_csv('data.csv')
print(csv_data) #If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
# print(csv_data.to_string()) #use to_string() to print the entire DataFrame.
print(csv_data.head(10))

# max_rows
# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with the pd.options.display.max_rows statement.
print("Check the number of maximum returned rows :- ")
print(pd.options.display.max_rows)

#We can change the maximum rows number with the same statement.
print("Increase the maximum number of rows to display the entire DataFrame :- ")
# pd.options.display.max_rows = 100
pd.options.display.max_rows = 200 #we have to set max rows greater than the total rows from csv file
csv_data = pd.read_csv('data.csv')
print(csv_data)

# Info About the Data
# The DataFrames object has a method called info(), that gives you more information about the data set.
print("information about the data set (CSV file):- ")
print(csv_data.info())

#*****************************Pandas Read JSON**********************
# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.
print("Load the JSON file into a DataFrame :- ")
json_data = pd.read_json('data.json')
# print(json_data)
print(json_data.to_string()) #use to_string() to print the entire DataFrame.
print("Return first 10 rows of json data:- ")
print(json_data.head(10)) #bydefault it return first 5 rows
print("Return last 10 rows of json data :- ")
print(json_data.tail(10)) #bydefault it return last 5 rows

# Info About the Data
# The DataFrames object has a method called info(), that gives you more information about the data set.
print("information about the data set (JSON file) :- ")
print(json_data.info())






