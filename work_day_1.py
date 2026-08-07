# -*- coding: utf-8 -*-

""" write a program to input salary (basic,da,hra,pf) if basic is < 10000 then da=25%,
 hra=5% if basic >=-10000 and basic<=30000 then dat=35% hra=10% if basic >30000  
 then da=40% hra=20% pf is same of all 12%"""
 
basic=eval(input("Enter the basic salary:-"))
if basic<10000:
    da=25*10000/100
    hra=5*10000/100
    
elif basic>=10000 and basic<=30000:
    dat=35*10000/100
    hra=10*10000/100
    
elif basic>30000:
    da=40*10000/100
    hra=20*1000/100
pf=12*10000/100
salary=basic+da+hra-pf
print("da salary:-",da)
print("hra salary:-",hra)
print("main slary:-",salary)




 