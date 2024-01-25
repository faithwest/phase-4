class UpdateBoard:
    def __init__(self, board):
        self.board = board.copy()  # Create a copy of the board

    def valid_moves(self, moves):
        """Marks valid moves on the board."""
        if isinstance(moves, list):
            for move in moves:
                to_row, to_col = move["to"]
                self.board[to_row][to_col] = "X"
            print(self.board)  # Print for debugging
            return self.board

    def move_capture(self, move):
        """Executes a move with a capture."""
        from_row, from_col = move["from"]
        to_row, to_col = move["to"]
        capture_row, capture_col = move["capture"]

        piece = self.board[from_row][from_col]
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = ""
        self.board[capture_row][capture_col] = ""
        return self.board

    def move_only(self, move):
        """Executes a move without a capture."""
        from_row, from_col = move["from"]
        to_row, to_col = move["to"]

        piece = self.board[from_row][from_col]
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = ""
        return self.board

    def analyze_board(self):
        """Checks for kings at the starting rows."""
        black_row = 0
        white_row = 7

        for i in range(len(self.board[black_row])):
            if self.board[black_row][i] == "B":
                self.board[black_row][i] = "KB"

        for i in range(len(self.board[white_row])):
            if self.board[white_row][i] == "W":
                self.board[white_row][i] = "KW"
        return self.board  # Indentation corrected for return statement

    def update_board(self, position, value):
        """Updates a specific position on the board with a given value."""
        row, col = position
        self.board[row][col] = value  # Indentation corrected for assignment
        return self.board

# Example usage (outside the class):
board = [
    # ... (Your board configuration)
]
update_board = UpdateBoard(board)
updated_board = update_board.update_board((4, 1), "R")

# Print the updated board
for row in updated_board:
    print(' '.join(row))
