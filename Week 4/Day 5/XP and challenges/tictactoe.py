# need to creat a board
board = ["-","-","-",
        "-", "-", "-",
        "-", "-", "-"]

game_is_going = True

winner = None # X or O

current_player = "x"

# function to display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " +board[2])
    print(board[3] + " | " + board[4] + " | " +board[5])
    print(board[6] + " | " + board[7] + " | " +board[8])

def play_game():
    global winner
    display_board()

    while game_is_going:


        take_turn()

        check_game_over()

        switch_player()

    if winner == "x" or winner == "o":
            print(winner + " won")
    elif winner == None:
            print(winner)



def take_turn():
    position = input("Type where you want to mark 1-9: ")
    # subtracting one to make it an index
    position = int(position) - 1
    # board at position will turn to an X
    board[position] = current_player
    display_board()

def check_game_over():
    check_winner()
    check_tie()
    if check_winner() == "x":
        return "x"
    return "o"

def check_winner():
    
    #lets us access global variables
    global winner

    row_winners = check_row()

    column_winners = check_column()

    diaganol_winners = check_diaganol()

    if row_winners:
        winner = row_winners
        return winner
    elif column_winners:
        winner = column_winners
       
    elif diaganol_winners:
        winner= diaganol_winners
    else:
        winner = None
        return

    #check rows
    # check columns
    #check diaganol
    
def check_row():

    #need to pull global variable
    global game_is_going
    # saying row_1 will only be  only if all spots are equal
    row_1 = board[0] == board [1] == board [2] != "-"
    row_2 = board[3] == board [4] == board [5] != "-"
    row_3 = board[6] == board [7] == board [8] != "-" 

    # row 1 exists
    if row_1 or row_2 or row_3:
        print("game over")
        game_is_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]    
    return

def check_column():
        #need to pull global variable
    global game_is_going
    # saying row_1 will only be  only if all spots are equal
    col_1 = board[0] == board [3] == board [6] != "-"
    col_2 = board[1] == board [4] == board [7] != "-"
    col_3 = board[2] == board [5] == board [8] != "-" 

    # row 1 exists(has a match) then kill the game
    if col_1 or col_2 or col_3:
        print(f'Game over')
        game_is_going = False
    # returning the winner
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]    
    return

def check_diaganol():

    global game_is_going

    diag_1 = board[0] == board [4] == board [8] != "-"
    diag_2 = board[2] == board [4] == board [6] != "-"

    if diag_1 or diag_2:
        print(f'Game over')

    if diag_1:
        game_is_going = False
        return board[4]
    elif diag_2:
        return board[4]
    return

def check_tie():
    global board

    "-" not in board:
    print("It's a tie")
    return

def switch_player():
    global current_player
    if current_player == "x" :
        current_player = "o"
        print("O's Turn")
        return current_player

    if current_player == "o" :
        current_player = "x"
        print("X's Turn")

        return current_player
    
  
    

play_game()
