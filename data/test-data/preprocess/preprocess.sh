awk -F "," '{OFS = ",";print $1,$11}' result.csv
