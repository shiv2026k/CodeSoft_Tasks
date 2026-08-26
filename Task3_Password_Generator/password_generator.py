# CODSOFT Python Programming Internship
# Task 3 - Password Generator

import random
import string


def generate_password(length):
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("==============================")
    print("      PASSWORD GENERATOR")
    print("==============================")

    while True:
        try:
            length = int(input("Enter password length: "))

            if length <= 0:
                print("Password length must be greater than 0.")
                continue

            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

            again = input("\nGenerate another password? (y/n): ").lower()

            if again != "y":
                print("Thank you for using Password Generator.")
                break

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()