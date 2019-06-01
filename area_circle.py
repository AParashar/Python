import math

input_status = True

while input_status:
    try:
        radius = int(input("Please enter Radius: "))
        input_status = False
    except:
        print("Invalid Entry. Try again!")
        input_status = True

def calculate_area():
    return math.pi * radius * radius

print("Area of the circle is: ", round( calculate_area(), 2))
