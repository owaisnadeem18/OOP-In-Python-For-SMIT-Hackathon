# Here , we have to understand the concept of self


class Student: 
    University = "Dawood UET"
    def getPercentage(self , remarks , name ):
        print(f"The percentage of student , from {self.University} is {self.percentage}% which is very {remarks} and the name of student is {name} ")

    @staticmethod
    def GoodMorning():
        print("Good Morning ! ")

    # Another Static Method:

    @staticmethod
    def TimeNow():
        print(f"The time now is 9PM")  


owais = Student()
owais.percentage = 94
owais.getPercentage("Good" , "Owais")
owais.GoodMorning() # == GoodMorning(owais)
owais.TimeNow()