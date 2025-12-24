# w : write mode - Removes the old data and adds new
# a : append mode - adds data to end of file
# r : read mode - used to read file
#r+ : Opens file for both reading and writing
#w+ : Opens for both reading and writing - if not present, it creates a new one. If present, it overwrites the data

# Writing data into a file

with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/funny.txt", "w") as f:
   f.write("I love C++")
with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/funny.txt", "a") as f:
   f.write("\nI love Python as well")

#Reading file

with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/funny2.txt", "r") as f:
   print(f.read())

with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/funny2.txt", "r") as f:
   for line in f:
      print(line)

with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/funny2.txt", "r") as f:
   for line in f:
       words=line.split(" ") #This function separates the words in each line according to the given separator, which can be stored in a list
       print(type(words))
       print(words)
       print(len(words))

with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/funny2.txt", "r") as f:
   with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/funny_3.txt", "w") as f_out:
     for line in f:
         word=line.split()
         f_out.write(line+" word count: "+str(len(word))+" ")

with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/funny2.txt", "r") as f:
   with open("C:/Users/Lakshya/Desktop/Python Projects/Sample/funny_4.txt", "w") as f_out:
     for line in f:
         word=line.split()
         f_out.write(line.strip()+", word count: "+str(len(word))+"\n") #strip function removes the Leading and trailing spaces (of any kind like \n \t simple space etc
         #lstrip() and rstrip()