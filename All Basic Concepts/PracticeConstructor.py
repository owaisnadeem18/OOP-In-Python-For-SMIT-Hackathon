class Car():
    def __init__(self , model , price , engineCC , kmDriven):
        self.model = model
        self.price = price
        self.engineCC = engineCC
        self.kmDriven = kmDriven

        print("I am car Constructor")

    def getCarDetails(self):
        print(f'The model of car is => {self.model} and the price is => {self.price} ')

    def getCarEngineDetails (self):
        print(f'The Engine of car is => {self.engineCC} and the driven km is => {self.kmDriven} ')

# Now, create an object instance here: 

CarObject = Car(2020 , 3400000 , 4000 , 1000)

CarObject.getCarDetails()
CarObject.getCarEngineDetails()
