

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created on Mon Sep 18 11:17:39 2017

# @author: jcart




# n = 0
# while n < 5:
#    print(n)
#    n += 1 # the '+=' is a shortcut operator to add to the variable



# o = 0
# while o < 20:
#    print(o)
#    o += 1  # the '+=' is a shortcut operator to add to the variable
    
    
# this is an infinite loop if you always type 'right'
# it will have nothing to evaluate to false.
# n = input("You are lost in a forest! Will you go left or right? --> ")
# while n == 'right':
#    n = input("You are lost in a forest! Will you go left or right? --> ")
#    print('You got out of the forest!')



# Intial FOR -- IN randge() statement

# shortcut with 'for' loop

# for n in range(5):
#   print(n)
#    if n == 4:
#        print('that\'s all buddy')
#    else:
#        print(n)

# 'for i in range(7, 10) calls on the numbers 
#in range 7-10. 'mysum += i' adds the numbers together
# 'print(mysum) will print the added numbers.
# print(mysum) will print different values if located
# within the actual loop itself. it will print the total
# values as the loop goes through each sequence

# mysum = 0
# for i in range(7, 10):
#     mysum += i
# print(mysum)

# adding an if statement in 'for' loop

# thisSum = 0
# for i in range(0, 100, 15):
#     thisSum += i
#     print(thisSum)
#     if i < 15:
#         print(i)
#    elif i == 15:
#        print(str(i, + " the number is ", i)
#    elif i > 15:
#        print("the number is larger than ", i)
#    else:
#        print("it has finished")


# the 'str()' function converts an 'int' to a string
# so you can print to STDOUT by concatenating the string

# yoursum = 0
# for i in range(5, 11, 2):
#     yoursum += i
#     print(str(yoursum) + " i + i while in loop")
# print(str(yoursum) + " answer while not in loop")

# BREAK statement
# ourSum = 0
# for i in range(5, 11, 2):
#     ourSum += i
#     if ourSum == 5:
#         print(str(ourSum) + " this is a BREAK statement!")
#     break

# break statement practice
# DO NOT forget your colon after a for statment, an if statment, an elif statement, and an else statement!
# ourDifference = 0
# for i in range(1, 100):
#     ourDifference -= i
#     if ourDifference == -75:
#         print(str(ourDifference) + " this is an \'if\' statement within a loop!")
#     elif ourDifference == 1:
#         print(str(ourDifference) + " this was the \'elif\' statement within the \'while loop!\'")
#     elif ourDifference == -1:
#         print(str(ourDifference) + " this was the 2nd \'elif\' statement within the \'while loop!\'")
#     else:
#         print("this was the else statement in the \'while\' loop!")
#     break


# this is a practice WHILE LOOP assigned to a function.

# DO NOT FORGET YOUR COLON WHILE ASSIGNING A FUNCTION!!!!!

# It appears we can't have a double argument in a function.

# The current way the program is written, it will not run..

# It returns a syntax error on the double 'int' argument

## WHY WOULD YOU NEED TWO ARGUMENTS?????!!!??

## YOU DON'T NEED ANY ARGUMENTS aka ZERO ARGUMENTS . . . watch. 


"""
def i():
#    a=int(input())
#    b=int(input())
    a = 1
    b = 100
    ourDiff = 0
    for i in range(a, b):
        ourDiff -= i
        if ourDiff == -75:
            print(str(ourDiff) + " this is an \'if\' statement within the \'while loop!\'")
        elif ourDiff == -2:
            print(str(ourDiff) + " this was the 1st \'elif\' statement within the \'while loop!\'")
        elif ourDiff == -1:
            print(str(ourDiff) + " this was the 2nd \'elif\' statement within the \'while loop!\'")
        else:
            print("this was the else statement in the \'while\' loop!")
        break
i()


def j():
    mysum = 0
    for i in range(5, 11):
        mysum += i
        if mysum == 5:
            print(str(mysum) + " this is a BREAK statement in j() -- !")
        break
j()
"""
# This started out as an experiement to incorporate conditional statements within conditional statements.
# It ended up working pretty beautifully!!

def k():
    myproduct = 1
    for i in range(7, 21, 2):
        myproduct *=  i
        if myproduct == 63 or myproduct == 693:
            if myproduct == 63:
                print(str(myproduct) + "       * This is the second \'if\' statement in k() -- !")
            else:
                print(str(myproduct) + "      * This is the third  \'if\' statement in k() -- !")
        elif myproduct == 7 or myproduct == 135135:
            if myproduct == 7:
                print(str(myproduct) + "        * This is the first \'elif\' statement in k() -- !")
            else:
                print(str(myproduct) + "   * This is the fifth \'elif\' statement in k() -- !")
        elif myproduct == 9009 or myproduct == 2297295:
            if myproduct == 9009:
                print(str(myproduct) + "     * This is the fourth \'elif\' statement in k() -- !")
            else:
                print(str(myproduct) + "  * This is the sixth \'elif\' statement in k() -- !")
        else:
            break
k()

# \
# \
# \
# we are trying to represent a function call to divide all numbers in this range or that range.
# this is a test and is for fun purposes only

def l():
    myQuotient = 0.1
    for i in range(1, 31, 3):
        myQuotient /= i
        print(str(myQuotient) + " this is the first \'myQuotient\'!")
        print(str(i) + " this is the letter \'i\'!")
        print(str(myQuotient) + " this is the second \'myQuotient\'!")
    print(str(myQuotient) + " this is the \'out of loop\' \'myQuotient\'!") 
l()

# \
# \
# \
# This is going to incorporate all 4 basic arthimetic versions.  Sums, Differences, Products and Quotient.

def m():
    mySum = 0
    myProduct = 1
    myDifference = 0
    myQuotient = -0.1
    print "%s, %s, %s, %s," % (mySum, myProduct, myDifference, myQuotient,)
    for i in range(1, 20, 2):
        mySum += i
        myProduct *= i
        myDifference -= i
        myQuotient /= i
