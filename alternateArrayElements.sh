#!/bin/bash

echo "Enter the number of elements:"
read n  # Read the number of elements from user

declare -a inputArray

echo "Enter $n elements:"
for ((i = 0; i < n; i++)); do
    read inputArray[i] 
done

echo "Alternate elements of the input array are:"
for ((i = 0; i < n; i += 2)); do
    echo "${inputArray[i]}"  
done
