# List comprehension provides a way to transform one list into another.
numbers=[1,2,3,4,5,6,7,8,9]
even = [i for i in numbers if i%2==0]
for i in even:
    print(i)
sqr_nos=[i*i for i in numbers]
print(sqr_nos)

# works the same way for sets, but with {} instead of []

# zip function takes multiple iterables and combines corresponding elements into an iterator of tuples.

cities=["mumbai", "new york", "paris"]
countries=["india", "usa", "france"]
z=zip(cities,countries)
print(z)
dicct={countries:cities for cities,countries in z}
print(dicct)
