#! /usr/bin/python3
import os
import numpy as np
import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

c=0
pos_count=0
neg_count=0
res = open("part-r-00000", 'r')
pos= "./data/positive/"
neg = "./data/negative/"


while True:
    line = res.readline();
    if not line:
        break

    data = line.split(':::')
    l = []
    if(len(data) == 3):
        sentences=sent_tokenize(data[1])

        sentences_clean=[re.sub(r'[^\w\s]','',sentence.lower()) for sentence in sentences]
        stop_words = stopwords.words('english')
        sentence_tokens=[[words for words in sentence.split(' ') if words not in stop_words] for sentence in sentences_clean]
        
        for words in sentence_tokens:
            for i in range(len(words)):
                if(words[i].isascii() and words[i].isalpha()):
                    l.append(words[i])
    else:
        continue

    c += 1
    '''
    review = data[1].split(' ')
    for i in range(len(review)):
        if(review[i].isascii() and review[i].isalpha() and len(review[i]) > 4):
            l.append(review[i].lower())
    '''
    if(len(data[2]) > 0 and int(data[2]) > 0):
        pos_count += 1
        #print("Positive Review", data[0], int(data[2]))
        path_to_file = pos + data[0] + "_pos.txt"
        if(os.path.isfile(path_to_file)):
            pos_fp = open(path_to_file, 'a')
        else:
            pos_fp = open(path_to_file, 'w')

        for k in range(len(l)):
            pos_fp.write(l[k] + " ")
        pos_fp.close()
    
    elif (len(data[2]) > 0 and int(data[2]) < 0):
        neg_count += 1
        #print("Negative Review", data[0], int(data[2]))
        path_to_file = neg + data[0] + "_neg.txt" 
        if(os.path.isfile(path_to_file)):
            neg_fp = open(path_to_file, 'a')
        else:
            neg_fp = open(path_to_file, 'w')

        for k in range(len(l)):
            neg_fp.write(l[k] + " ")
        neg_fp.close()

    l.clear()

print("Positive", pos_count)
print("Negative", neg_count)
print(c)
print()
res.close()
