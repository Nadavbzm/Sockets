import socket

HOST = '127.0.0.1' # Host Address
PORT = 53  # Arbitrary Portng

# creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding socket to port and local host
s.bind((HOST, PORT))
print('Socket bind complete')

# listening on port 53
s.listen(10)

while True:
    # Accepting connections
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    msg = conn.recv(1024).decode() # buffer is 1024
    print(msg)
    
s.close()
