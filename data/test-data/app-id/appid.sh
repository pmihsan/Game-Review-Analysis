i=1
n=1
while IFS= read -r line
do
	if [ $i -eq $n ] ; then
		echo $line | awk '{print $1}' | tr -s '\n' ', '
		n=$(($n+3))
	fi
	i=$(($i+1))
done < ./$1
echo