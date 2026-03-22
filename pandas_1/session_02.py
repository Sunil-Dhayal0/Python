# cleaning of data -> handle missing values
df = pd.read_csv("/content/raw_data.csv")
# 1. handle missing values
print(df)
# df.isnull()
# df.isna()   both are same
df.isnull().sum()   # print number of missing values with col_heading
df.dropna() # row drop -> whole row will drop if we use this command
df.dropna(axis=1)  # drop column which contain the NAN values
df.fillna(0)
df['age'].fillna(df['age'].mean()) # fill the NAN value with the mean() value
# forward fill
df.fillna(method='ffill')
# backward fill
df.fillna(method='bfill')




######---------------------

# feature engineering -> transforming data
# 1.apply() -> higher order function because take input another function that is lambda
df2 = df.copy()
df2["tax"] = df2["income"].apply(lambda x:"20%" if x >= 6000 else "10%" )
df2
# 2.map()
gender_map = {"Male":"M","Female":"F","Unknown":"U"}
df2["gender"] = df2['gender'].map(gender_map)
df2
# 3.assign()
df2.assign()
# 4.replace(old,new)

#######---------------


import pandas as pd
df = pd.read_csv("/content/raw_data.csv")
df2 = df.copy()

df2["tax"] = df2["income"].apply(lambda x:"20%" if x>=60000 else "10%")

df2["new_income"] = df2.apply(
    lambda x: x["income"] + x["income"] * 20 // 100 if x["tax"] == "20%"
    else x["income"] + x["income"] * 10 // 100,
    axis=1
)
df2.columns = ["Id","Name","Age","Country","Gender","Salary","Tax","New_Income"]
df2.rename(index = {1:"First"})
df2['New_Income'].sort_values()
df2.sort_values(["New_Income","Age"])

# ranking

df2['ranking'] = df2['Salary'].rank(ascending=False)
df2

# write data to csv file
df3 = df.copy()
df3.drop_duplicates()
df3.dropna()
df3 = df3.sort_values('income')

df3 = df3.reset_index(drop=True)
print(df3)
df3.to_csv('clean_data.csv')

########---------------------


# important things
# groupby
df4 = df.copy()
df4.groupby('country')
df4.groupby(['country','gender'])