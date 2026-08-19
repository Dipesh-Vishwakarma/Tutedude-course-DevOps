# calculator.py
# A simple menu-driven calculator program demonstrating basic Python concepts.

# Separate functions for basic arithmetic operations
def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2

def multiply(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2

def divide(num1, num2):
    """Returns the quotient of two numbers or an error message if dividing by zero."""
    if num2 == 0:
        return "Error: Cannot divide by zero."
    return num1 / num2

def main():
    # Loop until the user chooses to exit (Option 5)
    while True:
        # Display the calculator menu
        print("\n===== Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        # Get user's menu choice
        choice = input("\nEnter your choice: ").strip()

        # Handle Exit choice
        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        # Use if / elif / else to check user choice
        if choice in ("1", "2", "3", "4"):
            try:
                # Ask user to enter two numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            # Call appropriate function based on user's choice
            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)

            # Check if result is an error message (string) or a calculation result
            if isinstance(result, str):
                print(f"\n{result}")
            else:
                # Convert float to integer if there are no decimal places (e.g. 5.0 -> 5)
                if result.is_integer():
                    result = int(result)
                print(f"\nResult: {result}")
        else:
            # Handle invalid menu choice
            print("Invalid choice! Please select a valid option (1-5).")

# Run the calculator program
if __name__ == "__main__":
    main()
