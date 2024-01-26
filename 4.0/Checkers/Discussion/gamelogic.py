board = [
    [" ", " ", " ", " ", " ", "W", " ", "W"],
    ["W", " ", "KW", " ", "W", " ", "W", " "],
    [" ", "B", " ", "B", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", "", " "],
    ["B", " ", "B", " ", "B", " ", "B", " "],
    [" ", "B", " ", "B", " ", "B", " ", "B"],
    ["B", " ", "B", " ", "B", " ", "B", " "],
]

def move_piece():
    piece = "KW"
    current_position = {"x": 2, "y": 1}
    to_position = {"x": 4, "y": 3}

    if board[current_position["y"]][current_position["x"]] != piece:
        print("error")
        return

    kwm = KWmoves(board, current_position)
    all_kwm = kwm.moves()
    print("all_kwm", all_kwm)

    ub = UpdateBoard(board)

    for m in all_kwm:
        if to_position["x"] == m["to"]["x"] and to_position["y"] == m["to"]["y"]:
            print("Move", m)
            if m["capture"]:
                new_board = ub.move_capture(move_data={
                    "from": current_position,
                    "to": m["to"],
                    "capture": m["capture"],
                })
                print(new_board)
                return
            else:  # normal move
                new_board = ub.move_only(move_data={
                    "from": current_position,
                    "to": m["to"],
                })
                print(new_board)
                return

    print("No move was made")

move_piece()