# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 07:20:49 2026

@author: darvo
"""

kid_price=int(input("Enter the kid price:-"))
adult_price=int(input("Enter the adult_price:-"))
siniar_ct=int(input("Enter the sinia_ct prize:-"))
weekend=int(input("Enter the weekend price:-"))
is_weekend=input("Weekend is here (yes/no):-")
age=int(input("Enter the human age:-"))

price=0
if age<=12:
    print("You are kid")
    price=kid_price              
elif age>=12 and age<=60:
    print("You are adult")
    price=adult_price
else:
    print("You are siniar citizen.")
    price=siniar_ct
    
if is_weekend=='yes':
    price+=weekend
print("The total price is:-",price)