def print_board(board):
    for i in range(3):
        print("|".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("-----")


def check_winner(board):
    combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in combos:
        if board[a] == board[b] == board[c] != ' ': #Если три ячейки одинаковы и не пустые
            return board[a]
    return None

def play_game():
    board = [' '] * 9
    for turn in range(9):
        print_board(board) # Отображаем текущее состояние поля
        move = int(input(f"Ход игрока '{'X' if turn % 2 == 0 else 'O'}': ")) - 1
        if board[move] == ' ':
            board[move] = 'X' if turn % 2 == 0 else 'O'
            if (winner := check_winner(board)):
                print_board(board)
                print(f"Игрок '{winner}' победил!")
                return
        else:
            print("Клетка занята! Попробуйте снова.")
    print_board(board)
    print("Ничья!")

play_game()
