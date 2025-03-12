#!/bin/bash

if [ -z "$1" ]; then
  echo "Error: missing first parameter."
  exit 1
fi
if [ -z "$2" ]; then
  echo "Error: missing second parameter."
  exit 1
fi

number1=$1
number2=$2

echo "Enter the choice of operation:"
echo "1. Addition"
echo "2. Subtraction"
echo "3. Division"
echo "4. Multiplication"
echo "5. Modulus"

read choice

case $choice in
   1 )
   echo "Result is: $((number1 + number2))"
   ;;
   2 )
   echo "Result is: $((number1 - number2))"
   ;;
   3 )
   if [ "$number2" -eq 0 ]; then
      echo "Error! Division by zero is not allowed."
   else
      echo "Result is: $((number1 / number2))"
   fi
   ;;
   4 )
   echo "Result is: $((number1 * number2))"
   ;;
   5 )
   if [ "$number2" -eq 0 ]; then
      echo "Error! Modulus by zero is not allowed."
   else
      echo "Result is: $((number1 % number2))"
   fi
   ;;
   * )
   echo "Invalid choice of operation"
   ;;
esac
