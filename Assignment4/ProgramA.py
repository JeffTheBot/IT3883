# Program Name: ProgramA.py
# Course: IT3883/Section W01
# Student Name: Jeff Camacho
# Assignment Number: Assignment 4
# Due Date: 04/01/2026
# Purpose: This program asks the user to enter a string, sends that string
# to Program B using a socket connection, waits for a response, and then
# prints the response that it receives back from Program B.
# List Specific resources used to complete the assignment:
# Class notes, instructor directions, and personal coding practice.

import socket

# Hard-coded IP address and port number; since I am running on the same computer
# just put loopback address or local host, use available port

SERVER_IP = "localhost"
SERVER_PORT = 45000

# Ask the user to type a message
message_to_send = input("Enter a string to send to Program B: ")

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to Program B
    client_socket.connect((SERVER_IP, SERVER_PORT))

    # Send the user's message to Program B
    client_socket.send(message_to_send.encode())

    # Wait for the response from Program B
    returned_message = client_socket.recv(1024).decode()

    # Print what was received
    print("Received from Program B:", returned_message)

except ConnectionRefusedError:
    print("Could not connect to Program B. Make sure Program B is running first.")

finally:
    # Close the socket
    client_socket.close()