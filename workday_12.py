# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 06:23:29 2026

@author: darvo
"""


"""The Exam Eligibility Checker: A university allows a student to sit for a final exam only if they
meet attendance requirements AND have passed all assignments AND have no pending fees.
Think about what happens if a student fails just one of these — how should the message to the
student differ for each failure reason?"""

attendance=float(input("Enter the precentage of attendance:-"))
assignments_passed=input("All over assignment paseed (yes/no):-")
pending_fee=float(input("Enter the pending fees:-"))

min_attendance=75.50
if attendance<min_attendance:
    print("Not eligible for exam because student attendance is:-",attendance)
elif assignments_passed!='yes':
    print("Not eligible for pending assignment.")
elif pending_fee>0:
    print("Not eligible for you fees is pending:-",pending_fee)
else:
    print("Eligible for final exam.")