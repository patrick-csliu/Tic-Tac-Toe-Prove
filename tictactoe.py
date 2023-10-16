from chessboard import Board

wins = []


def show(board):
    board.show()
    print('='*10)


def o_turns(board: Board):
    next_chess = board.is_empty()
    results = []
    for pos in next_chess:
        board_next = board.copy()
        board_next.put(pos, True)
        if board_next.check_win(True):
            results.append(True)
            wins.append(board_next)
            break
        elif board_next.nospace():
            results.append(False)
        else:
            results.append(x_turns(board_next))
    return any(results)


def x_turns(board: Board):
    next_chess = board.is_empty()
    results = []
    for pos in next_chess:
        board_next = board.copy()
        board_next.put(pos, False)
        if board_next.check_win(False):
            results.append(False)
            break
        elif board_next.nospace():
            results.append(False)
            break
        else:
            results.append(o_turns(board_next))
    return all(results)


def o_turns2(board: Board):
    next_chess = board.is_empty()
    results = []
    for pos in next_chess:
        board_next = board.copy()
        board_next.put(pos, True)
        if board_next.check_win(True):
            results.append(False)
            break
        elif board_next.nospace():
            results.append(False)
            break
        else:
            results.append(x_turns2(board_next))
    return all(results)


def x_turns2(board: Board):
    next_chess = board.is_empty()
    results = []
    for pos in next_chess:
        board_next = board.copy()
        board_next.put(pos, False)
        if board_next.check_win(False):
            results.append(True)
            wins.append(board_next)
            break
        elif board_next.nospace():
            results.append(False)
        else:
            results.append(o_turns2(board_next))
    return any(results)


if __name__ == "__main__":
    wins = []
    board = Board()
    result = o_turns(board)
    print("O will win:", result)
    print("Length of wins list:", len(wins))

    wins = []
    board = Board()
    result = o_turns2(board)
    print("X will win:", result)
    print("Length of wins list:", len(wins))
    # print(wins)
