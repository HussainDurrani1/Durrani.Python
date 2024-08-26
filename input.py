# Step 1: Gather user information
name = input("Enter your Name Sir: ")

# Step 2: Collect the three favorite numbers
numbers = []
for i in range(1, 4):
    num = int(input(f"Enter your {i} favorite number: "))
    numbers.append(num)

# Step 3: Greet the user
print(f"\nHello, {name.title()}! Let's explore your favorite numbers:")

# Step 4: Check if the numbers are even or odd
even_odd_info = []
for num in numbers:
    if num % 2 == 0:
        even_odd_info.append((num, "even"))
    else:
        even_odd_info.append((num, "odd"))

# Step 5: Display even/odd information
for num, status in even_odd_info:
    print(f"The number {num} is {status}.")

# Step 6: Create and print tuples of numbers and their squares
print("\nHere are your numbers and their squares:")
for num in numbers:
    square_tuple = (num, num**2)
    print(f"The number {num} and its square: {square_tuple}")

# Step 7: Calculate the sum of the numbers
total_sum = sum(numbers)
print(f"\nThe sum of your favorite numbers is: {total_sum}")
