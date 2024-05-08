import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1. Consider each of following datasets and do below operations.
# i) Read the dataset.
# ii) Display first 5 and last 5 records.
# iii) Display info and describe the dataset.
# iv) Find out null values.
# v) Plot Various graphs. e.g. barchart, scatterplot, histogram, lineplot, pairplot and all other.
# vii)  Find out correlation and covariance in the dataset.

# i) ToyotaCorolla.csv
# ii) Engine.csv
# iii) delivery_time.csv
# iv) SAT-GPA.csv
# v) TvMarketing.csv
# vi) NewspaperData.csv
# vii) claimants.csv
# viii) framingham.csv
# ix) crime_data.csv
# x) Universities.csv
# xi) wine.csv
# xii) glass.csv
#toyota_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/ToyotaCorolla.csv')
# Engine_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/Engine.csv')
# delivery_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/delivery_time.csv')
# SAT_GPA_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/SAT-GPA.csv')
# Tv_Maerketing_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/TvMarketing.csv')
# NewspaperData_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/NewspaperData.csv')
# claimants_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/claimants.csv')
# framingham_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/framingham.csv')
# crime_data_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/crime_data.csv')
# universities_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/Universities.csv')
# wine_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/wine.csv')
#glass_df = pd.read_csv('/media/hp/New Volume/DBDA/DBDA 2023/ML/Assignment/glass.csv')

# print(toyota_df.to_string())
df = pd.read_csv(r"/home/hp/ML_Ass_2/ToyotaCorolla.csv")
print(df.head(5))
print(df.tail(5))
#  Display info and describe the dataset.
print(df.info())
print(df.describe())

#Find out null values.
print(df.isnull().sum())
# BAR Charts
plt.figure(figsize = (10,5))
df['Model'].value_counts().plot(kind = 'bar')
plt.title('Model distribution')
plt.xlabel('Model1')
plt.ylabel('Count')
plt.show()

#scatter plt
plt.figure(figsize=(10,5))
plt.scatter(df['Mileage'],df['price'])
plt.title('Milege vs price')
plt.xlabel('mileage')
plt.ylabel('price')
plt.show()

#histogram
plt.figure(figsize=(10,5))
df['price'].hist()
plt.title('price distribution')
plt.xlabel('price')
plt.ylabel('frquency')
plt.show()

#line plt
plt.figure(figsize=(10,5))
df.sort_values('price').plot(x = 'Model',y ='price',kind  = 'line')
plt.title('price trend by model')
plt.xlabel('model')
plt.ylabel('price')
plt.show()

#pairplot
plt.figure(figsize=(10,5))
sns.pairplot(df)
plt.show()

print(df.corr())
print(df.cov())