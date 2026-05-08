# Program Name: Sprint2_Corrected_Implementation.py
# Course: IT3883/Section W01
# Student Name: Jeff Camacho
# Assignment Number: Final Exam Sprint 2
# Due Date: 05/07/2026
# Purpose: This corrected program reads pseudo-English coin sentences,
# validates the input, calculates the value of the coins, and displays the
# total amount in dollars.
# List Specific resources used to complete the assignment: Course notes and class examples.


def calculate_coin_total(coin_sentence):
    """Convert a pseudo-English coin sentence into a dollar amount."""

    coin_values = {
        "penny": 1,
        "pennies": 1,
        "nickel": 5,
        "nickels": 5,
        "dime": 10,
        "dimes": 10,
        "quarter": 25,
        "quarters": 25
    }

    words = coin_sentence.lower().split()
    total_cents = 0
    valid_pair_found = False

    # Look through the sentence for number and coin word pairs.
    for index in range(len(words) - 1):
        current_word = words[index]
        next_word = words[index + 1]

        if current_word.isdigit():
            quantity = int(current_word)

            if next_word in coin_values:
                total_cents += quantity * coin_values[next_word]
                valid_pair_found = True
            else:
                raise ValueError("A number must be followed by a valid coin denomination.")

    if not valid_pair_found:
        raise ValueError("No valid coin amounts were found.")

    return total_cents / 100


def main():
    """Run the coin conversion program."""

    coin_sentence = input("Enter coin sentence: ")

    try:
        total = calculate_coin_total(coin_sentence)
        print(f"Total dollar amount: {total:.2f}")
    except ValueError as error:
        print("Input error:", error)


if __name__ == "__main__":
    main()
