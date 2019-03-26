import socket

s = socket.socket()

HOST = '192.168.8.104'
PORT = 7777

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by: {addr}")
        while(True):
            data = conn.recv(1024)
            if not(data):
                break
            if (data.decode('utf-8').isdigit()):
                number = int(data.decode('utf-8'))
                number *= 2
                data = str.encode(str(number))
            conn.sendall(data)
