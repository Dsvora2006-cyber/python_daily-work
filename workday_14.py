# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:08:43 2026

@author: darvo
"""


"""The Retry Limit Problem: A login system should lock a user out after too many failed
attempts, but should also reset the count if they succeed at any point. What information does
your program need to "remember" as it repeats this process?"""

fail_attemp=0
p_enter_limit=3

while fail_attemp<p_enter_limit:
    password=input("Enter your password:-")
    if password=='std123':
        print("Login successfully.")
        fail_attemp=0
        break
    else:
        fail_attemp+=1
        print("Your password is wrong", p_enter_limit-fail_attemp) 
if fail_attemp==p_enter_limit:
    print("Your account is locked.")