import socket

MAX_BYTES = 65535


def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Saindo do modo promíscuo e aceitando respostas
    # apenas do servidor hostname
    sock.connect((hostname, port))
    print('Client socket name is {}'.format(sock.getsockname()))

   # text = input("login: ")
    sock.sendto('A1'.encode('ascii'), (hostname, port))
    print('Tentando entrar na sala do jogo...')
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if not data:
            break
        print(data.decode('ascii'))

    print('The server says {!r}'.format(data.decode('ascii')))


if __name__ == '__main__':
    client('192.168.1.8', 1337)
