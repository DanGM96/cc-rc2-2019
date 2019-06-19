import random


def play():

    print("\n********************************")
    print("Bem vindo ao jogo da Adivinhação")
    print("********************************\n")

    secret_number = random.randrange(1, 100)
    points = 1000
    tries = 0          # Três tentativas

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
    print("Número secreto: ", secret_number)


if __name__ == "__main__":
    play()
