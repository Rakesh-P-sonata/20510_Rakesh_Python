user_action1 = input("Enter a choice rock, paper, scissors: ")
user_action2 = input("Enter a choice rock, paper, scissors: ")
print(f"\nYou chose {user_action1}, User 2 chose {user_action2}.\n")


def RPS(user_action1, user_action2):
    if user_action1 == user_action2:
        print(f"Both players selected {user_action1}. It's a tie!")
    elif user_action1 == "rock":
        if user_action2 == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif user_action1 == "paper":
        if user_action2 == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif user_action1 == "scissors":
        if user_action2 == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")


RPS(user_action1, user_action2)
