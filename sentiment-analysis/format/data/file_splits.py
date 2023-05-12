#! /usr/bin/python3
import os

folders = ["./positive/", "./negative/"]
resultant = "./splits/"

def split_file_by_words(input_file, num_parts, index, path):
    filename = folders[index] + input_file
    res = input_file.split('.')[0]
    with open(filename, 'r') as f:
        content = f.read()

    words = content.split()
    num_words_per_part = len(words) // num_parts

    parts = [words[i:i+num_words_per_part] for i in range(0, len(words), num_words_per_part)]
    print("Parts - Written", len(parts))

    for i, part in enumerate(parts):
        part_file_name = f"{path}/{res}_{i+1}.txt"
        with open(part_file_name, 'w') as f:
            f.write(" ".join(part))


for i in range(len(folders)):
    for file in os.listdir(folders[i]):
        directory = file.split('.')[0]
        
        path = resultant + directory
        if not os.path.exists(path):
            os.mkdir(path)
        
        split_file_by_words(file, 10, i, path)
        print(file, "DONE")
    print()
