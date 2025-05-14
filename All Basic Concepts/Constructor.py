# Here , we have to understand the concept of self


class Student: 
    University = "Dawood UET"
    def getPercentage(self , remarks , name ):
        print(f"The percentage of student , from {self.University} is {self.percentage}% which is very {remarks} and the name of student is {name} ")

    def __init__(self , cgpa , field , department ):

        # Let me accept some details from the parameters: 

        self.cgpa = cgpa
        self.field = field
        self.department = department

        print("I am a constructor , I will run immediately at the time of running the code once the object will get created (either the function called by the object or not")

    def showDetails(self): 
        print(f'''
            The cgpa of student is {self.cgpa} from the department {self.department} in the field of {self.field}
        ''')

    @staticmethod
    def GoodMorning():
        print("Good Morning ! ")

    # Another Static Method:

    @staticmethod
    def TimeNow():
        print(f"The time now is 9PM")  


owais = Student(3.5 , "BSCS" , 'MERN Stack' )

owais.showDetails()

# owais.percentage = 94
# owais.getPercentage("Good" , "Owais")
# owais.GoodMorning() # == GoodMorning(owais)
# owais.TimeNow()