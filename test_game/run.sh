if [ "$1" = "" ] ; then
	echo "./run.sh input-directory"
elif [ -f $PWD/result/$1.txt ] ; then
	echo "File Already Found"
else
	echo "RUNNING..."
	echo
	mahout seqdirectory -i /game_reviews/$1 -o /game_reviews/$1/output -c UTF-8

	mahout seq2sparse -i /game_reviews/$1/output/ -o /game_reviews/$1/vector/ -wt TF

	mahout rowid -i /game_reviews/$1/vector/tf-vectors -o /game_reviews/$1/sparse_vectors_cvb

	hdfs dfs -mkdir /game_reviews/$1/out

	hadoop fs -mv /game_reviews/$1/sparse_vectors_cvb/docIndex /game_reviews/$1/out/sparse-verctors-docIndex-latest1

	mahout cvb -i /game_reviews/$1/sparse_vectors_cvb -o /game_reviews/$1/lda/ -k 10 -x 1 -nt 500000 -mt /game_reviews/$1/temp/ -dt /game_reviews/$1/lda-topics -dict /game_reviews/$1/vector/dictionary.file-0

	mkdir -p $PWD/lda_output

	mahout vectordump -i /game_reviews/$1/lda-topics/part-m-00000 -o $PWD/lda_output/part-m-00000 -vs 10 -p true -dt sequencefile -sort /game_reviews/$1/test-lda-topics/ -c csv -d /game_reviews/$1/vector/dictionary.file-0

	mkdir -p $PWD/lda_output/words
	
	mahout vectordump -i /game_reviews/$1/lda/part-m-00000 -o $PWD/lda_output/words/part-m-00000 -dt sequencefile -c csv -d /game_reviews/$1/vector/dictionary.file-0 -sort /game_reviews/$1/test-lda-topics/

	for i in $(seq 9) ;
	do
		mahout vectordump -i /game_reviews/$1/lda/part-m-0000$i -o $PWD/lda_output/words/part-m-0000$i -dt sequencefile -c csv -d /game_reviews/$1/vector/dictionary.file-0 -sort /game_reviews/$1/test-lda-topics/

	done
	java TopicTermDistribution.java $PWD > $PWD/result/$1.txt
	make clean
fi
