#1) Using following list of cities per country,
#india = ["mumbai", "banglore", "chennai", "delhi"]
#pakistan = ["lahore","karachi","islamabad"]
#bangladesh = ["dhaka", "khulna", "rangpur"]
#Write a program that asks user to enter a city name and it should tell which country the city belongs to
#Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

#Ans1
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

#1
x=input("Enter City name:")
if x in india:
    print(f"{x} is in India")
if x in pakistan:
    print(f"{x} is in Pakistan")
if x in bangladesh:
    print(f"{x} is in Bangladesh")

#2
city1=input("Enter 1st City name:")
city2=input("Enter 2nd City name:")
if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in Pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in Bangladesh")
else:
    print("Both cities are in different countries")


#2) Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#Ask user to enter his fasting sugar level
#If it is below 80 to 100 range then print that sugar is low
#If it is above 100 then print that it is high otherwise print that it is normal

#Ans2
#1
sugar=input("Enter your fasting sugar level: ")
sugar=int(sugar)

#2
if sugar < 80:
    print("Your sugar level is low")
elif sugar < 100:
    print("Your sugar level is normal")
else:
    print("Your sugar level is high")



