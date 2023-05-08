# LargeSmall.py - This program calculates the largest and smallest of three integer values. 
# Declare and initialize variables here
largest = int
smallest = int

# Prompt the user to enter 3 integer values
number1 = int(input('Enter First number : ')) 
number2 = int(input('Enter Second number : '))
number3 = int(input('Enter Third number : ')) 
# Write assignments, and necessary if else statements here as appropriate
if (num1 > num2) and (num1 > num3):
        largest_num = num1
elif (num2 > num1) and (num2 > num3):
        largest_num = num2
else:
        largest_num = num3
    print("The largest of the 3 numbers is : ", largest_num)
def smallest(num1, num2, num3):
 if (num1 < num2) and (num1 < num3):
        smallest_num = num1
 elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
else:
        smallest_num = num3
# Output largest and smallest number. 
print("The largest value is " + str(largest))
print("The smallest value is " + str(smallest))

