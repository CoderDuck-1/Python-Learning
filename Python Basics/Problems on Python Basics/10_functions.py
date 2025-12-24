#1) Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
#area = (1/2)*base*height
from email.policy import default


#2) Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
#rectangle area=length*width
#If no shape is supplied then it should take triangle as a default shape

#3) Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
#*
#**
#***
#if input is 4 then it should print
#*
#**
#***
#****
#Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)


#Ans 1
def calculate_area(base, height):
    area=base*height/2
    return area

print(calculate_area(5,2))

#Ans2
def calculate_area2(base, height, shape="triangle",):
    if shape == "triangle":
        area=base*height/2
        return area

    elif shape == "rectangle":
        return base*height

print(calculate_area2(5,2, "rectangle"))

#Ans3
def print_pattern(n):
    for i in range(1,n+1):
        print("*"*i)
print_pattern(5)
