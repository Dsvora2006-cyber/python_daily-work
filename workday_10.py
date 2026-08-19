# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:12:13 2026

@author: darvo
"""

"""The Delivery App Charge: A food delivery app charges differently based on distance,
 whether it's raining, and whether the order value crosses a certain amount 
 (which might waive the delivery fee entirely). How would you decide the order 
 in which to check these conditions?"""

normal_del=int(input("Input the normal delivery charges:-"))
km=int(input("Enter the kelimeter:-"))
km_charge=int(input("Enter the kelimeter charges:-"))
customer_cost=int(input("Enter the customer cost:-"))
is_rain=input("The rain is heavily(yes/no):-")
rain_charge=int(input("Enter the rain charges:-"))

charges=0
if customer_cost>=500 and  km<=5:
    charges=0
else:
    charges=normal_del+(km*km_charge)+customer_cost
if is_rain=="yes":
    charges=normal_del+(km*km_charge)+rain_charge+customer_cost
print("Total amount of delivery charges is:-",charges)

