# <u>Python Code Explanation</u>

#### Step-by-step explanation of the code:


## Step 1: Getting User's Name:
The user is prompted to enter their name, and this input is stored in the variable name.
```
name = input("Enter your name: ")
```
## Step 2: Collecting Favorite Numbers:

- An empty list numbers is created.
- A loop runs three times (from 1 to 3) to collect three favorite numbers from the user.
* Each number entered by the user is converted to an integer and appended to the numbers list.
```
numbers = []
for i in range(1, 4):
    num = int(input(f"Enter your {i} favorite number: "))
    numbers.append(num)
```

## Step 3: Greeting the User:
The user's name is printed in uppercase, along with a greeting message.
```
print(f"\nHello, {name.upper()}! Let's explore your favorite numbers:")
```
## Step 4: Checking Even or Odd:
- A new empty list even_odd is created to store tuples containing each number and whether it is even or odd.
- The loop iterates over the numbers list.
* For each number, it checks if the number is even (if divisible by 2) or odd.
* A tuple with the number and its status ("even" or "odd") is appended to even_odd.
```
even_odd = []
for num in numbers:
    if num % 2 == 0:
        even_odd.append((num, "even"))
    else:
        even_odd.append((num, "odd"))
```
* Each number and its "even/odd" status is printed.
```
for num, status in even_odd:
    print(f"The number {num} is {status}.")
```

## Step 5: Displaying Numbers & Their Squares:
* The script prints a message introducing the square of the numbers.
* A loop iterates over the numbers list.
* For each number, a tuple is created containing the number and its square (num**2).
* The number and its square are printed in the format (num, square).
```
print("\nHere are your numbers and their squares:")
for num in numbers:
    square_tuple = (num, num**2)
    print(f"The number {num} and its square: {square_tuple}")
```
## Step 6: Calculating the Sum:
* The sum of all numbers in the numbers list is calculated using the sum() function and stored in total_sum.
* The sum is then printed.
```
total_sum = sum(numbers)
print(f"\nThe sum of your favorite numbers is: {total_sum}")
```
## Step 7: Checking if Sum is Prime:
* A boolean variable is_prime is initialized as True.
* The script checks if the total sum is prime:
   - If total_sum is less than or equal to 1, it is not prime (is_prime = False).
   - Otherwise, the script checks divisibility from 2 up to the square root of the sum.
   - If any divisor is found, the sum is not prime (is_prime = False) and the loop is exited.
```
   if is_prime:
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"The number {total_sum} is a composite number.")
```
* Finally, based on whether is_prime is True or False, the script prints whether the sum is a prime number or composite.

# Output
```
Enter your name: HUSSain
Enter your 1 favorite number: 4
Enter your 2 favorite number: 6
Enter your 3 favorite number: 9

Hello, HUSSAIN! Let's explore your favorite numbers:
The number 4 is even.
The number 6 is even.
The number 9 is odd.

Here are your numbers and their squares:
The number 4 and its square: (4, 16)
The number 6 and its square: (6, 36)
The number 9 and its square: (9, 81)

The sum of your favorite numbers is: 19
Wow, 19 is a prime number!
```