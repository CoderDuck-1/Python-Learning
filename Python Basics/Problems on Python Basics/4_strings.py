#1) Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
#2) Create a variable to store the string "Earth revolves around the sun"
#3) Print "revolves" using slice operator
#4) Print "sun" using negative index
#5) Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat every day. Use python f string for this.
#6) I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line

#Ans1
street="Raj Nagar Extension"
city="ghaziabad"
state="Uttar Pradesh"
country="India"
print(street+"\n"+city+"\n"+state+"\n"+country)
print(f"{street}\n{city}\n{state}\n{country}") #Format String

#Ans2
a="Earth revolves around the sun"

#Ans3
print(a[6:14])

#Ans4
print(a[-3:])

#Ans5
fruits=4
vegetables=8
print(f"I eat {fruits} fruits and {vegetables} vegetables in a day")

#Ans6
s="maine 200 banana khaye"

s=s.replace("banana","samosa")
s=s.replace("200", "10")
print("Using 2 replace:",s)

s.replace("banana","samosa").replace("200", "10")
print("Using 1 replace:",s)

