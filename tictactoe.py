"""
Tic Tac Toe Game Analysis

This Python script aims to verify that in a game of Tic Tac Toe, neither 
player "X" nor player "O" can win if both players make optimal moves. The 
goal is to prove that the game will always result in a tie when both players 
make the right action choices.

First, we must demonstrate that the first player must win, and then we must 
show that the second player must win. If both assumptions are proven to be 
untrue, then we can establish "No one can win".

"""

from chessboard import Board


def show(board):
    board.show()
    print('='*10)


def play_chess(board: Board, verify_o: bool, player: bool) -> bool:
    """Simulate "O's" turns.

    Parameters
    ----------
    board : Board
        The current Tic Tac Toe board state.
    verify_o : bool
        Determines whether we are verifying "O's" win or "X's" win.
        True for "O," False for "X."
    player: bool
        True stand for "O" turns.
        False stand for "X" turns.

    Returns
    -------
    bool
        If verify_o is True and player is True:
            - Returns True if "O" will win with the right move.
            - Returns False if "O" will lose regardless of the move they make.

        If verify_o is False and player is True:
            - Returns True if "X" will win regardless of "O's" move.
            - Returns False if "X" will lose if "O" makes the right move.

        If verify_o is True and player is False:
            - Returns True if "O" will win regardless of "X's" move.
            - Returns False if "O" will lose if "X" makes the right move.

        If verify_o is False and player is False:
            - Returns True if "X" will win with the right move.
            - Returns False if "X" will lose regardless of the move they make.

    """
    next_chess = board.is_empty()
    results = []
    for pos in next_chess:
        board_next = board.copy()
        board_next.put(pos, player)
        if board_next.check_win(player):
            results.append(not (verify_o != player))
            break
        elif board_next.nospace():
            results.append(False)
            if verify_o != player:
                break
        else:
            results.append(play_chess(board_next, verify_o, not player))
    if verify_o != player:
        return all(results)
    else:
        return any(results)


if __name__ == "__main__":
    print("O go first.")
    board = Board()
    result = play_chess(board, True, True)
    print("O will win:", result)

    board = Board()
    result = play_chess(board, False, True)
    print("X will win:", result)
