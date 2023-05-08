I have written the complete program as mentioned in the question using python. i have created all the functions required along with the main function and also added suffiecient comments for you to understand.

Note: You may see the screenshot of the code to have better understanding of the indentation

Python Code:

import random #random library for random numbers

#function to read student NAME
def inputNames():
    name = input("Enter Student Name: ")
    return name #return name to main

#function to set random numbers
def getNumbers():
    #this function will generate random number
    #from 1 to 500 (501 exclusive)
    num1 = random.randrange(1, 500)
    num2 = random.randrange(1, 500)
    return num1, num2

#function to return ans as sum
def getAnswer(num1, num2, ans):
    print("What is the answer to the following equation")
    print(str(num1) + "\n+\n" + str(num2))
    print("What is the sum", sep = ': ')
    ans = int(input()) #take user input for ans as integer
    return ans

#function to check for right answer
def checkAnswer(num1, num2, ans, right):
    if ans == num1 + num2: #check for sum
        print("Right")
        right = right + 1 #increment right answers
    else:
        print("Wrong")
    return right

#function to calculate avg result
def results(right, averageRight):
    averageRight = right/10
    return averageRight
  
#function to print results
def displayInfo(right, averageRight, studentName):
    print("Infomation for student: "+studentName)
    print("The number right: "+str(right))
    print("The average right is "+str(averageRight)+" or "+str(averageRight*100)+" %")
  
#main function
def main():
    #declare local variables
    c = 0 #integer counter
    studentName = "NO NAME" #student NAME
    averageRight = 0.0 #average right answers
    right = 0 #right answers
  
    num1 = 0 #first number
    num2 = 0 #second number
    ans = 0 #ans entered by user
  
    #call function to get student NAME
    studentName = inputNames()
  
    #loop for program
    while c < 10:
        #call function to get numbers
        num1, num2 = getNumbers()
      
        #get answer from user
        ans = getAnswer(num1, num2, ans)
      
        #check for right answer
        right = checkAnswer(num1, num2, ans, right)
      
        #increment counter
        c = c + 1
  
    #calculate results
    averageRight = results(right, averageRight)
  
    #print results
    displayInfo(right, averageRight, studentName)
      
#call main function
main()
