import random

# get random number from computer
randomNum = random.randint(1, 10)
userNum = 0
goAgain = "yes"
goAgain = "yes"

while goAgain ==  "yes":
    randomNum = random.randint(1, 10)
    userNum = 0

    # loop while the user's guess is incorrect
    while userNum != randomNum:
         # ask the user to enter their guess - a number
        userNum = int(input("Please enter your guess: "))    
         # if the guess is too low, display too low message
        if userNum < randomNum:
            print ("Too low")
            
         # if the guess is too high, display too high message
        elif userNum > randomNum:
            print("Too high")
      
         # otherwise, print "correct"
        else:
            print ("Correct")  
    goAgain = input("do you want another go yes or no? ")

#ask the user to press close
inp = input("press any key to close")
    
