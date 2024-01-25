board = [
    [" ", " ", " ", " ", " ", "W", " ", "W"],
    ["W", " ", "KW", " ", "W", " ", "W", ""],  # Remove the empty string here
    [" ", "B", " ", "B", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["B", " ", "B", " ", "B", " ", "B", " "],
    [" ", "B", " ", "B", " ", "B", " ", "B"],
    ["B", " ", "B", " ", "B", " ", "B", " "],
]
class Moves:
    def __init__(self, board, all_moves, piece, co):
        self.board = board
        self.all_moves = all_moves
        self.piece = piece
        self.co = co
        self.to_capture = True  # Assuming you want to capture by default, modify as needed

    def moves(self):
        all_moves = []

        if self.board[self.co["y"]][self.co["x"]] != self.piece:
            print("Piece not found")
            return all_moves

        for m in self.all_moves:
            to = m["to"]
            capture = m.get("capture")

            y_move = to["y"] + self.co["y"]
            x_move = to["x"] + self.co["x"]

            if not (0 <= x_move <= 7 and 0 <= y_move <= 7):
                continue

            move_position = self.board[y_move][x_move]
            if move_position:
                continue

            doc = {
                "from": {"x": self.co["x"], "y": self.co["y"]},
                "to": {"x": x_move, "y": y_move},
            }

            if capture:
                result = self.handle_capture(capture, x_move, y_move)
                if result:
                    doc["capture"] = result
                    all_moves.append(doc)
                continue

            all_moves.append({**doc, "capture": False})

        return all_moves

    def handle_capture(self, capture, x_move, y_move):
        if not self.to_capture:
            return None

        x = capture["x"]
        y = capture["y"]
        cap_x = x_move + x
        cap_y = y_move + y

        if not (0 <= cap_x <= 7 and 0 <= cap_y <= 7):
            return None

        capture_position = self.board[cap_y][cap_x]
        if capture_position in self.to_capture:
            return {"x": cap_x, "y": cap_y}

        return None


# class Wmoves(Moves):
#     def __init__(self, board, co):
#         all_moves = [
#             {"to": {"x": 1, "y": 1}, "capture": False},
#             {"to": {"x": -1, "y": 1}, "capture": False},
#             {"to": {"x": 2, "y": 2}, "capture": {"x": -1, "y": -1}},
#             {"to": {"x": -2, "y": 2}, "capture": {"x": 1, "y": -1}},
#         ]
#         super().__init__(board, all_moves, "W", co)


class Bmoves(Moves):
    def __init__(self, board, co):
        all_moves = [
            {"to": {"x": 1, "y": -1}, "capture": False},
            {"to": {"x": -1, "y": -1}, "capture": False},
            {"to": {"x": 2, "y": -2}, "capture": {"x": -1, "y": 1}},
            {"to": {"x": -2, "y": -2}, "capture": {"x": 1, "y": 1}},
        ]
        super().__init__(board, all_moves, "B", co)

class Bmoves(Moves):
    def __init__(self, board, co):
        all_moves = [
            {"to": {"x": 1, "y": -1}, "capture": False},
            {"to": {"x": -1, "y": -1}, "capture": False},
            {"to": {"x": 2, "y": -2}, "capture": {"x": -1, "y": 1}},
            {"to": {"x": -2, "y": -2}, "capture": {"x": 1, "y": 1}},
        ]
        super().__init__(board, all_moves, "B", co)


Kmoves = [
    {"to": {"x": 1, "y": 1}, "capture": False},
    {"to": {"x": -1, "y": 1}, "capture": False},
    {"to": {"x": 1, "y": -1}, "capture": False},
    {"to": {"x": -1, "y": -1}, "capture": False},
    {"to": {"x": 2, "y": 2}, "capture": {"x": -1, "y": -1}},
    {"to": {"x": -2, "y": 2}, "capture": {"x": 1, "y": -1}},
    {"to": {"x": 2, "y": -2}, "capture": {"x": -1, "y": 1}},
    {"to": {"x": -2, "y": -2}, "capture": {"x": 1, "y": 1}},
]

# all_Wmoves = [
#     {"to": {"x": 1, "y": 1}, "capture": False},
#     {"to": {"x": -1, "y": 1}, "capture": False},
#     {"to": {"x": 2, "y": 2}, "capture": {"x": -1, "y": -1}},
#     {"to": {"x": -2, "y": 2}, "capture": {"x": 1, "y": -1}},
# ]

all_Bmoves = [
    {"to": {"x": 1, "y": -1}, "capture": False},
    {"to": {"x": -1, "y": -1}, "capture": False},
    {"to": {"x": 2, "y": -2}, "capture": {"x": -1, "y": 1}},
    {"to": {"x": -2, "y": -2}, "capture": {"x": 1, "y": 1}},
]

class KWmoves(Moves):
    def __init__(self, board, co):
        super().__init__(board, Kmoves, "KW", co)


class KBmoves(Moves):
    def __init__(self, board, co):
        super().__init__(board, Kmoves, "KB", co)



# Create an instance of Bmoves with correct coordinates
b_moves_instance = Bmoves(board, {"x": 1, "y": 5})  # Adjusted coordinates

# Call the moves method
b_moves_result = b_moves_instance.moves()

# Print the result
print("B_moves_result:", b_moves_result)

# The target position for checking
target_position = {"x": 1, "y": 5}

# Print intermediate values for debugging
print("Intermediate Values:")
print("board state:", board)
print("target_position:", target_position)
print("all_Bmoves:", all_Bmoves)

# Check if the target position is in the list of possible moves
matching_move = next((move for move in b_moves_result if move["to"] == target_position), None)

if matching_move:
    if matching_move["capture"]:
        print("It's a capture move!")
    elif matching_move["to"] in all_Bmoves:
         print("It's a king move!")
    else:
        print("It's a normal move!")
else:
    print("The target position is not a valid move.")

# # Create an instance of Wmoves
# # w_moves_instance = Wmoves(board, {"x": 3, "y": 2})

# # # Call the moves method
# # w_moves_result = w_moves_instance.moves()

# # Print the result
# # print("W_moves_result:", w_moves_result)



# # Create an instance of Bmoves
# b_moves_instance = Bmoves(board, {"x": 1, "y":6 })

# # Call the moves method
# b_moves_result = b_moves_instance.moves()

# # Print the result
# print("B_moves_result:", b_moves_result)

# # # Assuming the piece is a white piece, and you have an instance of Wmoves
# # w_moves_instance = Wmoves(board, {"x": 5, "y": 2})

# # Call the moves method
# # all_w_moves = w_moves_instance.moves()

# # The target position for checking
# target_position = {"x": 4, "y": 1}

# # Check if the target position is in the list of possible moves
# matching_move = next((move for move in all_Bmoves if move["to"] == target_position), None)

# matching_move = next((move for move in b_moves_result if move["to"] == target_position), None)

# if matching_move:
#     if matching_move["capture"]:
#         print("It's a capture move!")
#     elif matching_move["to"] in all_Bmoves:
#          print("It's a king move!")
#     else:
#         print("It's a normal move!")
# else:
#     print("The target position is not a valid move.")
