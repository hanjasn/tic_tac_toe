import pygame
import os
from model import *
pygame.init()
os.chdir('../..') # redirect to project root from game package


class Game:
    WIDTH, HEIGHT = 960, 540
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    YELLOW = pygame.Color(255, 255, 0)
    GREEN = pygame.Color(0, 255, 0)
    GREY = pygame.Color(200, 200, 200)
    FPS = 120
    BOARD_LENGTH = int(HEIGHT * 0.8)
    BOARD_SQUARE_LENGTH = BOARD_LENGTH // 3
    MARK_SCALE_FACTOR = 0.8 # <= 1
    MARK_LENGTH = int(BOARD_SQUARE_LENGTH * MARK_SCALE_FACTOR)
    MARK_LENGTH_OFFSET = (BOARD_SQUARE_LENGTH - MARK_LENGTH)//2
    LINE_WIDTH = 10
    X_BOUNDARY_1 = WIDTH//2 - BOARD_LENGTH//2
    X_BOUNDARY_2 = X_BOUNDARY_1 + BOARD_SQUARE_LENGTH
    X_BOUNDARY_3 = X_BOUNDARY_2 + BOARD_SQUARE_LENGTH
    X_BOUNDARY_4 = X_BOUNDARY_3 + BOARD_SQUARE_LENGTH
    Y_BOUNDARY_1 = HEIGHT//2 - BOARD_LENGTH//2
    Y_BOUNDARY_2 = Y_BOUNDARY_1 + BOARD_SQUARE_LENGTH
    Y_BOUNDARY_3 = Y_BOUNDARY_2 + BOARD_SQUARE_LENGTH
    Y_BOUNDARY_4 = Y_BOUNDARY_3 + BOARD_SQUARE_LENGTH
    X_IMG = pygame.image.load(os.path.join('images', 'red_x.png'))
    O_IMG = pygame.image.load(os.path.join('images', 'blue_purple_circle.png'))
    X_IMG_SCALED = pygame.transform.scale(X_IMG, (MARK_LENGTH, MARK_LENGTH))
    O_IMG_SCALED = pygame.transform.scale(O_IMG, (int(MARK_LENGTH*1.2), int(MARK_LENGTH*1.2)))
    LINE_1 = pygame.Rect(X_BOUNDARY_2, Y_BOUNDARY_1, LINE_WIDTH, BOARD_LENGTH)
    LINE_2 = pygame.Rect(X_BOUNDARY_3, Y_BOUNDARY_1, LINE_WIDTH, BOARD_LENGTH)
    LINE_3 = pygame.Rect(X_BOUNDARY_1, Y_BOUNDARY_2, BOARD_LENGTH, LINE_WIDTH)
    LINE_4 = pygame.Rect(X_BOUNDARY_1, Y_BOUNDARY_3, BOARD_LENGTH, LINE_WIDTH)
    FONT = pygame.font.SysFont('Calibri', 70, True)
    RESTART = FONT.render("RESTART", True, YELLOW)
    RESTART_CTR_X = WIDTH // 2 - RESTART.get_width() // 2
    RESTART_CTR_Y = HEIGHT // 2 - RESTART.get_height() // 2

    def __init__(self):
        pygame.display.set_caption("Tic-tac-toe")
        pygame.display.set_icon(Game.X_IMG)
        self.init_game()
        self.render_game()
        self.turn_img = self.set_turn_img()
        self.turn_text = Game.FONT.render("{}'s turn".format(self.turn), True, Game.WHITE)
        self.clock = pygame.time.Clock()
        self.run_game()

    def init_game(self):
        self.board = Board()
        self.turn = Mark()
        self.turn.set_x() # game always starts with X

    def render_game(self):
        Game.WIN.fill(Game.BLACK)
        pygame.draw.rect(Game.WIN, Game.WHITE, Game.LINE_1)
        pygame.draw.rect(Game.WIN, Game.WHITE, Game.LINE_2)
        pygame.draw.rect(Game.WIN, Game.WHITE, Game.LINE_3)
        pygame.draw.rect(Game.WIN, Game.WHITE, Game.LINE_4)
        pygame.display.update()

    def run_game(self):
        self.run_game_loop()
        pygame.quit()

    def run_game_loop(self):
        run = True
        while run:
            self.clock.tick(Game.FPS)
            try:
                game_over = self.board.game_won() or self.board.board_full()
                if game_over:
                    end_text = None
                    if self.board.game_won():
                        end_text = Game.FONT.render("{} wins!".format(self.board.winner), True, Game.GREEN)
                    else:
                        end_text = Game.FONT.render("Tie game :C", True, Game.GREY)
                    Game.WIN.blit(end_text, (Game.WIDTH//2 - end_text.get_width()//2, Game.HEIGHT//2 - end_text.get_height()//2))
                    Game.WIN.blit(Game.RESTART, (Game.RESTART_CTR_X, Game.RESTART_CTR_Y + end_text.get_height()))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return
                        elif event.type == pygame.MOUSEBUTTONDOWN and \
                                Game.RESTART_CTR_X <= pygame.mouse.get_pos()[0] <= Game.RESTART_CTR_X + Game.RESTART.get_width() and \
                                Game.RESTART_CTR_Y + end_text.get_height() <= pygame.mouse.get_pos()[1] <= \
                                                                              Game.RESTART_CTR_Y + end_text.get_height() + Game.RESTART.get_height():
                            self.reset_game()
                    continue
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return
                        self.set_turn_img()
                        self.display_turn()
                        self.place_mark_event(event)
            except NonEmptyPositionError:
                continue

    def reset_game(self):
        self.board.reset_board()
        self.turn.set_x()
        self.render_game()

    def set_turn_img(self):
        if self.turn.is_x():
            self.turn_img = Game.X_IMG_SCALED
        else:
            self.turn_img = Game.O_IMG_SCALED

    def display_turn(self):
        turn_text_loc = (Game.X_BOUNDARY_1 - self.turn_text.get_width(), Game.HEIGHT//2 - self.turn_text.get_height()//2)
        self.turn_text.fill(Game.BLACK)
        Game.WIN.blit(self.turn_text, turn_text_loc)

        self.turn_text = Game.FONT.render("{}'s turn".format(self.turn), True, Game.WHITE)
        turn_text_loc = (Game.X_BOUNDARY_1 - self.turn_text.get_width(), Game.HEIGHT//2 - self.turn_text.get_height()//2)
        Game.WIN.blit(self.turn_text, turn_text_loc)
        pygame.display.update()

    def place_mark_event(self, event):
        check_column_1 = Game.X_BOUNDARY_1 < pygame.mouse.get_pos()[0] < Game.X_BOUNDARY_2
        check_column_2 = Game.X_BOUNDARY_2 < pygame.mouse.get_pos()[0] < Game.X_BOUNDARY_3
        check_column_3 = Game.X_BOUNDARY_3 < pygame.mouse.get_pos()[0] < Game.X_BOUNDARY_4
        check_row_1 = Game.Y_BOUNDARY_1 < pygame.mouse.get_pos()[1] < Game.Y_BOUNDARY_2
        check_row_2 = Game.Y_BOUNDARY_2 < pygame.mouse.get_pos()[1] < Game.Y_BOUNDARY_3
        check_row_3 = Game.Y_BOUNDARY_3 < pygame.mouse.get_pos()[1] < Game.Y_BOUNDARY_4
        check_within_boundary = check_column_1 and check_row_1 or check_column_2 and check_row_1 or \
                                check_column_3 and check_row_1 or check_column_1 and check_row_2 or \
                                check_column_2 and check_row_2 or check_column_3 and check_row_2 or \
                                check_column_1 and check_row_3 or check_column_2 and check_row_3 or \
                                check_column_3 and check_row_3
        if event.type == pygame.MOUSEBUTTONDOWN and check_within_boundary:
            if check_column_1 and check_row_1:
                self.board.place_mark(self.turn, 1)
                Game.WIN.blit(self.turn_img, (Game.X_BOUNDARY_1 + Game.MARK_LENGTH_OFFSET, Game.Y_BOUNDARY_1 + Game.MARK_LENGTH_OFFSET))
            elif check_column_2 and check_row_1:
                self.board.place_mark(self.turn, 2)
                Game.WIN.blit(self.turn_img, (Game.X_BOUNDARY_2 + Game.MARK_LENGTH_OFFSET, Game.Y_BOUNDARY_1 + Game.MARK_LENGTH_OFFSET))
            elif check_column_3 and check_row_1:
                self.board.place_mark(self.turn, 3)
                Game.WIN.blit(self.turn_img, (Game.X_BOUNDARY_3 + Game.MARK_LENGTH_OFFSET, Game.Y_BOUNDARY_1 + Game.MARK_LENGTH_OFFSET))
            elif check_column_1 and check_row_2:
                self.board.place_mark(self.turn, 4)
                Game.WIN.blit(self.turn_img, (Game.X_BOUNDARY_1 + Game.MARK_LENGTH_OFFSET, Game.Y_BOUNDARY_2 + Game.MARK_LENGTH_OFFSET))
            elif check_column_2 and check_row_2:
                self.board.place_mark(self.turn, 5)
                Game.WIN.blit(self.turn_img, (Game.X_BOUNDARY_2 + Game.MARK_LENGTH_OFFSET, Game.Y_BOUNDARY_2 + Game.MARK_LENGTH_OFFSET))
            elif check_column_3 and check_row_2:
                self.board.place_mark(self.turn, 6)
                Game.WIN.blit(self.turn_img, (Game.X_BOUNDARY_3 + Game.MARK_LENGTH_OFFSET, Game.Y_BOUNDARY_2 + Game.MARK_LENGTH_OFFSET))
            elif check_column_1 and check_row_3:
                self.board.place_mark(self.turn, 7)
                Game.WIN.blit(self.turn_img, (Game.X_BOUNDARY_1 + Game.MARK_LENGTH_OFFSET, Game.Y_BOUNDARY_3 + Game.MARK_LENGTH_OFFSET))
            elif check_column_2 and check_row_3:
                self.board.place_mark(self.turn, 8)
                Game.WIN.blit(self.turn_img, (Game.X_BOUNDARY_2 + Game.MARK_LENGTH_OFFSET, Game.Y_BOUNDARY_3 + Game.MARK_LENGTH_OFFSET))
            elif check_column_3 and check_row_3:
                self.board.place_mark(self.turn, 9)
                Game.WIN.blit(self.turn_img, (Game.X_BOUNDARY_3 + Game.MARK_LENGTH_OFFSET, Game.Y_BOUNDARY_3 + Game.MARK_LENGTH_OFFSET))
            pygame.display.update()
            if self.turn.is_x():
                self.turn.set_o()
            else:
                self.turn.set_x()


def main():
    Game()


if __name__ == "__main__":
    main()