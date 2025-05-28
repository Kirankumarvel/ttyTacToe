class Board:
    def __init__(self):
        self.reset()
        
    def reset(self):
        """Reset the board to empty state"""
        self.cells = [" " for _ in range(9)]
        
    def display(self):
        """Display the current board state"""
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.cells[i]} | {self.cells[i+1]} | {self.cells[i+2]} ")
            if i < 6:
                print("-----------")
        print("\n")
        
    def update(self, position, symbol):
        """Update the board with player's move"""
        if self.is_valid_move(position):
            self.cells[position-1] = symbol
            return True
        return False
        
    def is_valid_move(self, position):
        """Check if the move is valid"""
        return 1 <= position <= 9 and self.cells[position-1] == " "
        
    def is_full(self):
        """Check if the board is full"""
        return " " not in self.cells
        
    def check_winner(self, symbol):
        """Check if the current player has won"""
        # Check rows
        for i in range(0, 9, 3):
            if all(cell == symbol for cell in self.cells[i:i+3]):
                return True
                
        # Check columns
        for i in range(3):
            if all(self.cells[i+j] == symbol for j in range(0, 9, 3)):
                return True
                
        # Check diagonals
        if self.cells[0] == symbol and self.cells[4] == symbol and self.cells[8] == symbol:
            return True
        if self.cells[2] == symbol and self.cells[4] == symbol and self.cells[6] == symbol:
            return True
            
        return False