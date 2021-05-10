#! /bin/bash

file="./.pathList"

i=1
while read line; do
	export PATH="$PATH:$line"
	i=$((i+1))
done < $file
