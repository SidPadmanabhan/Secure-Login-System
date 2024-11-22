# Secure Login System

## Project Overview

This project implements a secure login system using **Python** and **SQLite** within a **client-server model**. It securely authenticates users by combining a database for credential storage, a multi-threaded server to handle client requests, and a client application for user interaction.

## Features

- **Database**: Securely stores user credentials in SQLite.
- **Server**: Handles client connections, validates credentials, and provides feedback.
- **Client**: Allows users to log in or register and displays authentication results.

## How to Run

### 1. Set Up the Database
- Create a SQLite database (`mydatabase.db`) with a `users` table.
- Insert sample user credentials for testing purposes.
- Verify the database is correctly populated with usernames and passwords.

### 2. Start the Server
- Run the server application to start listening for client connections.
- The server handles multiple connections using threading and validates credentials against the database.

### 3. Run the Client
- Start the client application to connect to the server.
- Enter login credentials when prompted.
- The server will return a success or failure message.

### Example Credentials
- Email: `john@gmail.com`
- Password: `johnny`

## Project Architecture

1. **Database**:
   - Stores user data in a `users` table.
   - Protects data integrity with unique constraints for email addresses.

2. **Server**:
   - Implements a multi-threaded socket server.
   - Communicates with the database to verify credentials.

3. **Client**:
   - Sends user input (email and password) to the server.
   - Receives and displays authentication results.

## Dependencies

- Python 3.x
- SQLite

## Objective

The project demonstrates:
- Secure login system implementation with a database.
- Client-server communication using sockets.
- Multi-threading to handle multiple client connections concurrently.
