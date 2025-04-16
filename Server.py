import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localHost", 12345))
    server_socket.listen(5)

    print("server is listing 1234.........")
    conn, addr = server_socket.accept()
    print("connection from {addr}")

    while True:
        data=conn.recv(1024)
        if not data:
            break
        print(f'Revieve {data.decode()}')
        conn.sendall(data)

    conn.close()
    server_socket.close()
    print('server is close')

if __name__=='__main__':
    server()        
