'''print(1/0) #ZeroDivisionError

print("abc"+2) #TypeError'''

x=input("Enter a number1: ")
y=input("Enter a number2: ")
#execution stops at error

#exception handling start
try:
    z=int(x)/int(y) #Block of code in which exception occur is placed in between try and except

#  except Exception as e: #generic way of handling exception, (used to know type of exception occured)
#  except ZeroDivisionError as e:  #This can also be used to handle different types of errors specifically
#  print(type(e).__name__,"exception has occured")
#  z=None

except ZeroDivisionError as e:
    print(type(e).__name__)
    z=None
except TypeError as e:
    print(type(e).__name__)

print("Division is ", z)

# No crash now even when error occured.