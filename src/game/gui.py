import pygame
import os
from model import *


class Game:
    WIDTH, HEIGHT = 960, 540
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    FPS = 120
    os.chdir('../..')
    BOARD_LENGTH = int(HEIGHT * 0.8)
    BOARD_SQUARE_LENGTH = BOARD_LENGTH // 3
    MARK_LENGTH = BOARD_SQUARE_LENGTH - 20
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
    O_IMG_SCALED = pygame.transform.scale(O_IMG, (MARK_LENGTH, MARK_LENGTH))

    def __init__(self):
        # self.clock = pygame.time.Clock()
        self.render_game()
        self.run_game()

    def render_game(self):
        line_1 = pygame.Rect(Game.X_BOUNDARY_2, Game.Y_BOUNDARY_1, Game.LINE_WIDTH, Game.BOARD_LENGTH)
        line_2 = pygame.Rect(Game.X_BOUNDARY_3, Game.Y_BOUNDARY_1, Game.LINE_WIDTH, Game.BOARD_LENGTH)
        line_3 = pygame.Rect(Game.X_BOUNDARY_1, Game.Y_BOUNDARY_2, Game.BOARD_LENGTH, Game.LINE_WIDTH)
        line_4 = pygame.Rect(Game.X_BOUNDARY_1, Game.Y_BOUNDARY_3, Game.BOARD_LENGTH, Game.LINE_WIDTH)

        pygame.display.set_caption("Tic-tac-toe")
        pygame.display.set_icon(Game.X_IMG)
        Game.WIN.fill(Game.BLACK)
        pygame.draw.rect(Game.WIN, Game.WHITE, line_1)
        pygame.draw.rect(Game.WIN, Game.WHITE, line_2)
        pygame.draw.rect(Game.WIN, Game.WHITE, line_3)
        pygame.draw.rect(Game.WIN, Game.WHITE, line_4)

        pygame.display.update()

    def run_game(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            # TODO:


def main():
    Game()


if __name__ == "__main__":
    main()