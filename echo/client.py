import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))  




while True:
    client_msg = input("You: ")
    s.send(client_msg.encode())
    server_msg = s.recv(1024).decode()
    print("echoed from server:", server_msg)


    if client_msg.lower() == "bye":
        print("You terminated the chat.")
        s.close()
        break