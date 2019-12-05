import random
print("This is a Rock, Paper, Scissors Game!")
elements = ["rock", "paper", "scissor"]
user_choice =  input("3,2,1, Choose!")
computer_choice = random.choice(elements)
print("Computer's Choice is", computer_choice)

if user_choice == computer_choice:
    print("Equality")

elif user_choice != computer_choice:
    if ((user_choice == "paper" and computer_choice == "rock") or (user_choice == "rock" and computer_choice == "scissor") or (user_choice == "scissor" and computer_choice == "paper")):
        print("User Wins!")
    else:
        print("Computer Wins!")