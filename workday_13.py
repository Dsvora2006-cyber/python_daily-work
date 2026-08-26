# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:08:43 2026

@author: darvo
"""

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
        print("Your passwod is wrong.",p_enter_limit-fail_attemp) 
if fail_attemp==p_enter_limit:
    print("Your account is locked it.")