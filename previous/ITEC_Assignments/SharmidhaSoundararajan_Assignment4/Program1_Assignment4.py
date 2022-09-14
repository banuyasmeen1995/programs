# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 11:37:57 2021

@author: sharm
"""

systolic_bp = eval(input("Enter Systolic blood pressure: "))
diastolic_bp = eval(input("Enter Diastolic blood pressure: "))
if systolic_bp < 120 and diastolic_bp < 80:
    print("Blood pressure category is Normal")
elif systolic_bp >= 120 and diastolic_bp <=129 and diastolic_bp < 80:
    print("Blood pressure category is Elevated")
elif (systolic_bp >= 130 and diastolic_bp <=139) or (diastolic_bp >= 80 and diastolic_bp <=89):
    print("Blood pressure category is Hypertension stage 1")
elif (systolic_bp >= 140 and diastolic_bp <= 180) or (diastolic_bp >= 90 and diastolic_bp <=120):
    print("Blood pressure category is Hypertension stage 2")
elif (systolic_bp > 180) or (diastolic_bp > 120):
    print("Blood pressure category is Hypertension crisis")
else:
    print("Enter valid details")