
initial_board = [
    [" ", "W", "B ", "W", " ", "W", " ", "W"],
    ["W", " ", "W", " ", "W", " ", "W", " "],
    [" ", "W", " ", "W", " ", "W", " ", "W"],
    [" ", " ", "", " ", " ", " ", " ", " "],
    [" ", " ", " ", " W", " ", " ", "", " "],
    ["B", " ", "B", " ", "B", " ", "B", " "],
    [" ", "B", " ", "B", " ", "B", " ", "B"],
    ["B", " ", "WK", " ", "B", " ", "B", " "],
]
class GameEngine:
    def __init__(self, board):
        self.board = board

    def is_valid_move(self, co):
        x, y = co

        if self.board[x][y] != "W":
            return []

        validated_moves = []


        for dx, dy in [(1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 7 and 0 <= ny < 7:
                if self.board[nx][ny] == " ":
                    validated_moves.append((nx, ny))  # Regular move
                    print(validated_moves)
                elif self.board[nx][ny] == "B" and 0 <= nx + dx < 7 and 0 <= ny + dy < 7 and self.board[nx + dx][ny + dy] == " ":
                    validated_moves.append((nx + dx, ny + dy))  # Capture move

        return validated_moves
        

    def display_board_with_possible_moves(self, possible_moves):
        board_with_indicators = [row[:] for row in self.board]
        for x, y in possible_moves:
            board_with_indicators[x][y] = "x"
        return board_with_indicators

if __name__ == "__main__":
    game_engine = GameEngine(initial_board)
    
    start_position = (2, 3)
    possible_moves = game_engine.is_valid_move(start_position)

    board_with_indicators = game_engine.display_board_with_possible_moves(possible_moves)

    # Print the board with indicators
    for row in board_with_indicators:
        print(" ".join(row))


class BlackMove:
    def __init__(self, board):
        self.board = board

    def is_valid_move(self, co):
        x, y = co

        if self.board[x][y] != "B":
            return []

        validated_moves = []

        for dx, dy in [(-1, 1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 7 and 0 <= ny < 7:
                if self.board[nx][ny] == " ":
                    validated_moves.append((nx, ny))  # Regular move
                elif self.board[nx][ny] == "W" and 0 <= nx + dx < 7 and 0 <= ny + dy < 7 and self.board[nx + dx][ny + dy] == " ":
                    # Capture move
                    validated_moves.append((nx + dx, ny + dy))

        return validated_moves

    def display_board_with_possible_moves(self, possible_moves):
        board_with_indicators = [row[:] for row in self.board]
        for x, y in possible_moves:
            board_with_indicators[x][y] = "O"
        return board_with_indicators

if __name__ == "__main__":
    

    black = BlackMove(initial_board)
    start_position = (5, 2)
    possible_moves = black.is_valid_move(start_position)
    board_with_indicators = black.display_board_with_possible_moves(possible_moves)

    # Print the board with indicators
    for row in board_with_indicators:
        print(" ".join(row))

class WhiteKing:
    def __init__(self, board):
        self.board=board


    def wk_move(self, co):
        x, y = co
        if self.board[7][y] == "W":
            self.board[7][y] = "WK"
            print("KING PROMOTION")
        else:
            print("invalid Coordinates")
        moves = [
            {"x": -2, "y": 2}, 
            {"x": -2, "y": -2},
        ]
        wk_moves=[]

        for move in moves:
            x_move = x + move["x"]
            y_move = y + move["y"]

            if not (0 <= y_move < 7 and 0 <= x_move < 7):
                continue
            wk_moves.append((x_move, y_move))
            print("Possible move: (", x_move,  ",", y_move, ")", sep="")
        return wk_moves

class BlackKing:
    def __init__(self, board):
        self.board = board

    def bk_move(self, co):
        x, y = co
        if self.board[0][y] == "B":  # Check for row 0
            self.board[0][y] = "BK"  # Update board with promoted king
            print("KING PROMOTION")
        else:
            print("invalid Coordinates")

        moves = [
            {"x": -2, "y": -2},
            {"x": -2, "y": 2},
            {"x": 2, y: 0}
        ]
        bk_moves = []

        for move in moves:
            x_move = x + move["x"]
            y_move = y + move["y"]

            if (0 <= y_move < 7 and 0 <= x_move < 7):
                #continue
                bk_moves.append((x_move, y_move))
                print("Possible move: (", x_move, ",", y_move, ")", sep="")
            return bk_moves


if __name__ == "__main__":
    blackking = BlackKing(initial_board)
    bk_moves = blackking.bk_move((1, 1))  # Example move to trigger promotion
    chosen_move = bk_moves[0]  # Example: Choose the first move
    self.board[chosen_move[0]][chosen_move[1]] = "BK"  # Apply the move

    print(initial_board)