from IPython.display import clear_output
import time

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
current_player_char = 'X'
next_player_char = 'O'
totalInputs = 9
winner = None


def checkHorizontal():
    global winner
    for row in board:
        if row[0] == row[1] == row[2]:
            winner = row[0]
            return


def checkVertical():
    global winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            winner = board[0][col]
            return


def checkDiagonal():
    global winner
    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
        return
    if board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]
        return


def checkBoard():
    checkHorizontal()
    checkVertical()
    checkDiagonal()
    return winner is not None


def placeCharacterOnBoard(pos):
    global board
    row = (pos - 1) // 3
    col = (pos - 1) % 3
    if isinstance(board[row][col], int):
        board[row][col] = current_player_char
        return 1
    else:
        print("Invalid position. Please choose a position that does not contain X or O.")
        return 0


def printCurrentBoard():
    print("-------------")
    for eachRow in board:
        print("|", end="")
        for eachCol in eachRow:
            print(f" {eachCol} ", end="|")
        print()
        print("-------------")


def runGame():
    global current_player_char, next_player_char, winner
    welcome_msg = '''Welcome to the TIC-TAC-TOE game. The first player to place a character on the board will be Player 1 (Character X) and the other player will be Player 2 (Character O).'''
    print(welcome_msg)
    inputCount = 0
    while inputCount < totalInputs:
        printCurrentBoard()
        position = int(input(f"Player {(inputCount % 2) + 1}, enter a position that does not contain any X or O:"))
        validityofInput = placeCharacterOnBoard(position)
        inputCount += validityofInput
        if inputCount >= 5:
            if checkBoard():
                winner = "Player 1" if current_player_char == 'X' else "Player 2"
                clear_output()
                break
        if validityofInput:
            current_player_char, next_player_char = next_player_char, current_player_char
        clear_output()
    printCurrentBoard()
    if winner is not None:
        print(f"Well done, {winner}. You have won the game.")
    else:
        print("The game ended in a draw.")


runGame()