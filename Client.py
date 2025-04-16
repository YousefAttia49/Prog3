import socket

def client():
    client_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_server.connect(('localHost',12345))

    message='hello Server'
    client_server.sendall(message.encode())
    print(f'send {message}')
    data =client_server.recv(1024)
    print(f'Recieve {data.decode()}')
    
    client_server.close()
    print('clint is close')

if __name__=='__main__':
    client()    



