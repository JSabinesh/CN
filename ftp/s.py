import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 5001))
s.listen(1)

print("Server is waiting for connection...")

conn, addr = s.accept()
print("Connected to", addr)

# 3️⃣ Ask for file to send
filename = input("Enter the filename to send: ")

# 4️⃣ Send filename
conn.send(filename.encode())

# 5️⃣ Send file data
with open(filename, 'rb') as f:
    data = f.read(1024)
    while data:
        conn.send(data)
        data = f.read(1024)

print("File sent successfully.")

# 6️⃣ Close connections
conn.close()
s.close()
