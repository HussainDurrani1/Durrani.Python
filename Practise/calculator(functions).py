def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def get_operation():
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    return input("Enter choice (1/2/3/4): ")

def perform_calculation():
    operation = get_operation()

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input. Please try again.")

def calculator():
    while True:
        perform_calculation()
        if input("Do you want to perform another calculation? (yes/no): ").lower() != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

calculator()
