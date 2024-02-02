#N=4>>>BACKTRACKING
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

######################################################################################################################################
######simple predefined moves method

#In contrast, the code you provided is a straightforward implementation of 
#checking whether a queen on a chessboard can attack a specific square using 
#a predefined set of moves. It iterates through the predefined moves, checks 
#the resulting coordinates, and determines if the target square is reachable by a queen.

#define the moves
mvs = [
    {"y": 1, "x": 0},
    {"y": 0, "x": 1},
    {"y": -1, "x": 0},
    {"y": 0, "x": -1},
    {"y": 1, "x": 1},
    {"y": -1, "x": 1},
    {"y": -1, "x": -1},
    {"y": 1, "x": -1},
]

# Define row/column in numeric values to simplify the calculation
#function to check uf queen is under attack
def is_under_attack(row, col):
    x, y = row, col
    #iterate over all possible attacks from current position
    for m in mvs:
        xmv=x+move['x']
        ymv=y+move['y']

        #check if the row,col are within the board[index] 8*8 board
        if 0 <= xmv <=7 and 0 <= ymv <=7:
            #if there is an opponent's queen at that spot
            if board[xmv][ymv]==-1 : return True
    return False

#place n queens on the board
def placeQueensN(n):
    global board
    board=[ [-1]*8 for _ in range(8) ]   #initialize empty board with -1 representing no queen
    placement=[False]*n                  #keep track of which queen has been placed
    def backtrack(row):
        if row == n: printSolution()     #base case: all queens have been placed
        else:
            for col in range(8):         #try each column in this row
                if not placement[col]:   #if the space hasn't been filled yet
                    i=row; j=col          #save the row and column number
                    placement[j]=True    #mark this space as occupied
                    if is_under_attack(i,j)==False:       #no one can kill our queen here
                        board[i][j]=1      #place a queen here
                        backtrack(row + 1)  #recursion, next row
                        board[i][j]=-1     #clear this cell so it can be used by other queens
                        placement[j]=False#this space is free again
    backtrack(0)                         #start placing queens from first row

print("Number of Queens:")
numOfQns = int(input())
placeQueensN(numOfQns)
