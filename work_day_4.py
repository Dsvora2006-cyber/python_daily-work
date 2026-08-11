# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:58:32 2026

@author: darvo
"""

#write a python program to create a pattern using range
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()