import guess_game
import hangman_game

def choose_game():
    print("\n****************")
    print("Escolha seu jogo")
    print("****************\n")

    while 1:
        game = int(input("(1)Forca (2)Adivinhação\n"))

        if game == 1:
            print("Iniciando jogo da Forca...\n")
            hangman_game.play()
            break
        elif game == 2:
            print("Iniciando jogo da Adivinhação...\n")
            guess_game.play()
            break
        else:
            continue


if __name__ == "__main__":
    choose_game()
