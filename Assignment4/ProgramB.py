# Program Name: ProgramB.py
# Course: IT3883/Section W01
# Student Name: Jeff Camacho
# Assignment Number: Assignment 4
# Due Date: 04/01/2026
# Purpose: This program waits for a connection from Program A, receives
# a string, converts the string to uppercase, prints the uppercase string,
# and sends the uppercase version back to Program A.
# List Specific resources used to complete the assignment:
# Class notes, instructor directions, and personal coding practice.

import socket

# Hard-coded IP address and port number; since I am running on the same computer
# just put loopback address or local host, use available port

SERVER_IP = "localhost"
SERVER_PORT = 45000

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port number
server_socket.bind((SERVER_IP, SERVER_PORT))

# Listen for one incoming connection
server_socket.listen(1)

print("Program B is waiting for a connection...")

# Accept a connection from Program A
connection_socket, client_address = server_socket.accept()

try:
    print("Connected to:", client_address)

    # Receive data from Program A
    received_message = connection_socket.recv(1024).decode()

    # Convert the message to uppercase
    uppercase_message = received_message.upper()

    # Print the uppercase message in Program B
    print("Uppercase message:", uppercase_message)

    # Send the uppercase message back to Program A
    connection_socket.send(uppercase_message.encode())

finally:
    # Close the connection socket and server socket
    connection_socket.close()
    server_socket.close()