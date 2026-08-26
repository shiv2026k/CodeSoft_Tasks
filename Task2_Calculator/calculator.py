# CODSOFT Python Programming Internship
# Task 1 - Calculator

def calculator():
    while True:
        print("==========================")
        print("      PYTHON CALCULATOR"                                                      )
        print("==========================")

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Thank you for using the calculator.")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                operation = "+"

            elif choice == "2":
                result = num1 - num2
                operation = "-"

            elif choice == "3":
                result = num1 * num2
                operation = "*"

            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue

                result = num1 / num2
                operation = "/"

            print(f"\n{num1} {operation} {num2} = {result}")

        except ValueError:
            print("Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
