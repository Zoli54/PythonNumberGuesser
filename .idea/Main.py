import random
import os
import sys

#This class generates a random number.
class numberGenerater:
    randomNum = int(random.randint(1,5))

#User tries to guess the number.
class Running:
    
# User chooses a number.
    userNum = input("What number am I thinking about? \n Take a guess: ")
    print("Your chosen number is : " + userNum)
    print()

#The program checks if its correct.
    print("Lets see if you're correct...")
    print()
    computerNum = numberGenerater()
    if userNum == computerNum.randomNum :
        print("YES")
        print("I was thinking about number " + str(computerNum.randomNum))
    else :
        print("no :( ")
        print("Unfortunatelly I was thinking about number " + str(computerNum.randomNum))
    print()

#If the user lost, it can try again.
    print("Want to try again?\nIf you want to please press Y\nIf not press N")
    print()
    answer = str(input("Write your answer here: "))
    if answer.upper() == 'Y' :
        os.execl(sys.executable, sys.executable, *sys.argv)
    if answer.upper() == 'N' :
        exit()
    if answer != 'N' or 'Y':
        print("Why did you fail me...")
        exit()