#1) We have following information on countries and their population (population is in crores),
#Country	Population
#China	143
#India	136
#USA	32
#Pakistan	21

#i Using above create a dictionary of countries and its population

#ii Write a program that asks user for three type of inputs,
#print: if user enter print then it should print all countries with their population in this format,
#china==>143
#india==>136
#usa==>32
#pakistan==>21
#add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
#remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
#query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.

#Ans1
print(dir(dict))
#i
country_pop={"China":143, "India":136, "USA":32, "Pakistan":21}
#ii
choice=input("Enter your command (print/add/remove/query): ")
if choice=="print":
    for k,v in country_pop.items():
        print(str(k)+"==>"+str(v))

elif choice=="add":
    c_add=input("Enter country name to be added: ")
    if c_add in country_pop:
        print("Country is already in list")
    else:
        p_add=input(f"Enter population of {c_add}: ")
    country_pop[c_add]=p_add
    for k,v in country_pop.items():
        print(str(k)+"==>"+str(v))

elif choice =="remove":
    c_remove=input("Enter country name to be removed: ")
    if c_remove not in country_pop:
        print("Country is not in list")
    else:
        del country_pop[c_remove]
        for k,v in country_pop.items():
            print(str(k)+"==>"+str(v))

elif  choice=="query":
    query=input("Enter name of country to be checked: ")
    if query not in country_pop:
        print("Country is not in list")
    else:
        print(f"The population of {query} is {country_pop[query]} crores")

#2) You are given following list of stocks and their prices in last 3 days,
#Stock	Prices
#info	[600,630,620]
#ril	[1430,1490,1567]
#mtl	[234,180,160]
#Write a program that asks user for operation. Value of operations could be,
#print: When user enters print it should print following,
#info ==> [600, 630, 620] ==> avg:  616.67
#ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#mtl ==> [234, 180, 160] ==> avg:  191.33
#add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

#Ans2

info =	[600,630,620]
ril	= [1430,1490,1567]
mtl =	[234,180,160]

stocks={"info":info,"ril":ril,"mtl":mtl}

def avg(list):
    return sum(list)/len(list)

choice2=input("Enter the operation(print/add): ")
if choice2 == "print":
    for  k,v in stocks.items():
        print(k,"==>",v,"==> avg:",round(avg(v),2))
elif choice2 == "add":
    s_name=input("Enter the stock name: ")
    s_price=float(input("Enter the stock price: "))
    if s_name in stocks:
        stocks[s_name].append(s_price)
    else:
        stocks[s_name] = [s_price]
    for  k,v in stocks.items():
        print(k,"==>",v,"==> avg:",round(avg(v),2))

#3) Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them

import math

def pi(): #or simply use math.pi
    return 22/7

def circle_calc(radius):
    area=round(pi()*radius**2,2)
    circumference=round(2*pi()*radius,2)
    diameter= round(2*radius,2)
    return area,circumference,diameter

if __name__=="__main__":
    r=input("Enter radius: ")
    r=float(r)
    x=circle_calc(r)
    print(type(x).__name__, x)

#OR
    area, circumference, diameter = circle_calc(r)
    print(f"Area:{area}, Circumference:{circumference}, Diameter:{diameter}")







