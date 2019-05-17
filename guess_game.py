print("\n******************************")
print("Bem vindo ao jogo de Adivinhação")
print("******************************\n")

secret_number = 42

guess = input("Digite o seu número: ")
print("n = ", guess)

if secret_number == int(guess):
    print("A resposta pra vida, o universo e tudo mais!")
else:
    print("Estou decepcionado com sua resposta.")


