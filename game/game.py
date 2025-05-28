from .board import Board
from .player import Player

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_player = None
        
    def setup_players(self):
        """Setup players with names and symbols"""
        player1_name = input("Enter Player 1 name: ")
        player2_name = input("Enter Player 2 name: ")
        
        self.players = [
            Player(player1_name, "X"),
            Player(player2_name, "O")
        ]
        self.current_player = self.players[0]
        
    def switch_player(self):
        """Switch to the other player"""
        self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
        
    def play(self):
        """Main game loop"""
        print("\nWelcome to Tic-Tac-Toe!\n")
        self.setup_players()
        self.board.display()
        
        while True:
            move = self.current_player.get_move()
            
            if not self.board.update(move, self.current_player.symbol):
                print("Invalid move! Try again.")
                continue
                
            self.board.display()
            
            if self.board.check_winner(self.current_player.symbol):
                print(f"Congratulations {self.current_player.name}! You won!")
                break
                
            if self.board.is_full():
                print("It's a tie!")
                break
                
            self.switch_player()
            
    def play_again(self):
        """Ask players if they want to play again"""
        while True:
            choice = input("Do you want to play again? (y/n): ").lower()
            if choice in ['y', 'n']:
                return choice == 'y'
            print("Invalid choice! Please enter 'y' or 'n'.")