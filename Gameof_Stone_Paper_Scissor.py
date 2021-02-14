import random
import shutil
from simple_colors import *
col= shutil.get_terminal_size().columns

print (red("Welcome to Suhail's Gaming Section".center(col)))
print(yellow(" Are you excited to play Stone, Paper, Pencil and Gun?".center(col)))
print(green("So ....Lets Play".center(col)))

Players_name= input("Enter the Players name: ")
def game():
    computerss_score=0
    Playerss_score= 0
    n=1
    while (n<=10):
        lst =["stone","paper","pencil","scissor"]
        Playerss_choice= input("Select Stone, Paper, Pencil or Scissor: ". lower())
        com_choice= random.choice(lst)
#
        if Playerss_choice=="stone":
            if com_choice=="stone":
                print("Its a draw")
                print("Computer Chooses", com_choice)
                print("Your Score: ", Playerss_score, "and Computer's Score: ",computerss_score)
                print("Play again")
                print(10-n, "chances left")

            elif com_choice=="pencil":
                print(Players_name, " Won")
                print("Computer Chooses", com_choice)
                Playerss_score += 1
                print("Your Score: ", Playerss_score, "and Computer's Score: ",computerss_score)

                print(10-n, "chances left")
            elif com_choice=="paper":
                print("You Lost")
                print("Computer Chooses", com_choice)
                computerss_score +=1
                print("Your Score: ", Playerss_score, "and Computer's Score: ",computerss_score)

                print("Play again")
                print(10-n, "chances left")

            elif com_choice == "scissor":
                print("You Won")
                print("Computer Chooses", com_choice)
                Playerss_score += 1
                print("Your Score: ", Playerss_score, "and Computer's Score: ", computerss_score)

                print("Play again")
                print(10 - n, "chances left")
#
        elif Playerss_choice == "paper":
            if com_choice == "stone":
                print("You Won")
                print("Computer Chooses", com_choice)
                Playerss_score += 1
                print("Your Score: ", Playerss_score, "and Computer's Score: ", computerss_score)
                print("Play again")
                print(10 - n, "chances left")

            elif com_choice == "paper":
                print("Draw")
                print("Computer Chooses", com_choice)
                print("Your Score: ", Playerss_score, "and Computer's Score: ", computerss_score)
                print(10 - n, "chances left")
                print("Play again")

            elif com_choice == "pencil":
                print("Computer Won")
                print("Computer Chooses", com_choice)
                computerss_score += 1
                print("Your Score: ", Playerss_score, "and Computer's Score: ", computerss_score)
                print(10 - n, "chances left")

            elif com_choice == "scissor":
                print("Computer Won")
                print("Computer Chooses", com_choice)
                computerss_score += 1
                print("Your Score: ", Playerss_score, "and Computer's Score: ", computerss_score)
                print("Play again")
                print(10 - n, "chances left")

        elif Playerss_choice == "pencil":
            if com_choice == "stone":
                print("You Won")
                print("Computer Chooses", com_choice)
                Playerss_score += 1
                print("Your Score: ", Playerss_score, "and Computer's Score: ", computerss_score)
                print("Play again")
                print(10 - n, "chances left")

            elif com_choice == "paper":
                print("You lose")
                print("Computer Chooses", com_choice)
                computerss_score += 1
                print("Your Score: ", Playerss_score, "and Computer's Score: ", computerss_score)

                print(10 - n, "chances left")
            elif com_choice == "pencil":
                print("Draw")
                print("Computer Chooses", com_choice)
                Playerss_score += 1
                print("Your Score: ", Playerss_score, "and Computer's Score: ", computerss_score)

                print("Play again")
                print(10 - n, "chances left")
            elif com_choice == "scissor":
                print("You Won")
                print("Computer Chooses", com_choice)
                Playerss_score += 1
                print("Your Score: ", Playerss_score, "and Computer's Score: ", computerss_score)
                print("Play again")
                print(10 - n, "chances left")
        n+=1
        if (Playerss_score<computerss_score):
            print("You lose")

        elif(Playerss_score>computerss_score):
            print("You Won")
        else:
            print("Its a Tie")

    yes= input("Press y to play again or n to quit: ")
    if yes=='y':
        game()
    elif yes=='Y':
        print("Wrong input, please press y")
    else:
        exit()

game()

