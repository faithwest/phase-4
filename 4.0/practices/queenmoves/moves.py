#the user inputs the number of queens
print("Enter the number of queens")
N = int(input())#int represents the number of queens whic is N

#next step is to initialize the board rep in 2D
board = [[0]*N for _ in range(N)]  #board size is N * N

###counter checking the dangers of placing a queen in a certain position,row,cols,diags
def is_attack(i, j):
    # checking if there is a queen in the same row or column
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # checking diagonals
    for k in range(0, N):
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False
