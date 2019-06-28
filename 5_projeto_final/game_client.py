import socket

MAX_BYTES = 65535


def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Saindo do modo promíscuo e aceitando respostas
    # apenas do servidor hostname
    sock.connect((hostname, port))
    print('Client socket name is {}'.format(sock.getsockname()))

   # text = input("login: ")
    sock.sendto(''.encode('ascii'), (hostname, port))
    print('Tentando entrar na sala do jogo...')
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if not data:
            break
        text = data.decode('utf-8')
        print(text)

        if text == '\nDefina o nível de dificuldade\n(1)Fácil\t(2)Médio\t(3)Difícil':
            text = input('')
            sock.sendto(text.encode('utf-8'), (hostname, port))


if __name__ == '__main__':
    client('192.168.52.6', 1337)
