# from multiprocessing.reduction import duplicate
import pandas as pd

#*********************Pandas - Cleaning Empty Cells******************
# One way to deal with empty cells is to remove rows that contain empty cells.
# This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
# By default, the dropna() method returns a new DataFrame, and will not change the original.
#If we want to change the original DataFrame, use the inplace = True argument:
print("Return a new Data Frame with no empty cells :- ")
empty_data = pd.read_csv('dirtydata.csv')
# print(empty_data) 
print("Return Data :- ")
print(empty_data.to_string()) #return whole data
print("data without null values")
new_empty = empty_data.dropna() #If we want to change the original DataFrame, use the inplace = True argument:
print(new_empty.to_string())

# empty_data2 = pd.read_csv('dirtydata1.csv')
# print("Return Data :- ")
# print(empty_data2.to_string()) #return whole data
# print("Delete all row with emplty cell (Changes made in csv file) :- ")
# empty_data2.dropna(inplace=True) #If we want to change the original DataFrame, use the inplace = True argument:
# print(empty_data2.to_string())

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:
empty_data1 = pd.read_csv('dirtydata.csv')
print('Replace NULL values with the number 130:')
empty_data1.fillna('hello', inplace=True)
print(empty_data1)

#***************Replace Only For Specified Columns***************
#To only replace empty values for one column, specify the column name for the DataFrame:

print("Replace NULL values in the Calories columns with the number 130 :- ")
empty_data3 = pd.read_csv('dirtydata2.csv')
empty_data3['Calories'].fillna('Hii', inplace = True)
print(empty_data3.to_string())

#**************Replace Using Mean, Median, or Mode************************
# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column
# Mean = the average value (the sum of all values divided by number of values).
print("Calculate the MEAN, and replace any empty values with it :- ")
mean_data = pd.read_csv('dirtydata2.csv')
mean = mean_data['Calories'].mean() #it calculate mean based on the column
# print(mean)
mean_data['Calories'].fillna(mean, inplace = True) #replace empty value by mean in specified column
print(mean_data.to_string())

# Median = the value in the middle, after you have sorted all values ascending.
print("Calculate the MEDIAN, and replace any empty values with it :-")
median_data = pd.read_csv('dirtydata2.csv')
median = median_data['Calories'].median() #it calculate median based on the column
# print(median)
median_data['Calories'].fillna(median, inplace = True) #replace empty value by median in specified column
print(median_data.to_string())

#Mode = the value that appears most frequently.
print("Calculate the MODE, and replace any empty values with it :- ")
mode_data = pd.read_csv('dirtydata2.csv')
mode = mode_data['Calories'].mode()[0] #it calculate mode based on the column [0] signify the label/index number. it must be [0] or strating index value
print(mode)
mode_data['Calories'].fillna(mode, inplace=True) #replace empty value by mode in specified column
print(mode_data.to_string())

#********************Cleaning Data of Wrong Format**********************
# Convert Into a Correct Format
# In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:
# Pandas has a to_datetime() method to convert all cells in the 'Date' column into dates.:
print("Convert to date :- ")
convert_data = pd.read_csv('dirtydata2.csv')
convert_data['Date'] = pd.to_datetime(convert_data['Date'])
print(convert_data.to_string())
print("Remove the null column (column having Duration 45 and index 22):- ")
convert_data.dropna(subset=['Date'], inplace=True) #it remove index 22 having empty date cell
print(convert_data.to_string())

# *********************Fixing Wrong Data***********************************
# Replacing Values
# One way to fix wrong values is to replace them with something else.
# In our datafrmae, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
print("Set Duration = 45 in row 7 :- ")
fixing_data = pd.read_csv('dirtydata2.csv')
fixing_data.loc[7, 'Duration'] = 45
print(fixing_data.to_string())

print("Loop through all values in the Duration column. If the value is higher than 120, set it to 120:")
fixing_data1 = pd.read_csv('dirtydata2.csv')
for x in fixing_data1.index:
    if fixing_data1.loc[x, 'Duration'] > 120:
        fixing_data1.loc[x, 'Duration'] = 120
print(fixing_data1.to_string())

# Removing Rows
# Another way of handling wrong data is to remove the rows that contains wrong data.
print("Delete rows where Duration is higher than 120 :- ")
remove_data = pd.read_csv('dirtydata2.csv')
for x in remove_data.index:
    if remove_data.loc[x, 'Duration'] > 120:
        remove_data.drop(x, inplace=True) #remember to include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy
print(remove_data.to_string()) #drop is used to delete a row by index value

#*****************************Removing Duplicates**************************
# To discover duplicates, we can use the duplicated() method.
# The duplicated() method returns a Boolean values for each row.
print("Returns True for every row that is a duplicate, othwerwise False :- ")
dupli_data = pd.read_csv('dirtydata2.csv')
print(dupli_data.duplicated()) #it return the True for duplicate rows otherwise false
dupli_data.drop_duplicates(inplace=True) #it delete the duplicates row
print(dupli_data.to_string())








