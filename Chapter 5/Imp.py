# write a python program to create two models of math calculation and measurement in mathcalculation model create these methods(sum, subtract, devision),
# in Measurement Model . Create Two methods area of circle and area of rectangle.Then using both models create an app to calculate sum, divison and area of circle .
import math
# Math Calculation Model
class MathCalculation:
    def sum(self, a,b):
        return a+b
    def subtract(self, a,b):
        return a-b
    def divide(self, a,b):
        if b!=0:
            return a/b
        else:
            return "Division by 0 is not allowed"
    # Measurement Model
class Measurement:
    def area_circle(self, radius):
        return math.pi * radius**2
    def area_rectangle(self, lenght, width):
        return lenght*width
# app using both models
math_obj = MathCalculation()
measure_obj = Measurement()

# calculations
print("Sum:", math_obj.sum(1,2))
print("Subtract:", math_obj.subtract(1,2))
print("Divide:", math_obj.divide(1,2))
print("Are of Circle:", measure_obj.area_circle(2))
