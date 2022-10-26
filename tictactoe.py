"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
from random import shuffle

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

    # Compare the count of 'X' and 'O' from the flattened list(board)
    return 'O' if sum(board, []).count(EMPTY) % 2 == 0 else 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Create an empty set for available tiles
    available = set()

    # Iterate through the whole board and check the EMPTY tiles
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                available.add((i, j))
    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # RAISE AN EXCEPTION FOR INVALID ACTIONS
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid move")

    # Deep copy the original board
    new = deepcopy(board)
    new[action[0]][action[1]] = player(board)
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check the two diagonals
    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] is not EMPTY:
            return board[1][1]

    # Check for all horizontal and vertical
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] is not EMPTY:
                return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] is not EMPTY:
                return board[0][i]

    # No winning state
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True
    elif len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    w = winner(board)
    if w == 'X':
        return 1
    elif w == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # Terminal state
    if terminal(board):
        return None

    # Return optimal action with highest or lowest value
    if player(board) == 'X':
        return max_value(board)[0]
    else:
        return min_value(board)[0]


def max_value(board):
    """
    Returns the optimal action for the maximizing player
    """

    # Return value
    optimal_action = None

    # The base case (terminal) returns the value (1, 0 or -1)
    # NOTE: optimal_action will always be None in this case
    if terminal(board):
        return optimal_action, utility(board)

    # Find the optimal action
    value = -math.inf
    for action in randomly(actions(board)):
        temp = min_value(result(board, action))[1]
        if temp == 1:
            return action, temp
        if temp > value:
            value = temp
            optimal_action = action
    return optimal_action, value


def min_value(board):
    """
    Returns the optimal action for the minimizing player
    """

    # Return value
    optimal_action = None

    # The base case (terminal) returns the value (1, 0 or -1)
    # NOTE: optimal_action will always be None in this case
    if terminal(board):
        return optimal_action, utility(board)

    # Find the optimal action
    value = math.inf
    for action in randomly(actions(board)):
        temp = max_value(result(board, action))[1]
        if temp == -1:
            return action, temp
        if temp < value:
            value = temp
            optimal_action = action
    return optimal_action, value


def randomly(sequence):
    """
    Return a sequence(list or set) as a shuffled list
    """

    x = list(sequence)
    shuffle(x)
    return x
