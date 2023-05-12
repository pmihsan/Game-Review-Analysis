#!/bin/bash

# Filter only the sentiment score
cat part-r-00000 | awk -F '----->' '{print $2}' > result.txt

# Remove Trailing white spaces
sed -i -e 's/^[[:space:]]*//g' result.txt

# Set the filename
filename="result.txt"

# Use awk to filter the positive, negative, and neutral numbers
positive=$(awk '{ if($1>0) print $1 }' $filename | wc -l)
negative=$(awk '{ if($1<0) print $1 }' $filename | wc -l)
neutral=$(awk '{ if($1==0) print $1 }' $filename | wc -l)

# Print the results
echo "Positive reviews: $positive"
echo "Negative reviews: $negative"
echo "Neutral reviews: $neutral"

