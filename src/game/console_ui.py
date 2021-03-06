from model import *
from errors import NonEmptyPositionError


class UI:
    def __init__(self):
        self.board = Board()
        self.turn = Mark()
        self.turn.set_x()  # game starts with X
        self.run_game()

    def reset_game(self):
        self.board.reset_board()
        self.turn.set_x()

    def run_game(self):
        run = True
        while run:
            game_over = self.board.game_won() or self.board.board_full()
            try:
                print(self.board)

                if game_over:
                    if self.board.game_won():
                        print(self.board.winner, "wins!")
                    else:
                        print("Game is a tie.")
                    print("Restart? (y/n)", end=" ")
                    if input().lower() == "y":
                        self.reset_game()
                        continue
                    else:
                        # run = False
                        break
                else:
                    print(str(self.turn) + "'s turn")
                    print("Input position: ", end="")  # 9 squares from left to right, top to bottom
                    position = int(input())
                    if position < 1 or position > 9:
                        raise IndexError
                    if (self.turn.is_x()):
                        self.board.place_x(position)
                        self.turn.set_o()
                    else:
                        self.board.place_o(position)
                        self.turn.set_x()
            except NonEmptyPositionError:
                print("Position is already filled")
                continue
            except ValueError:
                print("Not an integer")
                continue
            except IndexError:
                print("Integer must be from 1 to 9")
                continue


def main():
    UI()


if __name__ == "__main__":
    main()
