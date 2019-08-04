from math import sqrt

print("Please input the short edge of a triangle")
a = input()
print("Please input the second short edge of a triangle")
b = input()

print("The long edge of the triangle is {} in length.".format(sqrt(int(a)**2 + int(b)**2)))
