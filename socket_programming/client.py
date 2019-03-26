import socket

msg = str.encode(input("Msg to send to server: "))  # Converts string to bytes

HOST = '192.168.8.104'
PORT = 7777

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(msg)
    data = (s.recv(1024)).decode('utf-8')   # Converts bytes to string

print(f"received from server: {data}")
