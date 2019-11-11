import pandas as pd


# read in the dataset #
df= pd.read_csv('/Users/yunyunjiang/Documents/machine learning I/project/USvideos.csv',
                       header=0)

# check variable names #
print(list(df.columns.values))

# print first 5 observations #
print(df.head())

y=(1/3)*df['views']+(1/3)*df['likes']+(1/3)*df['dislikes']
print(y)

df2=df[['category_id','views','likes','dislikes','comment_count']]
print(df2.head())


# plot heatmap #

import numpy as np
import seaborn as sns
#%matplotlib inline
import matplotlib.pyplot as plt

# Get the correlation matrix, where each entry is the Pearson product-moment correlation coefficient
cm = np.corrcoef(df2.T)

plt.figure(figsize=(25, 25))

hm = sns.heatmap(cm,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size': 15},
                 yticklabels=df.columns,
                 xticklabels=df.columns)

plt.tight_layout()
plt.show()
