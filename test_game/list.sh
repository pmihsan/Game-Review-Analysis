#!/bin/bash
dir=($(hdfs dfs -ls /game_reviews | awk '{print $8}' | awk -F'/' '{print $3}'))

read -p "Enter start range " s
read -p "Enter end range " e

if [[ $s -gt 630 || $e -gt 630 ]] ; then
	echo "Invalid range"
	exit
fi

echo "START: $s, END: $e, RANGE: $((e-s+1))"
echo
while [ $s -le $e ] ; 
do
	echo "$s) ${dir[$((s-1))]}"
	s=$(($s+1))
done
