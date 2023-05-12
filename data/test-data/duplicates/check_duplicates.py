#!/usr/bin/python3

import os

list = []
app_id=""

for file in os.listdir('./data'):
    filetype = file.split('_')[1].split('.')[1]

    if(filetype == 'json'):
        app_id = str(file.split('_')[1].split('.')[0])
    elif(filetype == 'csv'):
        app_id = str(file.split('_')[0])
    
    list.append(app_id)


print("List has ",len(list))
print("Unique Elements ",len(set(list)))
