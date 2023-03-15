# 1 - Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class Rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width
    def areaOfRectangle(self):
        return (self.length * self.width)
rectangle = Rectangle(40,20)
print("The area is : ",rectangle.areaOfRectangle(),"m2")
# 2 - Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle : 
    def __init__(self, max_speed , mileage):
        self.max_speed = max_speed
        self.mileage = mileage
vehicle = Vehicle(300, 12000)
print("\nThe speed of the vehicle is" , vehicle.max_speed , " Km/h and its mileage is" , vehicle.mileage,"miles.\n")
# 3 - Create a Vehicle class without any variables and methods.
class Vehicle_1 : #I chose the name is Vehicle_1 to not conflit with the above one when executing the fourth question 
       pass
# 4 - Create a child class Bus that will inherit all of the variables and methods of the Vehicle class     
class Bus(Vehicle):
    def __init__(self, max_speed , mileage):
        super().__init__(max_speed , mileage)
    pass
bus = Vehicle(150 , 12000)
print("The speed of the bus is" , bus.max_speed , "Km/h and its mileage is" , bus.mileage,"miles.\n")
