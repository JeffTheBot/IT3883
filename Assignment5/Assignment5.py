# Program Name: Assignment5.py
# Course: IT3883/Section W01
# Student Name: Jeff Camacho
# Assignment Number: Assignment 5
# Due Date: 04/22/2026
# Purpose: This program creates a SQLite database, creates a table for
# storing temperature readings, reads data from an input file, inserts
# the data into the database, and calculates the average temperature
# for Sunday and Thursday.
# Resources: Class notes, SQLite documentation, Python documentation,
# and instructor-provided assignment directions.

import sqlite3

# Connect to SQLite database (this will be created if it does not exist)
connection = sqlite3.connect("temperature_data.db")
cursor = connection.cursor()

# making the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS temperatures (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Day_Of_Week TEXT,
    Temperature_Value REAL
)
""")

# Clear old data so the program does not duplicate records if run again
cursor.execute("DELETE FROM temperatures")

# Open the input file and insert each line into the database
with open("Assignment5input.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            day = parts[0]
            temperature = float(parts[1])

            cursor.execute("""
            INSERT INTO temperatures (Day_Of_Week, Temperature_Value)
            VALUES (?, ?)
            """, (day, temperature))

# Save inserted records
connection.commit()

# Compute average temperature for Sunday
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM temperatures
WHERE Day_Of_Week = 'Sunday'
""")
sunday_avg = cursor.fetchone()[0]

# Compute average temperature for Thursday
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM temperatures
WHERE Day_Of_Week = 'Thursday'
""")
thursday_avg = cursor.fetchone()[0]

# Print results to the console
print(f"Average temperature for Sunday: {sunday_avg:.2f}")
print(f"Average temperature for Thursday: {thursday_avg:.2f}")

# Close the database connection
connection.close()

