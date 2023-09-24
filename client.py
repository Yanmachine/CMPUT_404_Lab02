import socket

BYTES_TO_READ = 4096
FORMAT = 'utf-8'
PORT = 8080
HOST = "localhost"

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: " + host.encode(FORMAT) + b"\n\n"
    #creates client socket using IPv4 and TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send(request)
    client.shutdown(socket.SHUT_WR)
    result = client.recv(BYTES_TO_READ)
    while(len(result) > 0):
        print(result)
        result = client.recv(BYTES_TO_READ)

    client.close()

#get("www.google.com", 80)
get(HOST, PORT)