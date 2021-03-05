from model import Board
from errors import NonEmptyPositionError

class UI:
    def __init__(self):
        self.board = Board()
        self.run_game()

    def run_game(self):
        turn = self.board.x  # game starts with X
        while True:
            game_over = self.board.game_won() or self.board.board_full()
            try:
                print(self.board)

                if game_over:
                    if self.board.game_won():
                        print(str(self.board.winner) + " wins!")
                    else:
                        print("Game is a tie.")
                    print("Restart? (y/n)", end=" ")
                    if input().lower() == "y":
                        main()
                    else:
                        break
                else:
                    print(str(turn) + "'s turn")
                    print("Input position: ", end="") # 9 squares from left to right, top to bottom
                    position = int(input())
                    if position < 1 or position > 9:
                        raise IndexError
                    if (turn == self.board.x):
                        self.board.place_x(position)
                        turn = self.board.o
                    else:
                        self.board.place_o(position)
                        turn = self.board.x
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