#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 19:02:12 2024

@author: wrasmussen
"""

user_dict = {}

#with open("users.txt", "r") as f:
#    for line in f:
#        (key, val) = line.split(maxsplit=1)
#        user_dict[(key)] # = val
        
#print(user_dict)

avail_bal = {'balance': 1000}

#print(avail_bal)

with open("users.txt", "r") as f:
    for line in f:
        (key, val) = line.split(maxsplit=1)
        user_dict[(key)]  = avail_bal

for key, value in user_dict.items():
    print("\nUser ID:", key)
    
    for key in value:
        print(key + ':', value[key])