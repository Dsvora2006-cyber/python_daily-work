# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:30:51 2026

@author: darvo
"""

"""print the multiple lines using a single print ststement as-
            I Like a Python Programming Very Much
            It is My Favorite Subject"""
    
print("I like a python Progamming Very Much \n It is My Favorite Subject")

#Print the part of the above String "Very Much" using the slice operator.
a="I like a python Progamming Very Much. It is My Favorite Subject"
print(a[27:36])


#Print last 5 characters to Above String
a="I like a python Progamming Very Much. It is My Favorite Subject"
print(a[-5:])

#Print all Characters in smaller letter.Also print all the even number position Characters
a="I LIKE A PYHTON PROGAMMING VERY MUCH> IT IS MY FAVORITE SUBJECT"
print(a.lower())
print(a[::2])


#take two string as input and concatnate theme.
s1="Hello How Are Yoy"
s2="I am Python"
print(s1+s2)

#Take an input characters from the user and repeat the string for that many time.
s1=input("Enter the String:-")
n1=int(input("Entre the number:-"))
print(s1*n1)

#Take an input characters from the user and check whether characters 
#is present above given string or not-- Using IN operator and using NOT IN Operator
s1="Hello I am Python"
print('H' in s1)
print('k' in s1)
print("s" not in s1)
print("p" not in s1)


"""Create  a menu drive program for string manipulation
        A. Find the length of a string
        B. print the string in upper case
        C. print the string in lower case
        D .print the string with initial caption
        E. split the string based on the characters enterd"""
        
s1="Hello how are you My self Python"
print("A.find the length of a string")
print("B.print the string in upper case")
print("C.print the string in lower case")
print("D.print the string with initial caption")
print("E.split the string based on the characters entered")
 
choice=input("\n Enter Your choice (A-E):")
if choice=='A':
    print("Length of a stirng:",len(s1))
elif choice=='B':
    print("Upper case characters:",s1.upper())
elif choice=='C':
    
    
    print("Lower case characters:",s1.lower())
elif choice=='D':
    print("initial caption is",s1.title())
elif choice=='E':
    char=input("Enter the characters to split by:-")
    print("Split result:-",s1.split(char))
else:
    print("Invalide choice.")
   
    
   
    
#Take two string input s1 and s2 and check whether s2 is present in s1 or not.
s1="Hello I am python"
s2="python"
print(s1.find(s2))

#is s2 is part of s1 then print the first and last accurences of it.
s1="Hello I am python"
s2="o"
print("Fist accurences is:-",s1.index(s2))
print("Last accurences is:-",s1.rindex(s2))

#if s2 is present in s1 then also count number of times in s1
s1="Hello I am python"
s2="o"
print(s1.count(s2))

#Count the total no of words in string input by user
s1=input("Enter the string-")
ans=len(s1.split())
print("Total no of word is in string:-",ans)

#Take a input and print all the element in reverce order using range
s1=input("Enter the string")
for i in range(len(s1) -1,-1,-1):
    print(s1[i],end="")
print()


n=int(input("Enter the nu you want to enter:-"))
even_count=0
odd_count=0
for i in range(n):
    num=int(input(f"Enter the num{i+1}"))
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Odd no:-",odd_count)
print("even no:-",even_count)
