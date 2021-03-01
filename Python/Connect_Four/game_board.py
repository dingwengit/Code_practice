
WIN_CONNECTED_PIECES = 4


class ConnectFourBoard():
    """
    Game board class for Connect Four
    """
    def __init__(self, row=6, col=7):
        if row <=0 or col <= 0:
            raise ValueError("Invalid row {} or col {}".format(row, col))
        self.row, self.col = row, col
        self.board = [['*' for _ in range(col)] for _ in range(row)]
        self.players = ['x','o']
        self.current_player_idx = None

    def __repr__(self):
        ret = []
        for row in self.board:
            ret += " ".join(row)
            ret += ["\r\n"]
        return ''.join(ret)

    def __validate_move(self, player_id, row, col):
        return self.board[row][col] == '*'

    def __validate_player(self, player_id):
        return self.current_player_idx is None or \
               self.current_player_idx != player_id

    def __find_player_win(self, row):
        if len(row) < WIN_CONNECTED_PIECES:
            return False

        cnt = 0
        for item in row:
            if self.players[self.current_player_idx] == item:
                cnt += 1
                if cnt >= WIN_CONNECTED_PIECES:
                    return True
            else:
                cnt = 0
        return False

    def __get_diagonals_lr(self, row_idx, col_idx):
        res = []
        r, c = row_idx, col_idx
        while self.row > r >=0 and self.col > c >=0:
            res.append(self.board[r][c])
            r, c = r - 1, c - 1
        r, c = row_idx + 1, col_idx + 1
        while self.row > r >=0 and self.col > c >=0:
            res.append(self.board[r][c])
            r, c = r + 1, c + 1
        return res

    def __get_diagonals_ur(self, row_idx, col_idx):
        res = []
        r, c = row_idx, col_idx
        while self.row > r >=0 and self.col > c >=0:
            res.append(self.board[r][c])
            r, c = r + 1, c - 1
        r, c = row_idx - 1, col_idx + 1
        while self.row > r >=0 and self.col > c >=0:
            res.append(self.board[r][c])
            r, c = r - 1, c + 1
        return res

    def __check_win(self, row_idx, col_idx):
        # check rows
        if self.__find_player_win(self.board[row_idx]):
            return True

        # check columns
        column = [row[col_idx] for row in self.board]
        if self.__find_player_win(column):
            return True

        # lower-left-to-upper-right
        diagonals_lr = self.__get_diagonals_lr(row_idx, col_idx)
        if self.__find_player_win(diagonals_lr):
            return True
        # upper-left-to-lower-right diagonals
        diagonals_ur = self.__get_diagonals_ur(row_idx, col_idx)
        if self.__find_player_win(diagonals_ur):
            return True
        return False

    def place_move(self, player_id, row, col):
        """
        player to place a move
        :param player_id: player id (0,1)
        :param row: position in row
        :param col: position in col
        :return: True if win, else false
        """
        if not (self.row > row >= 0 and self.col > col >= 0):
            raise ValueError("Invalid row {} or col {}".format(row, col))
        if player_id not in range(len(self.players)):
            raise ValueError("Invalid player_id {}".format(player_id))

        if not self.__validate_player(player_id):
            raise ValueError("Invalid player turn {}".format(player_id))

        if not self.__validate_move(player_id, row, col):
            raise ValueError("Invalid move because the place is already "
                             "occupied by {}".format(self.board[row][col]))

        self.board[row][col] = self.players[player_id]
        self.current_player_idx = player_id

        print("Player {} placed on {}:{}".format(self.players[player_id],
                                                 row, col))
        print(self)

        if self.__check_win(row, col):
            print("**** player {} wins ****\r\n"
                  .format(self.players[self.current_player_idx]))
            return True
        return False
