# Classes and Objects are part of Object Oriented Programming

class human: #class name

    def __init__(self, n, o): #initialising object properties; n and o are function arguments
        self.name = n
        self.occupation = o

    def work(self):         # defining methods (functions that operate on class objects)
        if self.occupation == "tennis player":
            return(self.name+" plays tennis")
        elif self.occupation == "actor":
            return(self.name+ " is an actor")

    def hello(self):
        return("Hey, I'm " + self.name +". I'm fine and how are you?")

#Assigning objects in class

Tom=human("Tom Cruise", "actor")
print(Tom.hello())
print(Tom.work())

Maria=human("Maria Sharapova", "tennis player")
print(Maria.hello())
print(Maria.work())


