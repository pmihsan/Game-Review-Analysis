#!/usr/bin/python3
import os

f = open("pair.txt", "r")
hm = {}

def initialize(): 
    for line in f.readlines(): 
        values = line.split('\t')

        key = values[0]
        val = values[1].strip()
        hm[key] = val

def mapping(k):
    if k in hm:
        return hm[k]
    else:
        return "NA"
