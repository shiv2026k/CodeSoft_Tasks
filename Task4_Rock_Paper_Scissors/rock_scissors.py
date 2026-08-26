# CODSOFT Python Programming Internship
# Task 4 - Rock Paper Scissors Game

import random


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"

    if (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "scissors" and computer_choice == "paper")
        or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"

    return "computer"


def play_game():
    choices = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0
    ties = 0

    print("==============================")
    print("    ROCK PAPER SCISSORS")
    print("==============================")

    while True:
        print("\nChoose:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "4":
            break

        choice_map = {
            "1": "rock",
            "2": "paper",
            "3": "scissors"
        }

        if choice not in choice_map:
            print("Invalid choice.")
            continue

        user_choice = choice_map[choice]
        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "user":
            print("You win!")
            user_score += 1

        elif winner == "computer":
            print("Computer wins!")
            computer_score += 1

        else:
            print("It's a tie!")
            ties += 1

        print("\n===== SCORE =====")
        print(f"Your Score     : {user_score}")
        print(f"Computer Score : {computer_score}")
        print(f"Ties           : {ties}")

        play_again = input("\nPlay again? (y/n): ").lower()

        if play_again != "y":
            break

    print("\n==============================")
    print("          FINAL SCORE")
    print("==============================")
    print(f"Your Score     : {user_score}")
    print(f"Computer Score : {computer_score}")
    print(f"Ties           : {ties}")
    print("Thank you for playing!")


if __name__ == "__main__":
    play_game()