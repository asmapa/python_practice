#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 22:00:36 2024

@author: asma
"""

import random
import datetime


i=0
while(i<50):
    year=random.randint(2000,2024)
    if(year % 4==0 or year %100 != 0 and year % 400 == 0):
        leap=1
    else :
        leap=0
        
    month=random.randint(1,12)
    
    if(month == 2 and leap== 1):
        day=random.randint(1,29)
    elif(month == 2 and leap == 0):
        day=random.randint(1,28)
    elif(month==7 or month==8):
        day=random.randint(1,31)
    elif(month%2!=0 and month < 7):
        day=random.randint(1,31)
    elif(month %2==0 and month>7 and month<12):
        day=random.randint(1,31)
    else:
        day=random.randint(1,30)
    
        
    dd=datetime.date(year,month,day)
    day_of_year=dd.timetuple().tm_yday
    print(day_of_year)
    i=i+1;
    