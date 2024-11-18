"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
from random import choice

X = "X"
O = "O"
EMPTY = None

class InvalidActionError(Exception):
    def __init__(self, message):
        super().__init__(message)

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
    counter = 0
    for r in board:
        for i in r:
            if i == X:
                counter += 1
            elif i == O:
                counter -= 1

    if counter > 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == None:
                actions.append((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = deepcopy(board)
    i, j = action
    move = player(board)
    if board_copy[i][j] == None:
        board_copy[i][j] = move
        return board_copy
    else:
        raise InvalidActionError("Action provided isn't valid")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    row_count = [0, 0, 0]
    col_count = [0, 0, 0]
    diagonal_count = 0
    antidiagonal_count = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == X:
                move = 1
            elif board[i][j] == O:
                move = -1
            else:
                move = 0
            
            # Diagonais
            if i == j:
                diagonal_count += move
                
            if i + j == 2:
                antidiagonal_count += move
           
            row_count[i] += move
            col_count[j] += move
      
    if 3 in row_count or 3 in col_count or diagonal_count == 3 or antidiagonal_count == 3:
        return X
    if -3 in row_count or -3 in col_count or diagonal_count == -3 or antidiagonal_count == -3:
        return O
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for i in board:
        for j in i:
            if j == None:
                return False

    return True
    



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        result = winner(board)
        match result:
            case "X":
                return 1

            case "O":
                return -1

            case _:
                return 0
    

def maxValue(board):
    best_v = -math.inf
    best_action = None
    if terminal(board):
        return None, utility(board)
    
    for action in actions(board):
        _, v = minValue(result(board, action))
        if v > best_v:
            best_v = v
            best_action = action
    return best_action, best_v

def minValue(board):
    best_v = math.inf
    best_action = None
    if terminal(board):
        return None, utility(board)
    
    for action in actions(board):
        _, v = maxValue(result(board, action))
        if v < best_v:
            best_v = v
            best_action = action
    return best_action, best_v




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)
    match turn:
        case "X":
            if board == initial_state():
                action = choice(actions(board))   
                return action
            action, _ = maxValue(board)
        case "O":
            action, _ = minValue(board)
    return action
