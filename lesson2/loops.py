#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 11:17:39 2017

@author: jcart
"""



n = 0
while n < 5:
    print(n)
    n += 1 # the '+=' is a shortcut operator to add to the variable



o = 0
while o < 20:
    print(o)
    o += 1  # the '+=' is a shortcut operator to add to the variable
    
    
"""
# this is an infinite loop if you always type 'right'
# it will have nothing to evaluate to false.
n = input("You are lost in a forest! Will you go left or right? --> ")
while n == 'right':
    n = input("You are lost in a forest! Will you go left or right? --> ")
    print('You got out of the forest!')
"""



# shortcut with 'for' loop
for n in range(5):
    print(n)
if n == 4:
    print('that\'s all buddy')
else:
    print(n)