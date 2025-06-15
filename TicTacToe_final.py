# Initialize game variables
board = ["-" for _ in range(9)]
currentPlayer = "X"
winner = None
gameRunning = True

# Print the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Take player input safely
def playerInput(board):
    while True:
        try:
            inp = int(input(f"{currentPlayer}, enter a number (0-8): "))
            if inp >= 0 and inp <= 8:
                if board[inp] == "-":
                    board[inp] = currentPlayer
                    break
                else:
                    print("That spot is already taken!")
            else:
                print("Input must be between 0 and 8.")
        except ValueError:
            print("Please enter a valid integer between 0 and 8.")

# Check for win conditions
def checkHorizontal(board):
    global winner
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            winner = board[i]
            return True
    return False

def checkVertical(board):
    global winner
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != "-":
            winner = board[i]
            return True
    return False

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkWin():
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        printBoard(board)
        print(f"🎉 The winner is {winner}!")
        return True
    return False

def checkTie():
    if "-" not in board:
        printBoard(board)
        print("🤝 It's a tie!")
        return True
    return False

def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

# Game loop (max 9 turns)
for _ in range(9):
    printBoard(board)
    playerInput(board)
    if checkWin():
        break
    if checkTie():
        break
    switchPlayer()
