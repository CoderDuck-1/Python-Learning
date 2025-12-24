book={} #empty dictionary

book["bob"]= { #dictionary with dictionary as value corresponding to keys
    "Name" : "bob",
    "phone" : 9711712343,
    "age" : 16
}

book["Jack"]= {
    "Name" : "Jack",
    "phone" : 9711712444,
    "age" : 17
}

print(book)

print(type(book)) #dict

import json
s=json.dumps(book, indent=4) #dump into string (json)
print(s)

print(type(s)) #str

with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/book.txt", "w") as f:
    f.write(s)  #with keyword closes the file after a certain set of operations
# Book.txt got saved in the location specified

#reading the file in another project
with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/book.txt", "r") as f2:
    s2  = f2.read()
    print(s2)

book2=json.loads(s2)
print(book2)
print(type(book2))  #dict

print(book2['bob'])
print(book2['bob']['age' ])

print('\n')

for person in book:
    print(book[person]["age"])


