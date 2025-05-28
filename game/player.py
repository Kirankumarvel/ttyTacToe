class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        
    def get_move(self):
        """Get player's move from input"""
        while True:
            try:
                move = int(input(f"{self.name}'s turn ({self.symbol}). Enter position (1-9): "))
                return move
            except ValueError:
                print("Invalid input! Please enter a number between 1-9.")