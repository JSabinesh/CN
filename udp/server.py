
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 9999))  


while True:

    data, addr = s.recvfrom(1024)
    msg = data.decode()
    print("Client:", msg)

    
    if msg.lower() == "bye":
        print("Client ended the chat.")
        break

    reply = input("You: ")
    s.sendto(reply.encode(), addr)

# 5️⃣ Close the socket
s.close()