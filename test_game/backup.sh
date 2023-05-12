#!/bin/bash

mkdir data
mkdir -p data/part
# code files
cp Makefile *.sh *.java cloud/*.py data/
cp output/*.java output/*.sh data/part
tree data | tee data/map.txt

tar cf ~/data_backup.tar.gz data/
rm -r data
