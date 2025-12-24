exp= [ 2100, 2000, 2340, 4560, 1000]
total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]
print(total)

total2= 0
for item in exp:
    total2= total2+item
print(total2)

total3=0

for i in range(len(exp)): #range(start=0, stop, step) #start is included, end is not included
    print("For month ",i+1, " the expense is: ", exp[i])
    total3+=exp[i]
print("Total expense is: ",total3)

for i in range(1, 11):
    print(i)
print(list(range(5)))

for c in "Hello":
    print(c)