#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:51:16 2024

@author: asma
"""

"""

Create a Python program that takes a list of integers, reverses the list, adds the values at odd indices from both the original and reversed lists, and creates a new list with the result. The new list should be printed in the end.

Input Format:
The input consists of a single list of integers, separated by spaces.

Output Format:
The output consists of the new list of values, separated by spaces, obtained by adding values at odd indices from both the original and reversed lists.


Example:
Input:
1 2 3 4 5

Output:
1 6 3 6 5
"""

original = input("Enter the numbers :").split()
original=[int(num) for num in original]
rev=original[::-1]
result=[]

for i in range(len(original)):
    if i%2==0:
        result.append(original[i])
    else :
        result.append(original[i] + rev[i])
        
        
print(" ".join(map(str, result)))
        
        
print(result)