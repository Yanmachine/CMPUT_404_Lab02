import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "localhost"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data)
            extra_message = b"Server: Data received and echoed successfully\n"
            conn.sendall(extra_message)

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.listen()
        conn, addr = server.accept()
        handle_connection(conn, addr)

def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.listen(5)
        while True:
            conn, addr = server.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()


start_threaded_server()