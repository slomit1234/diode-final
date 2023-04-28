import socket
import hashlib
from tqdm import tqdm

SERVER_HOST1 = '10.100.102.17'  
SERVER_PORT = 65434      
SERVER_HOST = '127.0.0.1'  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_sock:
    s_sock.bind((SERVER_HOST, SERVER_PORT))
    s_sock.listen()
    print('Waiting for a diode to connect...')
    
    while True:
       print("****")
       conn, addr = s_sock.accept()
       #print (type(addr))
       print (addr)
       print('Connected by', addr)
       if (addr[0] == '127.0.0.1'): #the diode address '10.100.102.27'
           buffer = b''
           file_size = 10 * 1024 * 1024
           progress = tqdm(total=file_size, unit='B', unit_scale=True)
           while True:
               data = conn.recv(4096)
               if not data:
                   break
               buffer += data
               progress.update(len(data))
                
                
           with open('received_file', 'wb') as f:
               f.write(buffer)
          # Print
           md5_hash = hashlib.md5(buffer).hexdigest()
           print(f"MD5 hash of file: {md5_hash}")
           print('File forwarded to destination through the diode.')
           
    
