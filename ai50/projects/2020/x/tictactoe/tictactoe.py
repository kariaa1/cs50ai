"""
Tic Tac Toe Player
"""

import math
import itertools
import copy

X = "X"
O = "O"
EMPTY = None

win_states=[
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]]

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

    flat_list = list(itertools.chain(*board))
    p = flat_list.count(X) - flat_list.count(O)

    if p % 2 == 0 :
        return X
    else :
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    res = set()

    for i in range(3) :
        for j in range(3) :
            if board[i][j] == EMPTY :
                res.add((i,j))
    return res

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    if action[0] > 2 or action[0] < 0 or action[1] > 2 or action[1] < 0 :
        raise RuntimeError("Invalid action")

    res = copy.deepcopy(board)
    res[action[0]][action[1]] = player(board)

    return res

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for s in win_states :
        if board[s[0][0]][s[0][1]] != EMPTY and board[s[0][0]][s[0][1]] == board [s[1][0]][s[1][1]] == board[s[2][0]][s[2][1]] :
            return board[s[0][0]][s[0][1]]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    flat_list = list(itertools.chain(*board))
    if flat_list.count(EMPTY) == 0 :
        return True
    if winner(board) != None :
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == None :
        return 0
    elif winner(board) == X :
        return 1
    return -1

def max_value(board):

    if terminal(board) :
        return utility(board), None

    best_action = None
    best_v = -2

    v = -2
    for action in actions(board) :
        v = max(v, min_value(result(board, action))[0])
        
        if (v > best_v) :
            best_v = v
            best_action = action
    
    return v, best_action

def min_value(board):

    if terminal(board) :
        return utility(board), None

    best_action = None
    best_v = 2
    v = 2

    for action in actions(board) :
        v = min(v, max_value(result(board, action))[0])
        
        if (v < best_v) :
            best_v = v
            best_action = action
    
    return v, best_action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == O :
        r=min_value(board)
    else :
        r=max_value(board)

    return r[1]