class Car:
    """
    - Defined a class named Car with attributes: make, model, year
    - Initialized these attributes in the __init__ method
    - Added a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def describe_car(self):
        print(self.year, self.make, self.model)


# Created an instance of the Car class with the following attributes and called describe_car method:
p1 = Car("Toyota","Corolla","2020")
p1.describe_car()
