#Rock , paper , Scissors
import random

exit = False
user_score = 0
computer_score =0
while exit == False:
    option = ["rock","paper","scissors"]
    user_input= input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(option)

    if user_input == "exit":
        print("Game ended")
        print("You won a total score of " + str(user_score) + "and the computer total score is "+ str(computer_score))
        exit = True
    
    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a tie")
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer Wins!")
            computer_score += 1
        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print(" You Win!")
            user_score += 1

    elif user_input == "paper":
        if computer_input =="rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You Win!")
            user_score += 1
        elif computer_input == "paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("Its a tie")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer Wins!")
            computer_score += 1

    elif user_input == "scissors":
        if computer_input =="rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer Wins!")
            computer_score += 1 
        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You Win!")
            user_score += 1
        elif computer_input=="scissors":
            print("Your input is scissor")
            print("Computer input is scissors")
            print("Its a tie!")
        
    elif user_input != "rock" or user_input != "paper" or user_input != "scissors":
        print("invalid input")
    
