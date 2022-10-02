import time
print("Welcome to factorial program")
print("press q for quit ")
while True:
    userInput=int(input("Please enter your value"))
    if userInput > 1 :
        print("You entered your number, program is starting")
        time.sleep(3)
        i = userInput
        while(i >1):
            i -= 1
            userInput *= i
        print("values:", userInput)

    elif (userInput == "q"):
        print("You are closing the program...")
        time.sleep(3)
        break
    elif(userInput < 0):
        convertedUserInput=abs(userInput)
        print("You entered negative value, input is converting to positive..")
        time.sleep(3)
      # function will be added

    elif (userInput  == 1 or userInput == 0 ):

        convertedUserInput = abs(userInput)
        print("Program is working....")
        time.sleep(3)
        print("Factorial of {} is {}".format(userInput,1))

    else:
        print("unknown value program is closing")
        time.sleep(3)
        break