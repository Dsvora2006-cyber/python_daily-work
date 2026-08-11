# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:48:32 2026

@author: darvo
"""

num=121
reverce=0
original_num=num

while num>0:
    digit=num%10
    reverce=(reverce*10)+digit
    num=num//10
if reverce==original_num:
    print("Number is palimdrom")
else:
    print("Number is not palimdrom")
