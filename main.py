# Shawn Yang
# W02 Developer

# Print board
# Take player input
# check for win or tie
# switch player
# check for win or tie

board = [1,2,3,
         4,5,6,
         7,8,9]
winner=""
currentPlayer = "X"
haveWinner = False
gameDone = False





def main():
    # Print board
    while not (gameDone or is_Tie(board)):
        displayBoard(board)
        playerInput(board, currentPlayer)
        checkForWin(board)
    if haveWinner:
        print(f"{winner} is the winner.")
        print("Good game. Thanks for playing!")
    else:
        print("It is a tie. Thanks for playing!")
    

def displayBoard(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    

def playerInput(board, currentPlayer):
    # Set winner to the current player
    global winner

    square = int(input(f"{currentPlayer}'s turn to choose a square(1-9): "))
    if square >= 1 and square <= 9 and square == board[square - 1]:
        board[square - 1] = currentPlayer
        winner = currentPlayer
        switchPlayer()

    else:
        print("Square is taken already. Try Again.")


def switchPlayer():
    global currentPlayer

    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer ="X"

def checkForWin(board):
    
    global gameDone
    global haveWinner

    if board[0] == board[1] == board[2] or \
       board[3] == board[4] == board[5] or \
       board[6] == board[7] == board[8] or \
       board[0] == board[3] == board[6] or \
       board[1] == board[4] == board[7] or \
       board[2] == board[5] == board[8] or \
       board[0] == board[4] == board[8] or \
       board[2] == board[4] == board[6]:

       displayBoard(board)
       gameDone = True
       haveWinner = True
    
    

def is_Tie(board):
    for i in range(9):
        if board[i] != "X" and board[i] != "O":
            return False
    return True            
            
        
    
    

if __name__ == "__main__":
    main()

