import math

name = input("Enter your name: ").strip().title()
radius = float(input("Enter radius: "))

area = math.pi * math.pow(radius, 2)

print(f"Hello {name}, the area is {area:.2f}")
