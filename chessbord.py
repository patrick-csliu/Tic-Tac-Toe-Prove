import copy as _copy


# Define the winning combinations for Tic Tac Toe
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]


class Board:
    def __init__(self, board=None, history=[]):
        if board:
            self.board = board
        else:
            self.board = [[None, None, None] for i in range(3)]
        self.history = history

    def __repr__(self):
        board_str = [[' ', ' ', ' '] for i in range(3)]
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is True:
                    board_str[row][col] = 'O'
                elif self.board[row][col] is False:
                    board_str[row][col] = 'X'
                else:
                    pass
        line = '-' * 9
        board_lines = [" | ".join(row) for row in board_str]
        board_lines.insert(2, line)
        board_lines.insert(1, line)
        return "\n" + "\n".join(board_lines)
    
    def __getitem__(self, key):
        return self.board[key]
    
    # def __setitem__(self, key, value):
    #     self.board[key] = value
    
    # def __delitem__(self, key):
    #     del self.data[key]
    
    def show(self):
        print(repr(self))
    
    def check_win(self, player):
        for combo in winning_combinations:
            if all(self.board[i//3][i%3] == player for i in combo):
                return True
        return False
    
    def is_empty(self):
        empty = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is None:
                    empty.append(row*3 + col)
        return empty
        
    def put(self, position, player):
        if self.board[position//3][position%3] is not None:
            raise Exception("Position already occupied by another chess piece!")
        self.board[position//3][position%3] = player
        self.history.append(position)

    def copy(self):
        return Board(_copy.deepcopy(self.board), history=self.history.copy())
    
    def nospace(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True


if __name__ == "__main__":
    test_board = [
        [True, False, False],
        [None, True, False],
        [None, None, True],
    ]
    board = Board(test_board)
    board.show()
    print("O Win:", board.check_win(True))
    print("X Win:", board.check_win(False))
    print("Empty:", board.is_empty())
    board.put(7, False)
    print("After X put at 7:")
    board.show()
    print("No space:", board.nospace())
    board2 = board.copy()
    board.put(3, False)
    board.put(6, False)
    print("After X put at 3, 6:")
    board.show()
    print("No space:", board.nospace())

    board2.put(6, True)
    print("A copy:")
    board2.show()
    print("Origin after copy:")
    board.show()
