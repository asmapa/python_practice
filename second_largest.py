#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:50:20 2024

@author: asma
"""

"""
Create a Python program that finds the second largest number in a list of positive integers(includes zero). The program should prompt the user to input a list of numbers, then compute and print the second largest number in that list.

#Input Format:
#The input consists of a single list of numbers, separated by spaces.
#Hint: Use .split() function to convert input to list.

#Output Format:
#The output consists of the second largest number in the input list.

#Example:

#Input:
#3 1 4 1 5 9 2 6 5 3 5

#Output:
6
"""

var = input("Enter number : ").split()
var = [int(num) for num in var]

largest=var[0]
second_largest=var[0]

for number in var:
    if largest<number :
        largest=number
        
for number in var:
    if number!=largest:
        if second_largest<number:
            second_largest=number
    
        
   
        
print(largest)
print(second_largest)