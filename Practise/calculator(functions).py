# Basic Calculator with Functions

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division (with zero validation)
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Function for power
def power(a, b):
    return a ** b

# Function to get user input for operation
def get_operation():
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")

    choice = input("Enter choice (1/2/3/4/5): ")
    return choice

# Function to perform calculation based on user input
def perform_calculation():
    choice = get_operation()

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")

    else:
        print("Invalid input. Please try again.")

# Main loop for continuous operation until the user decides to quit
def calculator():
    while True:
        perform_calculation()
        cont = input("Do you want to perform another calculation? (yes/no): ").lower()
        if cont != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

# Start the calculator
calculator()
