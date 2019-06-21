import socket
import game

MAX_BYTES = 65535
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
p_number = 3  # Numero máximo de players, apenas números positivos!
p_name = []  # Guarda o player name
p_address = []  # Guarda o player address


def server(interface, port):
    sock.bind((interface, port))
    print('\n\nListening at', sock.getsockname())

    i = 0
    while True:
        i += 1
        online_players()

        if i > p_number:
            break

        data, client_address = sock.recvfrom(MAX_BYTES)
        login = data.decode('ascii')
        if login == '':
            login = 'P' + str(i)
        text = ('> {} conectado com sucesso.'.format(login))
        sock.sendto(text.encode('ascii'), client_address)
        p_name.append(login)
        p_address.append(client_address)
        print(text)

    game.play()


def online_players():
    p_online = len(p_name)
    p_head = '\nJogadores na sala ({}/{}):'.format(p_online, p_number)
    print(p_head)

    for i in range(p_online):
        sock.sendto(p_head.encode('ascii'), p_address[i])  # Envia o head com 'info' sobre quantidade de players

    for i in range(p_online):
        p_body = '\t{}\t{}'.format(p_name[i], p_address[i])
        print(p_body)
        for j in range(p_online):
            sock.sendto(p_body.encode('ascii'), p_address[j])  # Envia o 'body' com info sobre nome e address de players

    if p_number - p_online > 1:
        waiter = 'Aguardando mais jogadores...'
    elif p_number - p_online == 1:
        waiter = 'Aguardando um jogador...'
    else:
        waiter = 'Sala completa.'

    print(waiter)

    for i in range(p_online):
        sock.sendto(waiter.encode('ascii'), p_address[i])  # Envia o 'waiter' com mensagem sobre aguardo


if __name__ == '__main__':
    # Aqui, "" significa que o servidor está habilitado a receber
    # requisições de qualquer umas das interfaces locais
    server("", 1337)
