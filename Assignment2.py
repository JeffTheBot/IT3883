# Program Name: Assignment2.py
# Course: IT3883 / Section W01
# Student Name: Jeff Camacho
# Assignment Number: Assignment 2
# Due Date: 02/18/2026
# Purpose: This program reads student scores from a file,
# calculates each student’s average grade, and prints
# the results in descending order by average.
# Resources Used: Class notes, Python documentation

# This will open the input file aka the text file for reading
file = open("Assignment2input.txt", "r")

# This creates an empty list to store student data
student_averages = []

# Loop through each line in the file
for line in file:

    # Remove newline characters and split by space
    parts = line.strip().split()

    # First item is student name
    name = parts[0]

    # Remaining items are scores
    scores = parts[1:]

    # Convert scores from string to integer
    total = 0
    for score in scores:
        total += int(score)

    # Calculate average
    average = total / len(scores)

    # Store as tuple (name, average)
    student_averages.append((name, average))

# Close the file
file.close()

# Sort list in descending order by average; [1] = average 
def get_average(student_tuple): return student_tuple[1]
student_averages.sort(key=get_average, reverse=True)

# Print results formatted to 2 decimal places; .2f helps the outcome produce 2 decimal places
for student in student_averages:
    print(student[0], format(student[1], ".2f"))
