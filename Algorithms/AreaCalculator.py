from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print("Starting the calculator...")

print("Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute))

sleep(2)
      
hint = ("Don't forget to include the correct units! \nExiting...")
      
option = input("Enter C for Circle or T for Triangle: ")

option = option.upper()

if option == 'C':
    radius = float(input("Enter radius: "))
    area = pi * radius**2
    print("The pie is baking...")
    sleep(2)
    print("Area: %s. \n%s" % (area, hint))

elif option == 'T':
    base = float(input("Enter base or adjacent of triangle: "))  
    height = float(input("Enter the heigth or opposite of the triangle: "))
    area = (0.5)*base*height
    print("Uni Bi Tri...")
    sleep(2)
    print("Area: %s. \n%s" % (area, hint))
    sleep(2)
    
else:
    print(option + " is not defined. Exiting.")
    sleep(1)
    
