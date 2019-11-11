import pandas as pd


# read in the dataset #
df= pd.read_csv('/Users/yunyunjiang/anaconda3/envs/DOOR_classification/YouTube/Data/USvideos.csv',
                       header=0)


# check variable names #
print(list(df.columns.values))

# print first 5 observations #
print(df.head())

y=(1/3)*df['views']+(1/3)*df['likes']+(1/3)*df['dislikes']
print(y)

df2=df[['category_id','views','likes','dislikes','comment_count']]
print(df2.head())

#########################################
### check correlation among features ####
#########################################

# plot heatmap #

import numpy as np
import seaborn as sns
#%matplotlib inline
import matplotlib.pyplot as plt

# Get the correlation matrix, where each entry is the Pearson product-moment correlation coefficient
cm = np.corrcoef(df2.T)
print(cm)


plt.figure(figsize=(10, 10))

hm = sns.heatmap(cm,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size': 15},
                 yticklabels=df2.columns,
                 xticklabels=df2.columns)

plt.tight_layout()
plt.show()



#########################################################
### handling categorical features in the combined data ##
#########################################################


# Print the unique value and their number for each feature
for j in range(df.shape[1]):
    print(df.columns[j] + ':')
    print(df.iloc[:, j].value_counts(), end='\n\n')

#categorical feature checker #

def categorical_feature_checker(df, target, dtype):
    """
    The categorical feature checker

    Parameters
    ----------
    df : dataframe
    target : the target
    dtype : the type of the feature

    Returns
    ----------
    The categorical features and their number of unique value
    """

    feature_number = [ [ feature, df [ feature ].nunique () ]
                       for feature in df.columns
                       if feature != target and df [ feature ].dtype.name == dtype ]

    print ( '%-30s' % 'Categorical feature', 'Number of unique value' )
    for feature, number in sorted ( feature_number, key = lambda x: x [ 1 ] ):
        print ( '%-30s' % feature, number )

    return feature_number

feature_number = categorical_feature_checker(df2, 'views', 'object')

print(feature_number)