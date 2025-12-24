#Exercise: Python Variables
#Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see.

#Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables

#Store your first, middle and last name in three different variables and then print your full name using these variables

#Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue
#Ans4 = 1record, record-one, record^one, continue

#Ans1
#try:
#   break=5
#except Exception as e:
#    print(type(e).__name__,)
# break is a reserved keyword in Python. and we cannot get the exception type because its a syntax error, which occurs before the program even runs.


#Ans2
by=input("Enter birth year: ")
cy=input("Enter current year: ")
Age= int(cy) - int(by)
print(Age)


#Ans 3
first_name = 'Lakshya'
last_name = 'Upreti'
print("full name is : ", first_name, last_name) #Comma automatically separates the values by spaces.