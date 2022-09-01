# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab4b
# Date:         26 09 2021

from math import *

a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))
root1 = 0
root2 = 0
if(b**2-4*a*c<0):
    x1 = -b/(2*a)
    xi = sqrt(-1*(b**2-4*a*c))/(2*a)
elif(a==0):
    x1 = 0
else:
    x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2-4*a*c))/(2*a)
# Calculates the roots of a trinomial
if(a!=0):
    if(b**2-4*a*c<0):
       print("The roots are x = " + str(x1) + " + " + str(xi) + "i and x = " + str(x1) + " - " + str(xi) + "i")
    elif(b**2-4*a*c==0):
       x1 =-b/(2*a)
       print("The root is x = " + str(x1))
    else:
       print("The roots are x = " + str(x1) + " and x = " + str(x2))
elif(a==0 and b==0 and c!=0):
    print("You entered an invalid combination of coefficients")
else:
    x1 = -c/b
    print("The root is x = " + str(x1))
       
          
    
    
