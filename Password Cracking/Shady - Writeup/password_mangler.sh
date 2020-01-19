#!/bin/bash

cat $1 | while read -r passwd; do
	length=$(($(echo $passwd | wc -m)+2))  # Set +n to number of chars to add - 1
	crunch $length $length -t $passwd%%% >> wordlist2.txt  # Set the number of %s to n + 1
done
