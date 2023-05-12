#!/usr/bin/python3 -B
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS
import os
import re

import my_map as mp
mp.initialize()

folder = "../result/"
output = "../images/"

wc = WordCloud(background_color="white", max_words=2000,
               stopwords=STOPWORDS, max_font_size=100,
               random_state=42, width=500, height=500)

for file in os.listdir(folder):

    appid = file.split('_')[0]
    appname = mp.mapping(appid).replace(" ","")
    appname = re.sub(r'\W+', '', appname)

    if not os.path.exists(output + appname):
        os.mkdir(output + appname)

    tp = file.split('_')[1].split('.')[0]
    if tp == "pos":
        tp = "positive"
    else:
        tp = "negative"

    filename = folder + file 
    res = output + appname + "/" + appname + "_" + tp + ".png"
    
    print("TYPE: ",tp)
    print("INPUT: ",filename)
    print("OUTPUT: ",res)
    
    if os.path.exists(res):
        print("EXISTS", end='\n\n')
        #i += 1
        continue
    
    print()
    
    if filename.endswith(".txt"): 
        with open(filename, "r") as txtFile:
            lines = txtFile.readlines()
            words = ""
            for line in lines:
                if(line != '\n'):
                    s = line.split(" word ")
                    if(len(s) == 2):
                        words += s[1].split(" occurred")[0] + " "
            wc.generate(words)
            plt.imshow(wc, interpolation="bilinear")
            plt.axis('off')
            plt.savefig(res, bbox_inches='tight')
    else:
        continue
