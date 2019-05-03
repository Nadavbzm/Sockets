# importing libraries
import socket

SEND_IP = "127.0.0.1"
PORT = 53

# Connecting to remote address
server_address = (SEND_IP, PORT)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

# Sending data to server
msg = "info" + "\n"

sock.sendall(msg.encode())

# Closing the socket
sock.close()
print("Message sent: " + msg)

