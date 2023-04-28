import socket
import hashlib

#diode network info
DIODE_HOST = '127.0.0.1'   
DIODE_HOST1 = '10.100.102.27'  
DIODE_PORT = 8081       

#proxy network info
PROXY_HOST = '127.0.0.1' 
PROXY_HOST1 = '10.100.102.23' 
PROXY_PORT = 65432       

# Connect to diode on TCP
diode_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
diode_sock.connect((DIODE_HOST, DIODE_PORT))
print("Connected to diode.")

# Listening socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_sock:
    proxy_sock.bind((PROXY_HOST, PROXY_PORT))
    proxy_sock.listen()
    print('Waiting for a client to connect...')
    while True:
        conn, addr = proxy_sock.accept()
        print('Connected by', addr)

        # Create a buffer
        buffer = b''

        # Loop till all received
        while True:
            data = conn.recv(4096)
            diode_sock.sendall(data)
            if not data:
                break

            buffer += data

        #Print
        md5_hash = hashlib.md5(buffer).hexdigest()
        print(f"MD5 hash of file: {md5_hash}")
        print('File transfer completed!')
