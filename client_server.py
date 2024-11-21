import threading
import sqlite3
import socket

# Create the server socket
try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reuse the address to avoid errors
    print("[S]: Server socket created")
except socket.error as err:
    print(f"Socket open error: {err}")
    exit()

server_binding = ("localhost", 9999)
ss.bind(server_binding)
ss.listen()
print("[S]: Server is listening on port 9999")


# Function to verify email and password in the database
def verify(email, password):
    try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and user[0] == password:
            return True
        return False
    except Exception as e:
        print(f"[S]: Database error: {e}")
        return False



def start_connection(client_socket):
    try:
       
        email = client_socket.recv(1024).decode().strip()
        print(f"[S]: Received email: {email}")

        
        password = client_socket.recv(1024).decode().strip()
        print(f"[S]: Received password: {password}")


        if verify(email, password):
            client_socket.send("Login Successful".encode())
        else:
            client_socket.send("Invalid Login".encode())
    
    finally:
        client_socket.close()
        print("[S]: Connection closed")


# Main server loop
try:
    while True:
        client_socket, client_address = ss.accept()
        print(f"[S]: Connection established with {client_address}")

        client_thread = threading.Thread(target=start_connection, args=(client_socket,))
        client_thread.start()

finally:
    ss.close()
    print("[S]: Server socket closed")
