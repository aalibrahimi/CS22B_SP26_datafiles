### CS 22B Module 03 - Homework 5
### Name: Ali Alibrahimi

##### Homework to practice writing Exceptions #####

##### Problem 1: Math Function with Exception Handling #####
## Write a Python function calculate_square_root(number) that takes a single argument number. The function should:
## Raise a ValueError with the message "Input must be a non-negative number" if the input is negative.
## Use a try-except block to catch the ValueError when you call the function and print the error message. If no exception occurs, return the square root of the number (you can use number ** 0.5 for simplicity).

def calculate_square_root(number: int):
    try:
        if number < 0:
            raise ValueError
        return number ** (1 / 2)
    except ValueError:
        print("Input must be a non-negative number")


print(calculate_square_root(27))

##### Problem 2: Re-write Exception Handling #####
## A Python programmer has written a piece of code below, that reads a DNA sequence from a file and splits it up into a set number of equal-sized pieces (ignoring any incomplete pieces at the end of the sequence). It asks the user to enter the name of the file and the number of pieces, calculates the length of each piece (by dividing the total length by the number of pieces), then uses a range() to print out each piece.
## Re-write the python program in the empty cell below. Use try/except blocks to handle all the potential exceptions that may arise such as giving it the name of a non-existent file, or entering zero when asked for the number of pieces – or indeed, entering something that isn't a number at all when asked for the number of pieces. The input file dna_test.txt can be used to test your program.

## This is the original python program
"""
import os
import sys

DNA = "CTAGCTAGGCGAGCTACGAGAGCTAGCGAGACATCGATCAGTACGATCGACTCGACTAGCTACGACTACGATCAGCTACGATC"
f = open("dna_test.txt", 'w')
f.write(DNA)
f.close()

# check for valid filename
input_file = input('enter filename:\n')
if not os.path.isfile(input_file):
    sys.exit('not a valid filename')

f = open(input_file)
dna = f.read().rstrip("\n")

# check for valid number
pieces = input('enter number of pieces:\n')
if not pieces.isdigit():
    sys.exit('not a valid number')

# check that number is not zero or negative
pieces = int(pieces)
if pieces <= 0:
    sys.exit('number of pieces must be greater than zero')
# do the processing
piece_length = int(len(dna) / pieces)
print('piece length is ' + str(piece_length))
for start in range(0, len(dna) - piece_length + 1, piece_length):
    print(dna[start:start + piece_length])
"""
import re
import sys

filename = input("Enter file name:\n")
try:
    dna = ""
    with open(filename, "r", encoding="UTF-8") as file:
        contents = file.read().strip()
        if re.search(r"^[ATCG]+$", contents):
            dna = contents
        else:
            sys.exit("Could not find any DNA within file")
    
    pieces = int(input("Number of pieces to split DNA:\n"))
    if pieces <= 0:
        raise ValueError
    
    piece_length = int(len(dna) / pieces)
    
    for pos in range(0, len(dna) - piece_length + 1, piece_length):
        print(dna[pos:pos + piece_length])
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Number of pieces must be a greater than 0")


##### Problem 3: Writing a python class with exception handling #####
### Write a Python class TemperatureConverter with the following functionality:

## Constructor (init):
## Accepts two parameters: a numeric temperature and a scale ("C" for Celsius or "F" for Fahrenheit).
## Validates that: temperature is a number. Raise a TypeError if not. scale is either "C" or "F" (case-insensitive). Raise a ValueError if invalid.

## Methods:
## to_fahrenheit(): Converts the temperature to Fahrenheit: -> If the scale is "C", check if the input is above absolute zero (-273.15°C). If not, raise a ValueError. -> If the scale is "F", return the temperature as-is.
## to_celsius(): Converts the temperature to Celsius: -> If the scale is "F", check if the input is above absolute zero (-459.67°F). If not, raise a ValueError. -> If the scale is "C", return the temperature as-is.

## Requirements:
## Implement exception handling (try-except) for invalid inputs when creating an instance of the class or calling its methods.
## Demonstrate the following cases:
## - Converting 100°C to Fahrenheit.
## - Converting 32°F to Celsius.
## - Passing an invalid scale (e.g., "K") to the constructor.
## - Providing a temperature below absolute zero for either scale.

class TemperatureConverter:
    def __init__(self, temperature: int | float, scale: str):
        try:
            self.temperature = temperature
            if not self.temperature.is_integer():
                raise TypeError
            if scale.upper() == "C" or scale.upper() == "F":
                self.scale = scale.upper()
            else:
                raise ValueError
        except TypeError:
            print("Temperature must be a number")
        except ValueError:
            print(
                "Temperature scale must be either `C` ( Celsius ) or `F` ( Fahrenheit )")
    
    def to_fahrenheit(self):
        try:
            if self.scale == "C" and self.temperature < -273.15:
                raise ValueError
            elif self.scale == "F":
                return self.temperature
            else:
                return (self.temperature * 1.8) + 32
        except ValueError:
            print(
                "Temperature Celsius must be above absolute zero point ( -273.15 )")
    
    def to_celsius(self):
        try:
            if self.scale == "F" and self.temperature < -459.67:
                raise ValueError
            elif self.scale == "C":
                return self.temperature
            else:
                return (self.temperature * 1.8) + 32
        except ValueError:
            print(
                "Temperature Fahrenheit must be above absolute zero point ( -459.67 )")


# Case 1: Converting 100°C to Fahrenheit.
case1 = TemperatureConverter(100, "C").to_fahrenheit()
print(f"{case1}°F")
# Case 2: Converting 32°F to Celsius.
case2 = TemperatureConverter(32, "F").to_celsius()
print(f"{case2}°C")
# Case 3: Passing an invalid scale (e.g., "K") to the constructor.
TemperatureConverter(100, "K")
# Case 4: Providing a temperature below absolute zero for either scale.
case4 = TemperatureConverter(-300, "C").to_fahrenheit()
print(f"{case4}°F")
