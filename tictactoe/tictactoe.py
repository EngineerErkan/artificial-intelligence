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
    x_count, o_count = 0, 0
    for row in board:
        for column in row:
            if column == X:
                x_count += 1
            if column == O:
                o_count +=1
    if x_count <=  o_count:
        return X
    else:
        return O




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))

    return possible_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(new_board)

    return new_board
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #diagonal, vertical, horizontal
    if board[0][0] == board[1][1] == board[2][2]  != None:
        if board[1][1] == O:
            return O
        else:
            return X
    elif board[2][0] == board[1][1] == board[0][2]  != None:
        if board[2][0] == O:
            return O
        else:
            return X
    elif board[0][0] == board[0][1] == board[0][2]  != None:
        if board[0][0] == O:
            return O
        else:
            return X
    elif board[1][0] == board[1][1] == board[1][2]  != None:
        if board[1][0] == O:
            return O
        else:
            return X
    elif board[2][0] == board[2][1] == board[2][2]  != None:
        if board[2][0] == O:
            return O
        else:
            return X
    elif board[0][0] == board[1][0] == board[2][0]  != None:
        if board[2][0] == O:
            return O
        else:
            return X
    elif board[0][1] == board[1][1] == board[2][1]  != None:
        if board[2][1] == O:
            return O
        else:
            return X
    elif board[0][2] == board[1][2] == board[2][2]  != None:
        if board[2][2] == O:
            return O
        else:
            return X
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not actions(board):
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_value = winner(board)
    if winner_value == X:
        return 1
    elif winner_value == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)

    if board == [[EMPTY] * 3] * 3:
        return (0, 0)

    if p == X:
        v = float("-inf")
        selected = None
        for action in actions(board):
            min_value_result = min_value(result(board, action))
            if min_value_result > v:
                v = min_value_result
                selected = action
    elif p == O:
        v = float("inf")
        selected = None
        for action in actions(board):
            max_value_result = max_value(result(board, action))
            if max_value_result < v:
                v = max_value_result
                selected = action

    return selected


def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v
