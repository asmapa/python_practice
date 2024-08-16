#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:50:47 2024

@author: asma
"""


"""

Create a Python program that removes all duplicate positive integer numbers(includes zero) from a list and prints the unique numbers in the order they first appeared.
The program should prompt the user to input a list of numbers, then process the list to remove duplicates and print the resulting list of unique numbers.

Input Format:
The input consists of a single list of numbers, separated by spaces.

Output Format:
The output consists of the unique numbers, separated by spaces, from the input list, in the order they first appeared.

Example:
Input:
3 1 4 1 5 9 2 6 5 3 5
Output:
3 1 4 5 9 2 6

"""

var = input("Enter numbers:").split()
var=[int(num) for num in var]

org=[]

for num in var:
    nu=0
    for n in org:
        if num == n:
            nu=n
            break
        
    if num != nu:
        org.append(num)
            
   
    
print(org)

"""

Actually the below is the better way

for num in var:
    if num not in org:
        org.append(num)
"""
            