### This template is for the class demo and exercises covered in M07_Lec12_oop for CS 22B.
import math

class Car:
    ## Initializer method - set up the attributes for Car class
    def __init__(self, make: str, model: str, color: str):
        self.make = make
        self.model = model
        self.color = color

    def get_description(self):
        '''Instance method that returns a string description of the car.'''
        return f"The {self.make} {self.model} is colored {self.color}"
    
    
## Instantiate a Car object. Instance attributes 
toyota_supra = Car("Toyota", "Supra MK3 1988", "Red")


## Call our instance method
print(toyota_supra.get_description())


### Child class that inherits from Car
class GasCar(Car):
    def __init__(self, make: str, model: str, color: str, fuel_tank_size: float | int):
        super().__init__(make, model, color)
        self.fuel_tank_size = fuel_tank_size
       
    def get_fuel_tank_info(self):
        '''Instance method that returns a string description of the fuel tank.'''
        return f"Your {self.model} has a {self.fuel_tank_size} gallon fuel tank"
        
        
class ElectricCar(Car):
    def __init__(self, make: str, model: str, color: str, battery_size: int):
       super().__init__(make, model, color)
       self.battery_size = battery_size

    def get_battery_info(self):
        '''Instance method that returns a string description of the battery.'''
        return f"Your {self.model} has a {self.battery_size}kWh battery"
       
       
class HybridCar(Car):
    def __init__(self, make: str, model: str, color: str, fuel_efficiency: int):
        super().__init__(make, model, color)
        self.fuel_efficiency = fuel_efficiency
        
    def get_fuel_efficiency_info(self):
        '''Instance method that returns a string description of the fuel efficiency.'''
        return f"Your {self.model} is {self.fuel_efficiency} MPG ( Miles per Gallon )"
        
 
### Example usage of child classes
gas_car = GasCar("Toyota", "Supra MK3 1988", "Red", 18.5)
print(gas_car.get_description())


##### Example of superclass and subclass ####
## We will create a class called Circle that has 
# attribute radius
# methods area() and circumference()   

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

        
    def area(self):
        return math.pi * self.radius**2
        
       
    
    def circumference(self):
        return 2 * math.pi * self.radius**2
    
## Use case: Create an instance of the Circle class and call the area and circumference methods to verify that they work correctly.
my_circle = Circle(5)
print("Area of the circle:", round(my_circle.area(), 2))


### Now we will create a subclass called Cylinder that inherits from parent class Circle
# Using super(), will set .radius attribute from inherited superclass Circle.__init__()
# Define new methods surface_area() and volume() that calculate the surface area and volume of the cylinder using the inherited attribute
class Cylinder(Circle):
    def __init__(self, radius: int, height: int):
        super().__init__(radius)
        self.height = height
        
    def surface_area(self):
        base_area = self.area()  # Area of the circular base
        lateral_area =  base_area * self.height # Lateral surface area is circumference of base * height
        total_surface_area = (2 * base_area) * lateral_area # SA is 2x base * lateral
        return total_surface_area
   

    def volume(self):
        base_area = self.area() # Area of the circular base
        volume = base_area * self.height # Vol is base * height
        return volume


## Use case: Create an instance of the Cylinder class and call the surface_area and volume methods to verify that they work correctly.
my_cylinder = Cylinder(3, 5)
print("Surface area of the cylinder:", round(my_cylinder.surface_area(), 2))


### Now we creat a subclass Spheres that inherits from parent class Circle
# Using super(), will set .radius attribute from inherited superclass Circle.__init__()
# Define new methods surface_area() and volume() that calculate the surface area and volume of the sphere using the inherited attribute
class Sphere(Circle):
    def __init__(self, radius: int):
        super().__init__(radius)
    
    def surface_area(self):
        surface_area = 4 * self.area()  # SA 4x area 
        return surface_area
        

    def volume(self):
        volume = (4/3) * math.pi * self.radius**3 # Vol is (4/3)*pi*r^3
        return volume
       
    
## Use case: Create an instance of the Sphere class and call the surface_area and volume methods to verify that they work correctly.
my_sphere = Sphere(3)
print(f"Sphere Surface Area: {round(my_sphere.surface_area(), 2)}")
print(f"Sphere Volume: {round(my_sphere.volume(), 2)}")