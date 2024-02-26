"""
Tic Tac Toe Player
"""
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    rows = board[0]+board[1]+board[2]
    count_x = rows.count("X")
    count_o = rows.count("O")
    if count_x > count_o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i in range(3):
        for j, value in enumerate(board[i]):
            if value == EMPTY:
                result.add((i, j))
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    try:
        new_board[action[0]][action[1]] = player(new_board)
        return new_board
    except IndexError:
        print("Invalid spot")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        count_x = row.count(X)
        count_o = row.count(O)
        if count_x == 3:
            return X
        elif count_o == 3:
            return O
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        elif board[0][i] == board[1][i] == board[2][i] == O:
            return O
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O
    elif board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count_empty = (board[0]+board[1]+board[2]).count(EMPTY)
    return count_empty == 0 or winner(board) is not None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player = player(board)
    if current_player == X:
        v = -math.inf
        for action in actions(board):
            k = min_value(result(board, action))
            if k > v:
                v = k
                best_move = action
    else:
        v = math.inf
        for action in actions(board):
            k = max_value(result(board, action))
            if k < v:
                v = k
                best_move = action
    return best_move


def max_value(board):
    if terminal(board):
        return utility(board)
    v = - math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
