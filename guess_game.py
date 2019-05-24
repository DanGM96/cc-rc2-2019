import random

print("\n******************************")
print("Bem vindo ao jogo de Adivinhação")
print("******************************\n")

secret_number = random.randrange(1, 100)
tries = 3           # Três tentativas

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

print("\nFim de jogo.")