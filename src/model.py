from errors import NonEmptyPositionError


class Mark:
    X = "X"
    O = "O"
    EMPTY = " "

    def __init__(self):
        self.set_empty()

    def set_x(self):
        self.mark = Mark.X

    def set_o(self):
        self.mark = Mark.O

    def set_empty(self):
        self.mark = Mark.EMPTY

    def is_x(self):
        return self.mark == Mark.X

    def is_o(self):
        return self.mark == Mark.O

    def is_empty(self):
        return self.mark == Mark.EMPTY

    def __eq__(self, other):
        return self.mark == other.mark

    def __str__(self):
        return self.mark


class Board:
    def __init__(self):
        self.board_dict = {
            1: Mark(), 2: Mark(), 3: Mark(),
            4: Mark(), 5: Mark(), 6: Mark(),
            7: Mark(), 8: Mark(), 9: Mark()
        }
        self.winner = Mark()
        self.winner.set_empty()

    def reset_board(self):
        for mark in self.board_dict.values():
            mark.set_empty()
        self.winner.set_empty()

    def place_x(self, position):
        if self.board_dict[position] != Mark():
            raise NonEmptyPositionError
        self.board_dict[position].set_x()

    def place_o(self, position):
        if self.board_dict[position] != Mark():
            raise NonEmptyPositionError
        self.board_dict[position].set_o()

    # def place_mark(self, position, player):
    #     if player == self.x:
    #         self.place_x(position)
    #     elif player == self.o:
    #         self.place_o(position)

    def board_full(self):
        for mark in self.board_dict.values():
            if mark.is_empty():
                return False
        return True

    def game_won(self):
        if self.board_dict[4] == self.board_dict[5] == self.board_dict[6] != Mark() or \
                self.board_dict[2] == self.board_dict[5] == self.board_dict[8] != Mark() or \
                self.board_dict[1] == self.board_dict[5] == self.board_dict[9] != Mark() or \
                self.board_dict[3] == self.board_dict[5] == self.board_dict[7] != Mark():
            self.winner = self.board_dict[5]
            return True
        elif self.board_dict[1] == self.board_dict[2] == self.board_dict[3] != Mark() or \
                self.board_dict[1] == self.board_dict[4] == self.board_dict[7] != Mark():
            self.winner = self.board_dict[1]
            return True
        elif self.board_dict[7] == self.board_dict[8] == self.board_dict[9] != Mark() or \
                self.board_dict[3] == self.board_dict[6] == self.board_dict[9] != Mark():
            self.winner = self.board_dict[9]
            return True
        else:
            return False

    def __str__(self):
        board = str(self.board_dict[1]) + " | " + str(self.board_dict[2]) + "| " + str(self.board_dict[3]) + "\n" + \
                "--------\n" + \
                str(self.board_dict[4]) + " | " + str(self.board_dict[5]) + "| " + str(self.board_dict[6]) + "\n" + \
                "--------\n" + \
                str(self.board_dict[7]) + " | " + str(self.board_dict[8]) + "| " + str(self.board_dict[9])
        return board
