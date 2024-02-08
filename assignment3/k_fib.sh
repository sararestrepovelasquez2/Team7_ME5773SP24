#!/bin/bash
#
#================================================================================
# ITEM 6
#
#
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez
#
# Last modification date: 02/08/2024
# Version: 1.0
#================================================================================
#
# Ask the user to input a number
N=$1

echo The K-Fibonacci series for K = $N:

k_Fib=()

# Number of index show in series = N+1+x
x=5

sum=$N

# Compute the K-Fibonacci series
if [[ $N -le 0 ]]; then
	echo Input number N must greater or equal to 1.	
else
	for i in $(seq 0 $((N-1)));
	do
		k_Fib[$i]=1
		i=$((i+1))	
	done

	for i in $(seq $N $((N+x)))
	do
		k_Fib[$((i))]=$((sum-k_Fib[$((i-N-1))]+k_Fib[$((i-1))]))
		sum=${k_Fib[$i]}
		j=$((j+1))
	done
fi

# Print the K-Fibinacci series
for i in $(seq 0 $((N+x)))
do
	echo -n ${k_Fib[$i]}', '
	if [[ $i -eq $((N+x)) ]]
	then
		echo '...'
	fi
done



