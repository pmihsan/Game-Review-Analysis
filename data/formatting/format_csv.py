#! /usr/bin/python3

import pandas as pd
list = []

filename = 'steam_reviews.csv'
f = open("reviews", "w") 

df = pd.read_csv(filename, usecols=['app_id','review_id', 'review', 'language'])
df = df[df['language'] == 'english']

print(len(df))
start_app_id = "292030"

for index, row in df.iterrows():
    if row['app_id'] in list:
        continue

    if start_app_id != row['app_id']:
        list.append(start_app_id)
        start_app_id = row['app_id']

    if(row['language'] == 'english'):
        recom_id = str(row['review_id'])
        review = row['review']
        app_id = str(row['app_id'])


        res = str("{\"id\": \"" + recom_id + "\", \"review\": \"" + ''.join(str(review).splitlines()) + "\", \"game_id\": \"" + app_id + "\"}")

        f.write(res)
        f.write("\n")

print("List has ",len(list))
print("Unique Elements ",len(set(list)))
