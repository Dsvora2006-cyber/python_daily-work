# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:28:46 2026

@author: darvo
"""



"""The Library Fine Problem: A library charges a fine for overdue books,
 but the rule changes depending on how many days late a book is — 
 the fine per day increases the longer the delay. Design a way to calculate 
 the total fine for any number of overdue days."""
 
fix_day=int(input("Enter the free day:-"))
return_day=int(input("Enter the return day:-"))

od=return_day-fix_day
fine=0

if od<=2:
    fine=od*10
elif od<=4:
    fine=(2*10)+((od-2)*20)
elif od<=6:
    fine=(2*10)+(2*20)+((od-4)*30)
elif od<=8:
    fine=(2*10)+(2*20)+(2*30)+((od-6)*40)
else:
    fine=(2*10)+(2*20)+(2*30)+(2*40)+((od-8)*50)
print("Total overdue days:-",od)
print("Total fine is:-",fine)


