import socket
from os import system, name  # import only system from os
from time import sleep  # import sleep to show output for some time period
import game

MAX_BYTES = 65535
p_number = 3  # numero de players
p_name = []  # Guarda o player name
p_address = []  # Guarda o player address


# define clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def server(interface, port):
    clear()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('Listening at', sock.getsockname())

    i = 0
    while True:
        online_players()

        if p_number - i > 1:
            print('Aguardando mais jogadores...')
        elif p_number - i == 1:
            print('Aguardando um jogador...')
        else:
            print('O número de jogadores é inválido, configure seu jogo corretamente!')
            return

        data, client_address = sock.recvfrom(MAX_BYTES)
        login = data.decode('ascii')
        if login == '':
            login = 'P' + str(i + 1)
        text = ('> {} conectado com sucesso.\n'.format(login))
        sock.sendto(text.encode('ascii'), client_address)
        p_name.append(login)
        p_address.append(client_address)
        i += 1
        print(text)

        if i == p_number:
            sleep(1)
            clear()
            online_players()
            print('Sala completa.')
            break


def online_players():
    quant = len(p_name)
    print('Jogadores na sala ({}/{}):'.format(quant, p_number))
    for i in range(quant):
        print('\t{}\t{}'.format(p_name[i], p_address[i]))


if __name__ == '__main__':
    # Aqui, "" significa que o servidor está habilitado a receber
    # requisições de qualquer umas das interfaces locais
    server("", 1337)
