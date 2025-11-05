import socket

# 1️⃣ Connect to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5001))
print("Connected to the server.")

# 2️⃣ Receive filename
filename = s.recv(1024).decode()
print("Receiving file:", filename)

# 3️⃣ Receive and save file data
with open("received_" + filename, 'wb') as f:
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

print("File received successfully as 'received_" + filename + "'")

# 4️⃣ Close socket
s.close()
