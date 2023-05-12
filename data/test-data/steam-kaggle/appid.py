#! /usr/bin/python3
import os

steam="./csv"
for file in os.listdir(steam):
    id = file.split('_')[0]
    print(id)

print()
