#!/bin/bash
dir=($(hdfs dfs -ls /game_reviews | awk '{print $8}' | awk -F'/' '{print $3}'))

read -p "Enter start range " s
read -p "Enter end range " e

if [[ $s -gt 630 || $e -gt 630 ]] ; then
	echo "Invalid range"
	exit
fi

d1=`date`
st=$s

echo "START: $s, END: $e, RANGE: $((e-s+1))"
echo
while [ $s -le $e ] ; 
do
	echo "STARTING ($s) -> ${dir[$((s-1))]}"
	./run.sh  ${dir[$((s-1))]}
	echo "FINISHED ($s) -> ${dir[$((s-1))]}"
	s=$(($s+1))
	echo
done

d2=`date`
echo -e "START: $st, END: $e, RANGE: $((e-st+1))\n$d1\n$d2\n" > hist.txt
echo
echo "COMPLETED"
