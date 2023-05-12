if [ "$1" = "" ] ; then
	echo "./run.sh input-directory"
elif [ -d $PWD/part_data/$1 ] ; then
	echo "File Already Found"
else
	mkdir -p $PWD/part_data/$1/lda_output

	mahout vectordump -i /game_reviews/$1/lda-topics/part-m-00000 -o $PWD/part_data/$1/lda_output/part-m-00000 -vs 10 -p true -dt sequencefile -sort /game_reviews/$1/test-lda-topics/ -c csv -d /game_reviews/$1/vector/dictionary.file-0

	mkdir -p $PWD/part_data/$1/lda_output/words
	
	mahout vectordump -i /game_reviews/$1/lda/part-m-00000 -o $PWD/part_data/$1/lda_output/words/part-m-00000 -dt sequencefile -c csv -d /game_reviews/$1/vector/dictionary.file-0 -sort /game_reviews/$1/test-lda-topics/

	for i in $(seq 9) ;
	do
		mahout vectordump -i /game_reviews/$1/lda/part-m-0000$i -o $PWD/part_data/$1/lda_output/words/part-m-0000$i -dt sequencefile -c csv -d /game_reviews/$1/vector/dictionary.file-0 -sort /game_reviews/$1/test-lda-topics/

	done
	java TopicProbability.java $PWD/part_data/$1 > $PWD/part_data/$1/lda_output/$1_prob.txt
	java TopicTermDistribution.java $PWD/part_data/$1 > $PWD/part_data/$1/lda_output/$1_term.txt
fi
