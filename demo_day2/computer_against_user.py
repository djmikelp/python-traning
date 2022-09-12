import random


def winner(user_option, computer_option):
    if user_option == "rock" and computer_option == "scissors":
        return user_option
    elif user_option == "rock" and computer_option == "paper":
        return computer_option
    elif user_option == "paper" and computer_option == "rock":
        return user_option
    elif user_option == "paper" and computer_option == "scissors":
        return computer_option
    elif user_option == "scissors" and computer_option == "rock":
        return computer_option
    elif user_option == "scissors" and computer_option == "paper":
        return user_option


list_choice = ["rock", "paper", "scissors"]
print("*** rock, paper, scissors ***")
user_choice = input("Enter your option: ")
computer_choice = random.choice(list_choice)
print("computer option : ",computer_choice)
user_choice = user_choice.lower()
user_choice = user_choice.strip()
if user_choice in list_choice:
    if user_choice == computer_choice:
        print("Tie")
    elif winner(user_choice, computer_choice) == user_choice:
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid option")

