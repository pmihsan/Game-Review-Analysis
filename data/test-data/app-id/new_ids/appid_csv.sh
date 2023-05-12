l=1
while IFS= read -r line
do
	if [[ $l -ge $2  && $l -le $3 ]]; then
		echo $line | awk -F "," '{print $1}' | tr -s '\n' ', '
	fi
	l=$(($l + 1))
done < ./$1
echo $l
echo
