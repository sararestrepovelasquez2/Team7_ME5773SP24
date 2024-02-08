#!/bin/bash
#
#====================================================================
# ITEM 3
#
#
# Authors: Dai Nam Nguyen and Sara Restrepo Velasquez
#
# Last modification date: 02/08/2024
# Version: 1.0
#====================================================================
#
# Ask the user to input a number
N=$1

echo All factorials from 1 to $N:

fact=1

# Find and print all factorials from 1 to N
if [[ $N -le 0 ]]; then
	echo Input number N must greater or equal to 1.	
else
	for i in $(seq 1 $N)
	do
		fact=$((fact*i))
		echo $i! = $fact	
	done
fi


