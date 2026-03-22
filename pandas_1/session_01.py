import numpy as np
import pandas as pd

# series 1D array
# s = pd.Series([1,2,3,4,5],index = ["amam","bob","cat","dog"])

# series are homogenious
# vectorized operations
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([5,6,7,8,9])
print(s1+s2)
# handle missing values with NaN

# mutable values and immutable size
s1[0] = 5
print(s1+s2)
#  we have to create new series if we change something then
changed_s2 = s2.drop(1)
print(changed_s2)



#######----------------------


# dataframe(2D labeled array)
# 1 create dataframe using dictionary
info = {"Name":["sunil","rahul","anil","rahul"],
        "Age":[23,22,21,20],
        "GPA":[9.5,7.9,5.6,7.8]
        }
df = pd.DataFrame(info)
df.index
df.columns
# 2 dataframe can be list of lists

info = [["sunil",23],["rahul",22],["amit",21]]
df = pd.DataFrame(info,columns = ["Name","Age"])
print(df)

# 3. using numpy array
np_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
df = pd.DataFrame(np_array,columns=["a","b","c"])
df

######-------------


# usage with csv & json file from api
# csv is compatable with sql,R and python and work efficently that's use this
df = pd.read_csv("/content/employee_data.csv")
# print(df,type(df))

# head() method -> starting 5 rows
df.head()
# df.tail()  -> end five 5 rows
df.tail(2)
# df.sample() -> random row from data
# df.info()    -> summery of data
tuple_1 = df.shape
# df.describe() -> min,max,mean etc. of all column
# df.columns -> return list of columns
# df.nunique() -> return number of unique values in particular column

#########----------

df = pd.read_csv("/content/globalAirQuality.csv")
df.head().describe()

# columns
df["country"]
df[["city","aqi"]]
# rows
df.loc[0]
df.loc[0:2 ] # start idx: end idx(inclusive)
df.iloc[0:2] # start idx: end idx(exclusive)
# select single scalar value - at&iat

# cells -> rows and cols
# df.loc[0,"aqi"]  -> first row aqi value is print
# df.loc[0,['city','aqi']] -> first row aqi and city value is print
# df.iloc[0,['city','aqi']] -> index error we have to give index instead of 'city' and 'aqi' string
#  iloc index is only numeric values
df.iloc[0,[0,1]]
df.iloc[0:3,0:3]

# select single scalar value -at&iat
df.at[0,'aqi']
df.iat[0,3]

# df['city'] -> give a view of data not a copy
#  all the above give views not a copy so don't be change the data
#  if you want to change then make copy of that data
new_data = df.iloc[0,[0,1]].copy()
new_data # now we can change this data


##########-----------------------

# filtering pf data
import numpy as np
import pandas as pd
df = pd.read_csv("/content/globalAirQuality.csv")
aqi_data = df[(df['aqi']>100) &( df['temperature']>30)]
# df[df['aqi']>100][df['temperature']>30]  another way of get data
aqi_data.head()

# query method for data filteration
#  query bydeault return copy of data no view of data
df.query('aqi>100 and temperature>30') # like a sql command
#  expression as a string
# column based reference
# backticks for col_name with space or special chars
#  Operators(&,|,~,>=,>,<,== etc.)
# @ to reference python vars
#  chained comparisons
aqi_value = 100
df.query('aqi>@aqi_value & temperature>30')[['city','aqi','humidity']]


#######--------------