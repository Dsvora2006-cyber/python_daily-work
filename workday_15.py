# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:42:49 2026

@author: darvo
"""

#print the list
l1=['student1','student2','student3','student4']
print(l1)

#count total number of students from the list
l1=['a','b','c','d']
print(len(l1))

#add one more studetn in the list
l1=['a','b','c','d']
l1.append('e')
print(l1)

#display all student in shorted order
l1=['raj','karan','ajay','krunal']
l1.sort()
print(l1)

#check a particular student`s name is present in the list or not
l1=['ram','krishna','hanuman']
'ram' in l1

#if the student`s name is presetn`s in the list l1. 
#print total no of same name student in l1 and 
#diaplay the position of 1st student

l1=['ram','krishna','hanuman','ram','ram','ram']
'ram' in l1

l=[x for x in l1 if l1.count(x)>1]
print(l)
    
print(l1.index('ram'))

#remove the last number from the list1
l1=['ram','krishna','hanuman']
l1.pop()
print(l1)

"""remove the student from the list(take a name of student from the user)"""
l1=['ram','krishna','hanuman']
name=input("enter the removing name")
l1.remove(name)
print(l1)

"""while removing the particular from the list of multiple
students have same name then remove all of them from the list"""

l1=['ram','krishna','hanuman','ram','ram','ram']
l=[x for x in l1 if x!='ram']
print(l)


"""create a list of 10 numbers and findout the maximum and minmum number"""
l1=[1,2,3,4,5,6,7,8,9,10]
print(max(l1))
print(min(l1)) 

"""create a list of alphabets and count total number of volwe in it."""
l1=['a','b','c','d','e','i']
count=sum(1 for x in l1 if x in "aeiouAEIOU")
print("Total Wolve no is:-",count)


"""create a list of even number between 1 to 21 using range()"""
even=list(range(2,21,2))
print(even)

"""create a list of 10 numbers and find the total of odd numbers and even number"""
l1=[1,2,4,5,6,7,8,9,10]
odd=len([x for x in l1 if x%2==1])
even=len([x for x in l1 if x%2==0]) 
print(odd)
print(even)

"""create a list of 10 numbers and put the all the odd numbers in 1 list 
and even number in another list"""
l1=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
even=[x for x in l1 if x%2==1]
odd=[x for x in l1 if x%2==0]
print(odd)
print(even)


"""write a program create a list of words. print all the palimdrom words for it"""
l1=['aaa','mam','nayan','darshan','kunj']
palim=[x for x in l1 if x==x[::-1]]
print(palim)




