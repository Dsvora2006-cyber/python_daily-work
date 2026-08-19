# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 05:58:30 2026

@author: darvo
"""

"""The Class Attendance Puzzle: 
 A teacher wants to know not just how many students are present, 
 but whether the class qualifies for a "good attendance" reward, 
 which depends on a minimum percentage being met. 
 What do you need to calculate first, and what decision comes after? """
 

present = int(input("Enter number of students present: "))
total = int(input("Enter total number of students: "))
minimum = float(input("Enter minimum attendance percentage required: "))


attendance_percentage = (present / total) * 100

print(f"Attendance Percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= minimum:
    print("Good Attendance! Eligible for the reward.")
else:
    print("Not eligible for the reward.")