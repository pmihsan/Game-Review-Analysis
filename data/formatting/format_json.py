#! /usr/bin/python3
import os
import json
f = open("reviews", "w")

for file in os.listdir('steam-reviews'):
    file = './steam-reviews/' + file
    print("file ->",file)
    
    #game_id = file[len(file) - 11:]
    #game_id = game_id[0:6]

    app_id = file.split('_');
    app_id = app_id[1].split('.')

    #print(app_id[0])
    game_id = app_id[0]

    with open(file) as jsonFile:
        data = json.load(jsonFile)

        print(type(jsonFile))
        
        json_data = data["reviews"]
        print(type(json_data))
        for x in json_data:
            #d1 = json.load(json_data.get(x))
            #print(json_data[x])
            '''
            print()
            print(game_id)
            print(json_data[x]["recommendationid"])
            print(json_data[x]["review"])
            '''
            d = dict()
            d["id"] = json_data[x]["recommendationid"]
            d["review"] = json_data[x]["review"]
            d["game_id"] = game_id

            res = str("{\"id\": \"" + d["id"] + "\", \"review\": \"" + ''.join(str(d["review"]).splitlines()) + "\", \"game_id\": \"" + d["game_id"] + "\"}")
            f.write(res)
            f.write("\n")
    print()
f.close()

'''
    reviews = json_data["reviews"]
    for x in reviews:
        keys = x.keys()
        #print(keys)

    #json_format_str = json.dumps(data, indent=4)
    #print(json_format_str)
''' 
'''
    json_data = json.load(data)
    print(json_data)
'''

