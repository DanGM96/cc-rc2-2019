print("\n******************************")
print("Bem vindo ao jogo de Adivinhação")
print("******************************\n")

secret_number = 42
guess_str = input("Digite o seu número: ")
guess = int(guess_str)

correct = guess == secret_number
bigger = guess > secret_number
smaller = guess < secret_number

if correct:
    print("Correto! A resposta pra vida, o universo e tudo mais!")
else:
    if bigger:
        print("O número certo é MENOR do que esse. Estou decepcionado com você.")
    elif smaller:
        print("O número certo é MAIOR do que esse. Estou decepcionado com você.")

print("\nEndgame.")