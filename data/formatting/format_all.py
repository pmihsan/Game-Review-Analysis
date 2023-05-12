#! /usr/bin/python3

import os
import json
import pandas as pd

list = []
dir="./data/"
f = open("reviews", "w")

for file in os.listdir(dir):

    filename = dir + file
    filetype = file.split('_')[1].split('.')[1]
    fr = file

    print("FILE -> ",file)

    if(fr == 'steam_reviews.csv'):
        pass
'''
        df = pd.read_csv(filename, usecols=['app_id','review_id', 'review', 'language'])

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
'''
    elif(filetype == 'json'):
        app_id = str(file.split('_')[1].split('.')[0])

        if app_id in list:
            continue

        list.append(app_id)
        with open(filename) as jsonFile:
            data = json.load(jsonFile)

        #print(type(jsonFile))

        json_data = data["reviews"]
        #print(type(json_data))
        for x in json_data:
        
            if(json_data[x]["language"] == 'english'):
                d = dict()
                d["id"] = json_data[x]["recommendationid"]
                d["review"] = json_data[x]["review"]
                d["game_id"] = app_id

                res = str("{\"id\": \"" + d["id"] + "\", \"review\": \"" + ''.join(str(d["review"]).splitlines()) + "\", \"game_id\": \"" + d["game_id"] + "\"}")
                f.write(res)
                f.write("\n")
        print(app_id)

    elif(filetype == 'csv'):
        app_id = str(file.split('_')[0])

        if app_id in list:
            continue
        else:
            list.append(app_id)

            df = pd.read_csv(filename, usecols=['recommendationid', 'review', 'language'])
           
            for index, row in df.iterrows():
                if(row['language'] == 'english'):
                    recom_id = str(row['recommendationid'])
                    review = row['review']

                    res = str("{\"id\": \"" + recom_id + "\", \"review\": \"" + ''.join(str(review).splitlines()) + "\", \"game_id\": \"" + app_id + "\"}")
                    
                    f.write(res)
                    f.write("\n")
        
        print(app_id)
    
    print()
    
print("List has ",len(list))
print("Unique Elements ",len(set(list)))
