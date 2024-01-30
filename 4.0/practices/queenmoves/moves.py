#the user inputs the number of queens
print("Enter the number of queens")
N = int(input())#int represents the number of queens whic is N

#next step is to initialize the board rep in 2D
board = [[0]*N for _ in range(N)]  #board size is N * N

###counter checking the dangers of placing a queen in a certain position,row,cols,diags
def is_attack(i, j):
    # checking if there is a queen in the same row or column#
    #a loop that iterates over the range from 0 to N1.
        ##ALSO CHECKS each cell ,i, and column ,j, for a queen presence
    for k in range(0, N):
        ##this function checks the presence of a queen 
        ##if there is then it reurns true,indicating an attack
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # checking diagonals
    # checking if there is a queen in the same row or column#
    #a loop that iterates over the range from 0 to N1.
        ##ALSO CHECKS each cell ,i, and column ,j, for a queen presence
    for k in range(0, N):
        ##
        for l in range(0, N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False
def N_queen(n):
    # if n is 0, a solution is found
    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            # checking if we can place a queen here or not
            # queen will not be placed if the place is being attacked or already occupied
            if (not is_attack(i, j)) and (board[i][j] != 1):
                board[i][j] = 1
                # recursion: whether we can put the next queen with this arrangement or not
                if N_queen(n - 1) == True:
                    return True
                board[i][j] = 0
    return False
