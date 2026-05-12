import math 

x = int(input("enter an angle: "))

angle = math.radians(360 - x)

print("y: ", math.sin(angle) + 1)
print("x: ", math.cos(angle) + 3.5)

print("y2: ", math.sin(angle) + 1 + 0.1)
print("x2: ", math.cos(angle) + 3.5 + 0.1)


