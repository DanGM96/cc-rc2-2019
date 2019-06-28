import socket
import random

MAX_BYTES = 65535
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
p_number = 3  # Numero máximo de players, apenas números positivos!
p_conectados = {}


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
        login = data.decode('utf-8')
        if login == '':
            login = 'P' + str(i)
        text = ('> {} conectado com sucesso.'.format(login))
        sock.sendto(text.encode('utf-8'), client_address)
        p_conectados.update({login: client_address})
        print(text)

    game()


def game():
    secret_number = random.randrange(1, 100)
    points = 1000

    while True:
        print("\nConfigurando o jogo...")
        text = '\nDefina o nível de dificuldade\n(1)Fácil\t(2)Médio\t(3)Difícil'
        sock.sendto(text.encode('utf-8'), list(p_conectados.values())[0])
        data, list(p_conectados.values())[0] = sock.recvfrom(MAX_BYTES)
        level = data.decode('utf-8')

        if level == '1':
            tries = 8 * p_number
            dificuldade = 'Fácil'
            break
        elif level == '2':
            tries = 4 * p_number
            dificuldade = 'Médio'
            break
        elif level == '3':
            tries = 2 * p_number
            dificuldade = 'Difícil'
            break
        else:
            continue

    p_head = ('\nNível de dificuldade selecionado: {}\nVocês terão {} tentativas!').format(dificuldade, tries)
    p_body = ('\n********************************\nBem vindo ao jogo da Adivinhação\n********************************\n')
    for key, val in p_conectados.items():
        sock.sendto(p_head.encode('utf-8'), val)
        sock.sendto(p_body.encode('utf-8'), val)

    for run in range(tries):
        print("\nTentativa {} de {}".format(run + 1, tries))
        guess_str = input("Chute um numero entre 1 e 100: ")
        guess = int(guess_str)

        correct = guess == secret_number
        bigger = guess > secret_number
        smaller = guess < secret_number

        if guess < 1 or guess > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if correct:
            print("Parabéns! Você venceu.")
            break
        else:
            if bigger:
                print("Tente um número MENOR.")
            elif smaller:
                print("Tente um número MAIOR.")

            points -= abs(secret_number - guess)

    print(f"\nPontuação: {points}")
    print("\nFim de jogo.")
    print("Número secreto: ", secret_number)
    '''
    print("\n********************************")
    print("Bem vindo ao jogo da Adivinhação")
    print("********************************\n")

    secret_number = random.randrange(1, 100)
    points = 1000
    tries = 0  # Três tentativas

    while 1:
        print("Defina o nível de dificuldade")
        level = int(input("(1)Fácil (2)Médio (3)Difícil\n"))

        if level == 1:
            tries = 20
            break
        elif level == 2:
            tries = 10
            break
        elif level == 3:
            tries = 5
            break
        else:
            continue

    for run in range(tries):
        print("\nTentativa {} de {}".format(run + 1, tries))
        guess_str = input("Chute um numero entre 1 e 100: ")
        guess = int(guess_str)

        correct = guess == secret_number
        bigger = guess > secret_number
        smaller = guess < secret_number

        if guess < 1 or guess > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        if correct:
            print("Parabéns! Você venceu.")
            break
        else:
            if bigger:
                print("Tente um número MENOR.")
            elif smaller:
                print("Tente um número MAIOR.")

            points -= abs(secret_number - guess)

    print(f"\nPontuação: {points}")
    print("\nFim de jogo.")
    print("Número secreto: ", secret_number)'''


def online_players():
    p_head = '\nJogadores na sala ({}/{}):'.format(len(p_conectados), p_number)
    print(p_head)

    for key, val in p_conectados.items():
        sock.sendto(p_head.encode('utf-8'), val)  # Envia o head com 'info' sobre quantidade de players

    for key, val in p_conectados.items():
        p_body = '\t{}\t{}'.format(key, val)
        print(p_body)
        for order2 in p_conectados.values():
            sock.sendto(p_body.encode('utf-8'),
                        order2)  # Envia o 'body' com info sobre nome e address de players

    if p_number - len(p_conectados) > 1:
        waiter = 'Aguardando mais jogadores...'
    elif p_number - len(p_conectados) == 1:
        waiter = 'Aguardando um jogador...'
    else:
        waiter = 'Sala completa.'

    print(waiter)

    for key, val in p_conectados.items():
        sock.sendto(waiter.encode('utf-8'), val)  # Envia o 'waiter' com mensagem sobre aguardo


if __name__ == '__main__':
    # Aqui, "" significa que o servidor está habilitado a receber
    # requisições de qualquer umas das interfaces locais
    server("", 1337)
