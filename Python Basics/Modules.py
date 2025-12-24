import math
print(dir(math)) #gets the list of functions in the module
print(math.pow(2,3))
print(math.log(100,10))
print(math.log2(36)) #specific log functions like log 2 and log 10 exist
print(math.pi)
print(math.floor(2.1))
print(math.ceil(2.1))


import calendar
print(dir(calendar))
cal = calendar.month(2025,1)
print(cal)
print(type(cal))
print(calendar.isleap(2024))


#importing a module of our own with user defined functions
#FIle is in same directory
# We can also give alias to any pre defined or custom Module
import Functions #import Functions as f
print(Functions.sum(4,5))
a=[10,20,30,40]
print(Functions.calc_expenses(a))

#if not in the same directory:
import sys
sys.path.append("C:/Users/Lakshya/Desktop/Python Projects/hello")
import Functions as f
Functions.calc_expenses(a)


