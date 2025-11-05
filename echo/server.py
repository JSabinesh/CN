import socket
import datetime


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9999)) 
s.listen(1)  # allow one client
print("Server waiting for connection...")

conn, addr = s.accept()

while True:
    
    client_msg = conn.recv(1024).decode().lower()
    now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print("Client:", client_msg)

    conn.send(client_msg.encode())
    

    #date time
    conn.send(now.encode())
    
    if client_msg.lower() == "bye":
        print("Server terminated the chat.")
        conn.close()
        break