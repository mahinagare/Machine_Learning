import numpy as np
import pandas as pd
#24. Refer the dataset "Advertising.csv" and perform following tasks.

#1.i) Read the dataset "Advertising.csv" in data frame.

ad_data = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/datasets/Advertising.csv')
#ii) Print first five records of dataset.


print(ad_data.to_string())
print(ad_data.head(5))
#iii) print last five records from dataset.

print("\n last five records")
print(ad_data.tail(5))

#iv) display the column names of the dataset.
print("\n column names in csv")
print(ad_data.columns)
#v) display last three records from dataset.

print("\n last 3 reoreds from file")
print(ad_data.tail(3))

#vi) display the information about the dataset and analyse the data.
print("\n information of dataset")
print(ad_data.info())

#vii) display data types of each columns.
print("\n display datatype of dataset")
print(ad_data.dtypes)

#viii) check for null values in the dataset and display the sum of null values inside the column.
print("\n null values")
print(ad_data.isnull().sum())

#ix) drop all null values.
print("\n drop null values")
print(ad_data.dropna())
#x) drop a column 'radio' from a dataset and display first ten records.
print("\n drop col radio and dsiplay 1st 10 records")
ad_data = ad_data.drop('radio', axis=1)
print(ad_data.head(10))

#xi) increase the sales by 10% and add a new column "updated_sales" in dataframe.
ad_data['updated_sales'] = ad_data['sales'] * 1.1
print("\n 1st 5 records of updated sales")
print(ad_data.head(5))

#xii) display shape of data.
print(ad_data.shape)



