#! /usr/bin/python3

import pandas as pd

f = open("pair.txt", "w")
filename = 'steam_reviews.csv'

df = pd.read_csv(filename, usecols=['app_id', 'app_name', 'language'])
df = df[df['language'] == 'english']
df = df.drop(columns='language')

print("WHOLE", len(df))
print("UNIQUE", len(df['app_id'].unique()))

unique = df.drop_duplicates(subset='app_id', keep='first')
print()
#print(unique)

for index, row in unique.iterrows():
    #print(row['app_id'],"\t",row['app_name'])
    f.write(str(row['app_id']) + "\t" + row['app_name'] + "\n") 

