### CS 22B Module 07 - Homework 7
### Name: Ali Alibrahimi

### Homework 7: Object-Oriented Programming (OOP) in Python
## In this homework we will create a superclass Rectangle and subclass Square

### Problem 1: Define a class called Rectangle that contains:
# attributes height and width 
# methods area() and perimeter() 

class Rectangle:
  def __init__(self, height: int, width: int):
    self.height = height
    self.width = width

  def area(self) -> int:
    return self.height * self.width
  
  def perimeter(self) -> int:
    return 2 * (self.height + self.width)

   

## Use case: Create an instance of the Rectangular class and call the area and perimeter methods to verify that they work correctly.
my_rectangle = Rectangle(17, 8)
print(f"Rectangle Area: {my_rectangle.area()}")
print(f"Rectangle Perimeter: {my_rectangle.perimeter()}")


### Problem 2: Define a subclass called Square that 
# inherits from parent class Rectangle
# Using super(), will set .height and .width attributes from inherited superclass Rectangle.__init__()
class Square(Rectangle):
  def __init__(self, side_length: int):
    super().__init__(side_length, side_length)
    self.side_length = side_length

 
 
## Use case: Create an instance of the Square class and call the area and perimeter methods to verify that they work correctly.
my_square = Square(17)
print(f"Square Area: {my_square.area()}")
print(f"Square Perimeter: {my_square.perimeter()}")

### Problem 3: Create a new class Cube that inherits from parent class Square
# Use super() to set .height and .width attributes from inherited superclass Square.__init__()
# Define new methods surface_area() and volume() that calculate the surface area and volume of the cube using the inherited attribute 

class Cube(Square):
  def __init__(self, side_length: int):
    super().__init__(side_length)

  def surface_area(self) -> int:
    return 6 * self.side_length**2
  
  def volume(self) -> int:
    return self.side_length**3
   

## Use case: Create an instance of the Cube class and call the surface_area and volume methods to verify that they work correctly.
my_cube = Cube(17)
print(f"Cube Surface Area: {my_cube.surface_area()}")
print(f"Cube Volume: {my_cube.volume()}")