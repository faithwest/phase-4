def valid_moves(self, arr):
        if isinstance(arr, list):
            for m in arr:
                to = m["to"]
                self.board[to["y"]][to["x"]] = "X"
            print(self.board)
            return self.board

def move_capture(self, move_data):
        piece = self.board[move_data["from"]["y"]][move_data["from"]["x"]] (5,2)#B
        self.board[move_data["to"]["y"]][move_data["to"]["x"]] = piece #possible move for a specific co "W"
        self.board[move_data["from"]["y"]][move_data["from"]["x"]] = "" #if next is empty"""
        self.board[move_data["capture"]["y"]][move_data["capture"]["x"]] = "" #capture true"
        return self.board

def move_only(self, move_data):
        piece = self.board[move_data["from"]["y"]][move_data["from"]["x"]] 
        self.board[move_data["to"]["y"]][move_data["to"]["x"]] = piece
        self.board[move_data["from"]["y"]][move_data["from"]["x"]] = ""
        return self.board

def analyze_board(self):
        Bkm = 0
        Wkm = 7

        black_row = self.board[Bkm]
        white_row = self.board[Wkm]

        # Black Piece
        for i in range(len(black_row)):
            piece = black_row[i]
            if piece == "B":
                self.board[B][i] = "KB"
            else:
                print("inalid Coordinates")
        #White Piece
        for i in range(len(white_row)):
            piece == white_row[i]
            if piece == "W":
                self.board[W] [i] = "KW"
            else:
                  print("Invalid Coordinates")
