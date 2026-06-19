BOARD_SIZE = 9
WINNING_COMBINATIONS = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def create_board():
    return ["" for _ in range(BOARD_SIZE)]


def available_moves(board):
    return [index for index, cell in enumerate(board) if cell == ""]


def make_move(board, index, player):
    if index < 0 or index >= BOARD_SIZE:
        return False
    if board[index] != "":
        return False

    board[index] = player
    return True


def check_winner(board):
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board):
    return check_winner(board) is None and all(cell != "" for cell in board)
