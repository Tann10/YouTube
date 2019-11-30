import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
import json
# read files
unprocessed_df = pd.read_csv("Data/US_videos.csv")
with open("Data/US_category_id.json") as train_file:
    categories = json.load(train_file)["items"]

cat_dict = {}
for cat in categories:
    cat_dict[int(cat["id"])] = cat["snippet"]["title"]

unprocessed_df['category_name'] = unprocessed_df['category_id'].map(cat_dict)




check = json_normalize(data = dict_train['items'], record_path='snippet', meta=['title'], errors='ignore')

train = pd.DataFrame.from_dict(dict_train, orient='index')
train.reset_index(level=0, inplace=True)
train.columns
json_normalize(train[2])

data = json.loads("Data/US_category_id.json")


category_id = pd.read_json("Data/US_category_id.json")

check = pd.DataFrame(category_id.kind.values)


json_normalize(category_id)

type(category_id['items'][0])
# converting to df
category_id_2 = pd.DataFrame.from_dict(category_id['items'], orient='columns')
category_id.reset_index(level=0, inplace=True)
category_id_2.head()
type(category_id)
pd.DataFrame(data=[*dict.values()], columns=['firstcolumn','secondcolumn', 'thirdcolumn'])

