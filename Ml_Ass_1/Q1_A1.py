import numpy as pd
import pandas as pd
#1.1. i) Create a list of empids and names (10 employees).

emp_data = {'emp_id':[ 1,2,3,4,5,6,7,8,9,10],
            'name':['mahesh','vishal','arya','prashya','akash',
                    'shruti','apkesha','anurag','puneet','akshay']}
#2.ii) Convert list into Series.

emp_series = pd.Series(emp_data)

#3 print the type of series
print('type of series: ', type(emp_series))

#4. convert the series into dataframe

emp_df = pd.DataFrame(emp_series)

#5. display all records
print("all records: ")
print(emp_df)

#6. display first 5 records

print("\n first five records")
print(emp_df.head(5))

#7. display last five reords
print("\n last five reocrds")
print(emp_df.tail(5))

#8. save into csv file
emp_df.to_csv("emp_details.csv ", index=False)
