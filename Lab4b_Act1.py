# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab4b
# Date:         26 09 2021

# Takes in 3 inputs and prints the smallest one
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
if(num1<=num2 and num1<=num3):
    print("The smallest number is " + str(num1))
elif(num2<=num3 and num2<=num1):
    print("The smallest number is " + str(num2))
elif(num3<=num2 and num3<=num1):
    print("The smallest number is " + str(num3))

