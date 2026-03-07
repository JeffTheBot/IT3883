# Program Name: Assignment3.py
# Course: IT3883/ Section W01
# Student Name: Jeff Camacho
# Assignment Number: Assignment 3
# Due Date: 03/06/2026
# Purpose: This program creates a GUI application that converts Miles per Gallon (MPG)
# into Kilometers per Liter (km/L). The result updates automatically as the
# user types into the input box.
# Resources Used:
# Class lecture slides, Python documentation, and professor example.

from tkinter import *

# Conversion constant
MPG_TO_KML = 0.425143707


# Function that runs whenever the user types in the box
def convert_mpg(event):
    try:
        mpg_value = float(mpg_entry.get())
        kml_value = mpg_value * MPG_TO_KML
        result_label.config(text=f"{kml_value} km/L") #initally had ":.4f" to round to four
    except:
        # Handles letters or blank input
        result_label.config(text="Enter a valid number")


# Create the main window
root = Tk()
root.title("MPG to km/L Converter")
root.geometry("300x150")

# MPG label
mpg_label = Label(root, text="Miles per Gallon (MPG):")
mpg_label.pack(pady=5)

# Entry box where user types MPG
mpg_entry = Entry(root)
mpg_entry.pack(pady=5)

# Bind typing event so conversion happens automatically
mpg_entry.bind("<KeyRelease>", convert_mpg)

# Result label
result_label = Label(root, text="km/L will appear here")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
