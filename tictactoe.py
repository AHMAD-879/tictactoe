import copy

"""
Tic Tac Toe Player
"""

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
    # loops over all the cells and counts the occurrences
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1
    # if x has less occurrences, or the board is empty, it is X's turn
    if x_count <= o_count:
        return X
    else :
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(len(board)):
        for j in range(len(board)):
            value = board[i][j]
            if value == EMPTY :
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # if the move is invalid, raise an exception
    if action not in actions(board) :
        raise ValueError("Move invalid")

    copied_board = copy.deepcopy(board) # deep copy of the board
    (i, j) = action 
    copied_board[i][j] = player(board) # update the board copy with the new action move
    return copied_board
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check for a horizontal win
    for row in board:
        if row[0] == row[1] == row[2] :
            return row[0]   
    # check for a vertical win
    for j in range(len(board)) :
        if board[0][j] == board[1][j] == board[2][j] :
            return board[0][j]
    # check for a diagonal win
    if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]) :
        return board[1][1]
    # else if the game has no winner 
    else :
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # returns True if there is a winner or no actions are left
    return winner(board) != None or not actions(board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    champ = winner(board)
    if champ == X:
        return 1
    elif champ == O:
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
        return max_value(board)[1]
    else:
        return min_value(board)[1] 

def max_value(board):
    """
    Helper method for finding maximum utility of a board
    """
    if terminal(board):  
        return (utility(board), None)

    value = float("-inf")
    best_move = None
    # for each possible action
    for action in actions(board):
        result_board = result(board, action)
        min_utility = min_value(result_board)[0]
        if min_utility > value:
            value = min_utility
            best_move = action
    return (value, best_move)

def min_value(board):
    """
    Helper method for finding minimum utility of a board
    """
    if terminal(board):
        return (utility(board), None)

    value = float("inf")
    best_move = None
    # for each possible action
    for action in actions(board):
        result_board = result(board, action)
        max_utility = max_value(result_board)[0]
        if max_utility < value:
            value = max_utility
            best_move = action
    return (value, best_move)