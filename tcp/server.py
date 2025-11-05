
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9999)) 
s.listen(1) 


conn, addr = s.accept()


while True:
    
    client_msg = conn.recv(1024).decode()
    print("Client:", client_msg)

    
    msg = input("You: ")
    conn.send(msg.encode())

  
    if msg.lower() == "bye":
        print("Server terminated the chat.")
        conn.close()
        break