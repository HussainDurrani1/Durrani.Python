name = input("Enter your name: ")

numbers = []
for i in range(1, 4):
    num = int(input(f"Enter your {i} favorite number: "))
    numbers.append(num)

print(f"\nHello, {name.upper()}! Let's explore your favorite numbers:")

even_odd = []
for num in numbers:
    if num % 2 == 0:
        even_odd.append((num, "even"))
    else:
        even_odd.append((num, "odd"))

for num, status in even_odd:
    print(f"The number {num} is {status}.")

print("\nHere are your numbers and their squares:")
for num in numbers:
    square_tuple = (num, num**2)
    print(f"The number {num} and its square: {square_tuple}")

total_sum = sum(numbers)
print(f"\nThe sum of your favorite numbers is: {total_sum}")

is_prime = True
if total_sum <= 1:
    is_prime = False
else:
    for i in range(2, int(total_sum**0.5) + 1):
        if total_sum % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"The number {total_sum} is a composite number.")
