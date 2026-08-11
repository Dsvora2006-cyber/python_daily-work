# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:48:32 2026

@author: darvo
"""

print("CALCULATOR")
print("1.Addition")
print("2.substration")
print("3.Multiplication")
print("4.Devision")

choice=input("Enter the choice 1/2/3/4")
n1=eval(input("Entre the value of n1:-"))
n2=eval(input("Enter the value of n2:-"))

if choice=='1':
    print("Result=", n1+n2)
elif choice=='2':
    print("result=",n1-n2)
elif choice=='3':
    print("result=",n1*n2)
elif choice=='4':
    print("result=",n1/n2)
else:
    print("Invalide option")
    
