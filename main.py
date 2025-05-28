from game.game import TicTacToe

def main():
    while True:
        game = TicTacToe()
        game.play()
        if not game.play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()