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


# Intial FOR -- IN randge() statement

# shortcut with 'for' loop

for n in range(5):
    print(n)
if n == 4:
    print('that\'s all buddy')
else:
    print(n)
"""
'for i in range(7, 10) calls on the numbers 
in range 7-10. 'mysum += i' adds the numbers together
'print(mysum) will print the added numbers.
print(mysum) will print different values if located
within the actual loop itself. it will print the total
values as the loop goes through each sequence
"""
mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)

# adding an if statement in 'for' loop

thisSum = 0
for i in range(0, 100, 15):
    thisSum += i
    print(thisSum)
    if i < 15:
        print(i)
#    elif i == 15:
#        print(str(i, + " the number is ", i)
#    elif i > 15:
#        print("the number is larger than ", i)
    else:
        print("it has finished")


# the 'str()' function converts an 'int' to a string
# so you can print to STDOUT by concatenating the string

yoursum = 0
for i in range(5, 11, 2):
    yoursum += i
    print(str(yoursum) + " i + i while in loop")
print(str(yoursum) + " answer while not in loop")

# BREAK statement
ourSum = 0
for i in range(5, 11, 2):
    ourSum += i
    if ourSum == 5:
        print(str(ourSum) + " this is a BREAK statement!")
    break

# break statement practice
# DO NOT forget your colon after a for statment, an if statment, an elif statement, and an else statement!
ourDifference = 0
for i in range(1, 100):
    ourDifference -= i
    if ourDifference == -75:
        print(str(ourDifference) + " this is an \'if\' statement within a loop!")
    elif ourDifference == 1:
        print(str(ourDifference) + " this was the \'elif\' statement within the \'while loop!\'")
    elif ourDifference == -1:
        print(str(ourDifference) + " this was the 2nd \'elif\' statement within the \'while loop!\'")
    else:
        print("this was the else statement in the \'while\' loop!")
    break

"""
this is a practice WHILE LOOP assigned to a function.

DO NOT FORGET YOUR COLON WHILE ASSIGNING A FUNCTION!!!!!

It appears we can't have a double argument in a function.

The current way the program is written, it will not run..

It returns a syntax error on the double 'int' argument



def i(int, int):
    ourDiff = 0
    for i in range(1, 100):
        ourDifference -= i
        if ourDifference == -75:
            print(str(ourDifference) + " this is an \'if\' statement within a loop!")
        elif ourDifference == 1:
            print(str(ourDifference) + " this was the \'elif\' statement within the \'while loop!\'")
        elif ourDifference == -1:
            print(str(ourDifference) + " this was the 2nd \'elif\' statement within the \'while loop!\'")
        else:
            print("this was the else statement in the \'while\' loop!")
        break
i(int, int)

"""