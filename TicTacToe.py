import random

def choose_first():
    first_player_id = 0
    if random.randint(0,100) <= 50:
        first_player_id = 1
    else:
        first_player_id = 2
    return first_player_id

def player_input(first_player):
    player_marker = ''
    while not(player_marker == 'X' or player_marker == 'O'):
        player_marker = input(f"Player no.{first_player}! Select Marker X or O: ").upper()
    return player_marker
        
def display_board(board):
    print(f'{board[1]} | {board[2]} | {board[3]} \n_   _   _\n{board[4]} | {board[5]} | {board[6]}\n_   _   _\n{board[7]} | {board[8]} | {board[9]}')

def place_marker(board, marker, position):
    board[position] = marker

def check_if_won(board):
    if board[1] == board[2] == board[3] != " " or board [4] == board[5] == board[6] != " " or board[7] == board[8] == board[9] != " " or board[1] == board[4] == board[7] != " " or board[2] == board[5] == board[8] != " " or board[3] == board [6] == board[9] != " " or board[1] == board[5] == board[9] != " " or board[3] == board[5] == board[7] != " ":
        print("Congratulations, you won!")
        return True
    else:
        return False

def ask_about_position(marker, current_player):
    position = 0
    while position not in range(1,10):
        position = int(input(f"Player {current_player} {marker} choose position 1-9: "))
    if check_position(board,position):
        place_marker(board,marker,position)
    else:
        print("Wrong. Choose another non occupied position.")
    
def check_position(board,position):
    if board[position] == " ":
        return True
    else:
        return False

def space_on_board(board):
    for i in board[1:]:
        if i == " ":
            return True
    return False

def replay():
    answer = ''
    while not(answer == 'N' or answer == 'Y'):
        answer = input("Do you want to play again? (Y/N): ").upper()
    if answer == "Y":
        return True
    else:
        return False
    
def playing_player(current_player):
    if current_player == 1:
        return 2
    else:
        return 1
    
def marker_player(marker):
    if marker == "X":
        return "O"
    else:
        return "X"
       
while True:
    first_player = choose_first()
    board = [" "]
    board = 10 * board
    print(f"Hello to the game. The first goes player number: {first_player}.")
    marker = player_input(first_player)
    current_player = first_player  
    
    while not check_if_won(board):
        ask_about_position(marker,current_player)
        display_board(board)
        current_player = playing_player(current_player)
        marker = marker_player(marker)
        if not space_on_board(board):
            print('It is a draw. End of game.')
            break
    
    if not replay():
        break