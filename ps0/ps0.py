# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:20:20 2020

@author: Sharon G
"""

# Problem Set 0 
# Write a program that does the following in order:  
# 1. Asks the user to enter a number “x” 
# 2. Asks the user to enter a number “y”  
# 3. Prints out number “x”, raised to the power “y”. 
# 4. Prints out the log (base 2) of “x”.   

# Please note that the assignment requests the use of numpy or pylab.
# For this reason, multiple methods have been included for executing 
# the requested commands. 

x = int(input("Hello User, and Welcome to PS_0\nPlease enter a value for variable x:"))
y = int(input("Next, please enter a value for variable y:"))
import math
print("Importing math:")
print("The value of x, raised to the power of y, is", x**y, ".")
print("The log (base 2) of x is", math.log(x, 2), ".")
import numpy
print("Importing numpy:")
print("The log (base 2) of x, is", numpy.log2(x), ".")
import pylab
print("Importing pylab:")
print("The log (base 2) of x, is", pylab.log2(x), ".")