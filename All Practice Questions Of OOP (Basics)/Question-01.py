# Create class Programmer for storing info of few programmers working at Microsoft: 

class Student():
    def __init__(self , id , dept , name):
        self.id = id 
        self.dept = dept
        self.name = name

    def student_Details(self):
        print(f"The name of the student is '{self.name}' bearing the roll # '{self.id}' from dept. '{self.dept}'")

student_1 = Student(983 , "Owais Nadem" , "BSCS")
student_2 = Student( 4334,"Wifey aka Rabia Owais" , "Baatain banana or baatain sunana")

student_1.student_Details()
student2.student_Details()
