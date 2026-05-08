# Program Name: Sprint1_Implementation.py
# Course: IT3883/Section W01
# Student Name: Jeff Camacho
# Assignment Number: Final Exam Sprint 1
# Due Date: 05/07/2026
# Purpose: This program reads a pseudo-English sentence that describes coins
# and converts the coin amounts into a dollar total.
# List Specific resources used to complete the assignment: Course notes and class examples.

# Dictionary that stores each coin name and its value in dollars.
coin_values = {
    "penny": 0.01,
    "pennies": 0.01,
    "nickel": 0.05,
    "nickels": 0.05,
    "dime": 0.10,
    "dimes": 0.10,
    "quarter": 0.25,
    "quarters": 0.25
}


# Ask the user to enter a coin sentence.
coin_sentence = input("Enter coin sentence: ")

# Split the sentence into separate words.
words = coin_sentence.lower().split()

# Keep track of the total dollar amount.
total = 0.0

# Go through each word and look for a number followed by a coin name.
for index in range(len(words) - 1):
    if words[index].isdigit():
        quantity = int(words[index])
        coin_name = words[index + 1]

        if coin_name in coin_values:
            total += quantity * coin_values[coin_name]

# Display the final dollar amount with two decimal places.
print(f"Total dollar amount: {total:.2f}")

