# Program Name: Assignment1.py
# Course: IT3883 / Section W01
# Student Name: Jeff Camacho
# Assignment Number: Lab 1
# Due Date: 01/24/2026
# Purpose:
# This program provides a text-based menu that allows the user to
# store text in a buffer, clear it, display it, or exit the program.
# Resources Used:
# Python documentation (https://docs.python.org/3/)

# Initialize the input buffer to store user text
input_buffer = ""

# Keep displaying the menu until the user chooses to exit
while True:
    # Display menu options
    print("\n--- Text Buffer Menu ---")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    # Prompt the user to select a menu option
    choice = input("Enter your choice (1-4): ")

    # Option 1: Append user-entered text to the buffer
    if choice == "1":
        user_text = input("Enter text to append: ")
        input_buffer += user_text
        print("Text appended successfully.")

    # Option 2: Clear all data stored in the buffer
    elif choice == "2":
        input_buffer = ""
        print("Input buffer has been cleared.")

    # Option 3: Display the current contents of the buffer
    elif choice == "3":
        if input_buffer == "":
            print("The input buffer is currently empty.")
        else:
            print("Current input buffer contents:")
            print(input_buffer)

    # Option 4: Exit the program
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    # Handle invalid menu selections
    else:
        print("Invalid choice. Please select a number between 1 and 4.")


