# OOP Basic Concepts and Understanding: 

class Employee:
    company = "Owais Tech Pvt. Ltd"
    salary = 100000

newEmployee = Employee()

newEmployee.company = "Saad tech Pvt.Ltd" 

newEmployee.salary = 300000  # instance attribute
# This instance attribute will get more priority always and get printed 

print(Employee.company) # will print class attributes
print(Employee.salary) # will print class attributes

print(newEmployee.company)
print(newEmployee.salary)