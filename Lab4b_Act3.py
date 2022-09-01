# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Caleb Lewis
# Section:      521
# Assignment:   Lab4b
# Date:         26 09 2021

# Calculates the number of total widgets created by the day the user inputs
total = 0
days = int(input("Please enter a positive value for day: "))
if(days<0):
    print("You entered an invalid number!")
elif(days<=10):
    total = days*10
    print("The total number of widgets produced on day " + str(days) + " is " + str(int(total)))
elif(days<=50):
    total = ((days+11)/2)*(days-10)+100
    print("The total number of widgets produced on day " + str(days) + " is " + str(int(total)))
else:
    peas = days
    if(days>100):
        peas = 100     
    total = 1320 + (50*(peas-50))
    print("The total number of widgets produced on day " + str(days) + " is " + str(int(total)))

    
    
