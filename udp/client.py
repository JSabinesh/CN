from datetime import datetime
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 9999)

while True:
    msg = input("You: ")
    sn = time.time()
    s.sendto(msg.encode(), server_address)

    if msg.lower() == "bye":
        print("You ended the chat.")
        break

    data, _ = s.recvfrom(1024)
    en = time.time()
    print("Round-trip time:", en - sn)
    print("Server:", data.decode())

s.close()