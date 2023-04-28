import socket
import hashlib

SERVER_HOST = 'localhost' 
SERVER_HOST11 = '10.100.102.17'
SERVER_PORT = 65434  


PROXY_HOST = 'localhost'  
PROXY_HOST11 = '10.100.102.27'  
PROXY_PORT = 8081       

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.connect((SERVER_HOST, SERVER_PORT))
print("Connected to server.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_sock:
    proxy_sock.bind((PROXY_HOST, PROXY_PORT))
    proxy_sock.listen()
    print('Waiting for a proxy to connect...')
    
    while True:
        conn, addr = proxy_sock.accept()
        print('Connected by', addr)
        if (addr[0] == '127.0.0.1'): #change to the proxy adress '10.100.102.23'
            buffer = b''

            while True:
                data = conn.recv(4096)
                s_sock.sendall(data)
                if not data:
                    break
                    
                buffer += data

            # Print 
            md5_hash = hashlib.md5(buffer).hexdigest()
            print(f"MD5 hash of file: {md5_hash}")
            print('File forwarded to destination through the diode.')
