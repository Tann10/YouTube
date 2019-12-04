import pandas as pd
import numpy as np


# read in the dataset #
df= pd.read_csv('/Users/yunyunjiang/anaconda3/envs/DOOR_classification/YouTube/Data/USvideos.csv',
                       header=0)


# check variable names #
#print(list(df.columns.values))

# print first 5 observations #
#print(df.head())

y=(1/3)*df['views']+(1/3)*df['likes']+(1/3)*df['dislikes']
print(y)
y1=np.array(y)
print(y1)
z=np.matmul(y1.T,y1)
print(z)