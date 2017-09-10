#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 12:25:10 2017

@author: jcart
"""

if x%2 == 0:
    if x%3 == 0:
        print('')
        print('Divisible by 2 and 3')
    else:
        print('')
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')