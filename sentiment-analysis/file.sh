#! /bin/bash
rm -f ./*.class review.jar

javac -cp $(hadoop classpath) Sentiment_Analysis.java
jar cf review.jar ./*.class

rm -f ./*.class 

hadoop jar review.jar Sentiment_Analysis /data /result
