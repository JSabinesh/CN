
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))


while True:
   
    msg = input("You: ")
    s.send(msg.encode())

    reply = s.recv(1024).decode()
    print("Server:", reply)


    if reply.lower() == "bye":
        print("Server ended the chat.")
        s.close()
        break