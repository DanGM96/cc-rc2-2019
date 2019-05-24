print("\n******************************")
print("Bem vindo ao jogo de Adivinhação")
print("******************************\n")

secret_number = 42
tries = 3           # Três tentativas

for run in range(tries):
    print("\nTentativa {} de {}".format(run + 1, tries))
    guess_str = input("Chute um numero entre 1 e 100:")
    guess = int(guess_str)

    correct = guess == secret_number
    bigger = guess > secret_number
    smaller = guess < secret_number

    if guess < 1 or guess > 100:
        print("Você deve digitar um número entre 1 e 100!")
        continue

    if correct:
        print("Correto! A resposta pra vida, o universo e tudo mais!")
        break
    else:
        if bigger:
            print("O número certo é MENOR do que esse. Estou decepcionado com você.")
        elif smaller:
            print("O número certo é MAIOR do que esse. Estou decepcionado com você.")

print("\nFim de jogo.")