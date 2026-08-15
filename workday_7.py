# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:24:55 2026

@author: darvo
"""

#write a program to check number is armstrong or not

n=int(input("Enter the number:-"))
temp=n
length=len(str(n))
rev=0
while n>0:
        digit=n%10
        rev=rev+(digit**length)
        n=n//10
if rev==temp:
    print("No is armstrong")
else:
    print("no is not armstrong")