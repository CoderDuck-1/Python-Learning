# Set is an unordered collection of unique elements.\
# Set elements cant be accesses using indexes.
a=set() # cant initialise using empty curly braces as its dict
a.add(1)
a.add(2) # or a={1.2}
print(a)

#usage of set for getting unique elements.
numbers =[1,2,4,5,6,3,4,5,2,]
unique_numbers = set(numbers)
unique_numbers2=frozenset(numbers)
#frozen set is type of set whose contents cant be changed.
#we can take OR |, AND & and difference - of sets, check subsets and supersets (like x<y)


