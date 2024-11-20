import threading # two things happening at once
import sqlite3
import hashlib
import socket # used to establish the connection between client and server

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet socket, connection oriented protocol (TCP)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ("localhost", 9999)
ss.bind(server_binding)
ss.listen()


def verify(email, password):
    try: 
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? and password = ?", (email, password))
        user = cursor.fetchone()
        conn.close()
        return user is not None
    except Exception as e:
        print(f"[S]: Database error: {e}")
        return False

def start_connection(client_socket): # taking client as parameter
    msg = "Welcome to Blueprint! Log in"
    client_socket.send(msg.encode())

    #receive email and password
    client_socket.send("Enter your email:".encode())
    email = client_socket.recv(1024).decode()

    client_socket.send("Enter your password:".encode())
    password = client_socket.recv(1024).decode()

    if verify(email, password):
        client_socket.send("Login Successful".encode())
    else:
        client_socket.send("Invalid Login".encode())

    client_socket.close()
    
while True:
    try: 
        client_socket, client_address = ss.accept()
        print(f"[S]: Connection established with {client address})")

    client_thread = threading.Thread(target=start_connection, args = (client_socket,))
    client_thread.start()
