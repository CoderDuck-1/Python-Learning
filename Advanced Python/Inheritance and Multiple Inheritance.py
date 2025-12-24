# Benefits:-
# 1- Code Reusability
# 2- Extensibility
# 3- Readability

# if both parent and child class have a method, the child class method will be used. To explicitly call the parent method we can use "super() function"
# eg super().show()
class Vehicle():
    def generic_usage(self):
        print("Generic Usage: Transportation")

class Car(Vehicle):
    def __init__(self):
        print("Im a Car")
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self):
        print("Specific Usage: Family Travel, Commute to work, etc.")

class Bike(Vehicle):
    def __init__(self):
        print("Im a bike")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self):
        print("Specific Usage: Road Trips, Racing")

class Father():
    def gardening(self):
        print('I like gardening')

class Mother():
    def cooking(self)
        print('I like cooking')

class child(Father, Mother):
    def playing(self):
        print('I like playing games.')



if __name__ == '__main__':
    c = Car()
    c.generic_usage()
    c.specific_usage()

    b= Bike()
    b.generic_usage()
    b.specific_usage()

    print(isinstance(c, Car))
    print(issubclass(Car, Vehicle))


