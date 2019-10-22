# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 11:58:29 2019

@author: grego
"""





def tax(income):
    if income <= 9525:
        return income * 0.10
    elif income <= 38700:
        return income * 0.12
    elif income <=82500:
        return income * 0.22
    elif income <= 157500:
        return income * 0.24
    elif income <= 200000:
        return income* 0.32
    elif income <= 500000:
        return income * 0.35
    else:
        return income * 0.37
    
income = float(input("Please enter income: "))
print(tax(income))