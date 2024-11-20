import threading
import socket

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET --> types of address your program can work with
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()

# connect to the server on local machine
server_binding = ("localhost", 9999)
cs.connect(server_binding)

data_from_server=cs.recv(1024)
print("[C]: Data received from server: " + message)    
cs.send(input("Response here: ").encode())

email = input("Enter your email: ")
cs.send(email.encode())

password = input("Enter your password: ")
cs.send(password.encode())

login_response = cs.recv(1024)
print("[C]: Login response from server: " + login_response.decode())

cs.close()
print("[C]: Connection closed")
