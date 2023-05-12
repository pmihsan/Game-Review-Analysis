#! /usr/bin/python3
import os

csv = './csv/'

for file in os.listdir(csv):
    
    filename = file.split('_')
    app_id = str(filename[0])
    app_name = str(filename[1].split('.')[0])
    
    print(app_id,app_name,sep='\t')

print()
