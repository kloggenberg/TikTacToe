import os

def print_board(board):
    for row in board:
        print("|",end="")
        for element in row:
            print(" " + element + " ",end="|")
        print()


def take_choice():
    while True:
        choice = input("Please pick a position(press 'q' to exit game):\n")
        if choice.lower() == "q":
            return choice
        if 0 < int(choice) < 10:
            break
        else:
            print("Please enter a valid position.")
    return int(choice)


def check_win(board):
    # Horizontal checks
    if board[0][0] == board[0][1] == board[0][2]:
        return True
    elif board[1][0] == board[1][1] == board[1][2]:
        return True
    if board[2][0] == board[2][1] == board[2][2]:
        return True
    
    # Vertical checks
    elif board[0][0] == board[1][0] == board[2][0]:
        return True
    elif board[0][1] == board[1][1] == board[2][1]:
        return True
    elif board[0][2] == board[1][2] == board[2][2]:
        return True
    
    # Diagonal checks
    elif board[0][0] == board[1][1] == board[2][2]:
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        return True
    
    # If no matches
    else:
        return False

def update_board(board,turn,choice):
    if choice == 1:
        board[0][0] = turn
    elif choice == 2:
        board[0][1] = turn
    elif choice == 3:
        board[0][2] = turn
    elif choice == 4:
        board[1][0] = turn
    elif choice == 5:
        board[1][1] = turn
    elif choice == 6:
        board[1][2] = turn
    elif choice == 7:
        board[2][0] = turn
    elif choice == 8:
        board[2][1] = turn
    elif choice == 9:
        board[2][2] = turn
        
    return board


def change_turn(turn):
    if turn == "X":
        return "Y"
    else:
        return "X" 

    
def text_game():
    turn =  "X"
    
    board = [["1","2","3"],
             ["4","5","6"],
             ["7","8","9"]]
    
    while True:
        os.system("cls")
        
        print_board(board)
        
        choice = take_choice()
        if choice == "q":
            break
        
        board = update_board(board,turn,choice)
        os.system("cls")
        
        print_board(board)
        
        if check_win(board):
            print(f"Player {turn} wins!!!")
            break
        else:
            turn = change_turn(turn)
            
    print("Thanks for playing.")