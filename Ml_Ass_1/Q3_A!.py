import pandas as pd
import numpy as np

df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/Salaries .csv')
#1. 1st 5 records
print(df.head(5))

#2. 1st 10 records

print(df.head(10))

#3.iv) display last five records.
print(df.tail(5))

#4. v) display last ten records.
print(df.tail(10))

#5. vi) display the columns inside the dataset.

print(df.columns)
#vii) display shape of data.
print(df.shape)

#viii) describe the dataset.
print(df.describe())
#ix) display the information about the dataset and analyse the data.
print(df.info())

#x) display types of each columns.
print(df.dtypes)

#xi) Find out maximum,minimum,mean,median,standard deviation value of each column.
#print(df.agg(['max', 'min','mean', 'median', 'std']))
print("\n max, min, mean, median, std")
print(df.max())
print(df.min())
print(df.mean())
print(df.median())
print((df.std()))
#xii) check for null values in the dataset and display the sum of null values inside the column.

print(df.isnull().sum())

#xiii) Replace all null values by mean or mode acoording to the type of column.
# print(df.fillna(df.mode(), inplace=True))
#
# print("\n null values after filling")
# print(df.isnull().sum())

for col in df.columns:
    if df[col].dtype =='object':
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].mean(),inplace=True)
print("\n after filling null values")
print(df.head())