import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxyClient:
        proxyClient.connect((host, port))
        proxyClient.send(request)
        proxyClient.shutdown(socket.SHUT_WR)
        chunk = proxyClient.recv(BYTES_TO_READ)
        result = b'' + chunk

        while(len(chunk)>0):
            chunk = proxyClient.recv(BYTES_TO_READ)
            result += chunk
        proxyClient.close()
        return result
    
print(get("localhost", 8080))