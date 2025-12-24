#1) You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
#2) You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
#3) You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
#4) Print binary representation of number 17

#Ans1)
length=92
breadth=48.8
area=length*breadth
area = round(area,2)
print("Area of the football field is:", area, "m^2")

#Ans2)
n=9
c=1.49
p=20
b=p-c*n
print("Shopkeeper will give back", b, "rs")

#Ans3
area_b=5.5**2
cost_t=500
cost_Total= area_b*cost_t
print("Total cost:", cost_Total)

#Ans4
num=17
print(format(num, 'b'))

