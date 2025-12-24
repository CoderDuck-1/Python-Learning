#Create a sample class named Employee with two attributes id and name
#employee :
#   id
#    name
#object initializes id and name dynamically for every Employee object created.
#emp = Employee(1, "coder")
#Use del property to first delete id attribute and then the entire object

#Ans)
class Employee:
    def __init__(self,i,n):
        self.ID=i
        self.Name=n

emp=Employee(1, "coder")

print(emp.ID)
print(emp.Name)
del(emp.ID)
del(emp)