board = [' ' for _ in range(9)]

def print_board():
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def check_win(player):
    winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def play_game():
    current_player = 'X'
    while True:
        print_board()
        move = input(f"Player {current_player}, enter your move (1-9): ")
        if board[int(move) - 1] == ' ':
            board[int(move) - 1] = current_player
            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move, try again.")

play_game()            

            
