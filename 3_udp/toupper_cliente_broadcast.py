import socket

BUFSIZE = 65535


def client(network, port):
    # Criando o socket para Internet e UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Configurando a opção de broadcast para este socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    text = 'Broadcast datagram!'
    sock.sendto(text.encode('ascii'), (network, port))

    text = input("Envie uma mensagem para o servidor: ")
    sock.sendto(text.encode('ascii'), (network, port))
    while True:
        data, address = sock.recvfrom(BUFSIZE)
        if not data:
            break;
        print(data.decode('ascii'))


if __name__ == '__main__':
    client('192.168.52.255', 1060)
