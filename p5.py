# Head or Tails Simulator 

from random import choice #choice is a function that randomly chooses from a list

while True:
    print("Welcome to our head or tails game..")
    print("Please choose either heads or tails.")
    while True:
        user_input = input("User's choice: ")
        user_input = user_input.lower()  #makes everything lowercased

        if user_input in {"heads", "tails", "head", "tail"}:
            #user_input was valid, we cant exit the infinite loop 
            break 
        else: 
            print("please type in heads or tails !!")
    # end of while 
    flip_result = choice(["heads", "tails"])

    if user_input in {"heads", "head"} and flip_result == "heads":
        print("the user guessed correctly !!!")
    elif user_input in {"tails", "tail"} and flip_result == "tails":
        print("the user guessed correctly !!!")
    else: 
        print("u lose!")

    user_input = input("would you still like to play? say yes/no: ")
    if user_input.lower() == "yes":
        print("goodbye !") 
        break

# end of flip checking 

