#!/bin/bash

echo "Enter the first number:"
read  number1

echo "Enter the second number:"
read  number1

echo "Enter the choice of operation:"
echo "1. for addition"
echo "2. for substraction"
echo "3. for division"
echo "4. for multiplication"
echo "5. for modulus"

read choice

case choice in
   1 )
   echo "Result is: $number1 + $number2"
   ;;
   2 )
   echo "Result is: $number1 - $number2"
   ;;
   3 )
   echo "Result is: $number1 / $number2"
   ;;
   4 )
   echo "Result is: $number1 * $number2"
   ;;
   5 )
   echo "Result is: $number1 % $number2"
   ;;
 *)
   echo "Invalid choice of operation"
   ;;
esac
