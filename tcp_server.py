import socket

HOST = '0.0.0.0'
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"[TCP SERVER] Listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"[TCP SERVER] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"[TCP SERVER] Received: {data.decode()}")
                conn.sendall(data)
