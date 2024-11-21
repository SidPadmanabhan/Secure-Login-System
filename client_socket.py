import socket

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print(f"Socket open error: {err}")
    exit()

server_binding = ("localhost", 9999)
cs.connect(server_binding)

email = input("Enter your email: ")
cs.send(email.encode())

password = input("Enter your password: ")
cs.send(password.encode())


login_response = cs.recv(1024).decode()
print(login_response)


cs.close()
print("[C]: Connection closed")
