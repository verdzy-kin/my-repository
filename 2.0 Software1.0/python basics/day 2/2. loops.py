# # import random

# # target = random.randint(1, 10)
# # guess = 0
# # attempts = 0

# # print("I'm thinking of a number between 1 and 10...")
# # while guess != target and attempts < 3:
# #     guess = int(input("Please enter your guess: ")) # Simulating user guess
# #     attempts += 1

# #     if guess == target:
# #         print(f"Correct! The number was {target}")
# #         print(f"It took {attempts} attempts")
# #     elif guess < target:
# #         print(f"Guess {guess} is too low")
# #     else:
# #         print(f"Guess {guess} is too high")

# # if guess != target:
# #     print(f"Sorry! The number was {target}")


# # Password validator
# # def validate_password(password):
# #     has_upper = False
# #     has_lower = False
# #     has_digit = False

# #     for char in password:
# #         if char.isupper():
# #             has_upper = True
# #         elif char.islower():
# #             has_lower = True
# #         elif char.isdigit():
# #             has_digit = True

# #     return has_upper and has_lower and has_digit and len(password) >= 8

# # # Test passwords
# # passwords = ["Password123", "password", "PASSWORD", "Pass123"]
# # for pwd in passwords:
# #     if validate_password(pwd):
# #         print(f"'{pwd}' is a strong password ✓")
# #     else:
# #         print(f"'{pwd}' is a weak password ✗")

# password=input("Please enter your password: ")
# has_lower=False
# has_upper=False
# has_digits=False
# # check if password is weak or strong:
# # strong password should contain caps, lower and digits
# # islower(), isupper(), isdigit()
# for pwd in password:
#     if pwd.isupper():
#         has_upper=True
#     elif pwd.islower():
#         has_lower=True
#     elif pwd.isdigit():
#         has_digits=True
# if has_digits and has_lower and has_upper:
#     print(f"It was indeed a strong password: {password}")
# else:
#     print("That password was very weak")

    


# Multiplication table
# print("Multiplication Table:")
# for i in range(1, 12):  # Rows
#     print("__"*45)

#     for j in range(1, 12):  # Columns
#         result = i * j
#         print(f"{i} x {j} = {result}")
#     print()  # Empty line after each row

# age = 25
# has_license = True
# has_insurance = True

# # AND operator (all conditions must be True)
# if age >= 18 and has_license and not has_insurance:
#     print("You can drive!")
# else:
#     print("Cannot drive.....")


# OR operator (at least one condition must be True)
# is_weekend = False
# is_holiday = True

# if is_weekend or is_holiday:
#     print("No work today!")


# is_raining = False
# if not is_raining:
#     print("Let's go for a walk!")



#for loop
#starting point
#condition
#increment or decrement
#database of people

names=["Hubert", "Kate", "Leo mbom", "Killian"]
# print(names[0])
# print(names[1])
# print(names[2])

count = 1
for name in names:    
    print(f"{count}. {name}")
    count += 1

#range function
# range(stop) - starts from 0
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Countdown
for i in range(10, 0, -1):
    print(f"Countdown: {i}")
print("Blast off! 🚀")


# Basic while loop
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Same as count = count + 1

# User input loop
user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to exit: ")
    if user_input != "quit":
        print(f"You entered: {user_input}")

print("Goodbye!")

# Break - exit the loop completely
print("Finding the first even number:")
for number in range(1, 10):
    if number % 2 == 0:
        print(f"Found even number: {number}")
        break
    print(f"{number} is odd")

# Continue - skip to next iteration
print("\nPrinting only odd numbers:")
for number in range(1, 10):
    if number % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {number}")

# Number guessing game simulation
import random

target = random.randint(1, 10)
guess = 0
attempts = 0

print("I'm thinking of a number between 1 and 10...")
while guess != target and attempts < 3:
    guess = random.randint(1, 10)  # Simulating user guess
    attempts += 1

    if guess == target:
        print(f"Correct! The number was {target}")
        print(f"It took {attempts} attempts")
    elif guess < target:
        print(f"Guess {guess} is too low")
    else:
        print(f"Guess {guess} is too high")

if guess != target:
    print(f"Sorry! The number was {target}")

# Enumerate - get both index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Zip - loop through multiple lists together
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# List comprehension - create lists with loops
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

print("Triangle pattern]")
for row in range(1,6):
    for star in range(row):
        print("*", end="")
    print()
