#Student ID: 1201201476#
#Student Name:Eng Hong Chee#

import math

radius = float(input("Enter radius: "))

volume = 4/3 * math.pi * radius**3
sarea = 4 * math.pi * radius**2

print("Volume of sphere      : {:.2f}".format(volume))
print("Surface area of sphere: {:.2f}".format(sarea))