#! /usr/bin/python3
import os
import pandas as pd

f = open("reviews", "w")
csvDir = './csv/'

for file in os.listdir(csvDir):
    filename = csvDir + file
    app_id = str(file.split('_')[0])
    
    print("File: ",file)
    print(app_id)

    df = pd.read_csv(filename, usecols=['recommendationid', 'review'])
    for index, row in df.iterrows():
        recom_id = str(row['recommendationid'])
        review = row['review']

        res = str("{\"id\": \"" + recom_id + "\", \"review\": \"" + ''.join(str(review).splitlines()) + "\", \"game_id\": \"" + app_id + "\"}")

        f.write(res)
        f.write("\n")

    print()

f.close()
