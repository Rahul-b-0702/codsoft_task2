from game_logic import available_moves, check_winner, make_move


AI_PLAYER = "O"
HUMAN_PLAYER = "X"


def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == AI_PLAYER:
        return 1
    if winner == HUMAN_PLAYER:
        return -1
    if not available_moves(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in available_moves(board):
            next_board = board.copy()
            make_move(next_board, move, AI_PLAYER)
            score = minimax(next_board, False)
            best_score = max(best_score, score)
        return best_score

    best_score = float("inf")
    for move in available_moves(board):
        next_board = board.copy()
        make_move(next_board, move, HUMAN_PLAYER)
        score = minimax(next_board, True)
        best_score = min(best_score, score)
    return best_score


def best_move(board):
    moves = available_moves(board)
    if not moves:
        return None

    preferred_order = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    ordered_moves = [move for move in preferred_order if move in moves]

    best_score = -float("inf")
    chosen_move = ordered_moves[0]

    for move in ordered_moves:
        next_board = board.copy()
        make_move(next_board, move, AI_PLAYER)
        score = minimax(next_board, False)
        if score > best_score:
            best_score = score
            chosen_move = move

    return chosen_move
