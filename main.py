import pygame
from board.Board import Board
from engine.Engine import Minimax
import time
WIDTH = HEIGHT = 512


def main():
    alter = True
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    board = Board()
    white_minimax = Minimax(depth=3)
    black_minimax = Minimax(depth=3)

    while True:
        board.draw(screen)
        current_minimax = white_minimax if alter else black_minimax
        best_move = current_minimax.get_best_move(board, 1 if alter else -1)
        alter = not alter

        if best_move is not None:
            board = board.copy_move(best_move[0], best_move[1])

        evaluation = current_minimax.evaluate_board(board, 1)
        print(evaluation)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        


if __name__ == '__main__':
    main()