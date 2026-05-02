# game.py
# Stone-Paper-Scissors Game

import random

def get_user_choice():
    print("\nChoose one option:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        return "Stone"
    elif choice == "2":
        return "Paper"
    elif choice == "3":
        return "Scissors"
    else:
        print("Invalid choice. Try again.")
        return None

def get_computer_choice():
    return random.choice(["Stone", "Paper", "Scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Stone" and computer == "Scissors") or \
         (user == "Paper" and computer == "Stone") or \
         (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    while True:
        print("\n===== Stone-Paper-Scissors =====")
        user_choice = get_user_choice()
        if not user_choice:
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        print(decide_winner(user_choice, computer_choice))

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()