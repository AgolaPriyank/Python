import pandas as pd
import numpy as np

# print(pd.__version__)

df = pd.DataFrame(np.arange(0, 20).reshape(5, 4), 
                  index=['ROW1', 'ROW2', 'ROW3', 'ROW4', 'ROW5'], 
                  columns=['COL1', 'COL2', 'COL3', 'COL4'])

# print(df)

# use this method we create csv file of datafream data
# df.to_csv("Test1.csv")

# use this method fatache the data from datafream
# print(df.loc['ROW1'])

# print(type(df.loc['ROW1']))

# print(df.iloc[0:3,0:2])
# print(type(df.iloc[0:3,0:2]))

# print(df.iloc[0:2,0])
# print(type(df.iloc[0:2,0]))

# print(df.iloc[:,1:])

# print(df.iloc[:,:].values)
# print(df.iloc[:,:].values.shape)


# print(df.isnull().sum())

# print(df['COL1'].unique())

print(df[['COL1','COL2']])