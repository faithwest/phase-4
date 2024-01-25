
def for_red_piece(self, node_position):
    column, row = node_position
    moves = []
    if self.board[column][row].piece and self.board[column][row].piece.team == "R":
        vectors = [[1, -1], [1, 1]]  # Directions for regular red pieces
        if self.board[column][row].piece.type == "KING":
            vectors += [[-1, -1], [-1, 1]]  # Add directions for king red pieces
        for vector in vectors:
            new_column, new_row = column + vector[0], row + vector[1]
            if self._is_valid_move(new_column, new_row):
                moves.append((new_column, new_row))
            elif self._is_valid_capture_move(new_column, new_row):
                new_column += vector[0]  # Jump over captured piece
                new_row += vector[1]
                moves.append((new_column, new_row))
                # Continue checking for chains of captures
                while self._is_valid_capture_move(new_column, new_row):
                    new_column += vector[0]
                    new_row += vector[1]
                    moves.append((new_column, new_row))
    return moves
