# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:16:36 2019

@author: grego
"""
x = "redro esrever ni ecneuqes a"

def reverse_a_string(x):
    inc = len(x) - 1
    while inc >= 0:
        print(x[inc], end='')
        inc = inc - 1
        
reverse_a_string(x)
