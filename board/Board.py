import pygame
from config import *
from pieces.Pieces import *
import copy
import os
class Board:
    def __init__(self, _board=None):
        if _board is None:
            self.board = [  [Rook(-1, Posicao(0, 0)), Knight(-1, Posicao(0, 1)), Bishop(-1, Posicao(0, 2)), Queen(-1, Posicao(0, 3)), King(-1, Posicao(0, 4)), Bishop(-1, Posicao(0, 5)), Knight(-1, Posicao(0, 6)), Rook(-1, Posicao(0, 7))],
                            [Pawn(-1, Posicao(1, i)) for i in range(8)],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [Pawn(1, Posicao(6, i)) for i in range(8)],
                            [Rook(1, Posicao(7, 0)), Knight(1, Posicao(7, 1)), Bishop(1, Posicao(7, 2)), Queen(1, Posicao(7, 3)), King(1, Posicao(7, 4)), Bishop(1, Posicao(7, 5)), Knight(1, Posicao(7, 6)), Rook(1, Posicao(7, 7))]
                        ]
        else:
            self.board = _board

    def copy_move(self, prev : Posicao, nxt : Posicao): 
        n = copy.deepcopy(self.board)
        n[nxt.x][nxt.y] = n[prev.x][prev.y]
        n[nxt.x][nxt.y].move(nxt, self)
        n[prev.x][prev.y] = 0
        cpy = copy.deepcopy(self)
        cpy.board = n;
        return cpy;





    def is_check(self, color):
            # Encontra a posição do rei do jogador em questão
            for i in range(8):
                for j in range(8):
                    piece = self.board[i][j]
                    if isinstance(piece, King) and piece.color == color:
                        king_pos = Posicao(i, j)
                        break

            # Verifica se alguma peça adversária pode atacar o rei
            for i in range(8):
                for j in range(8):
                    piece = self.board[i][j]
                    if isinstance(piece, Piece) and piece.color == -color:
                        if piece.possible(king_pos, self):
                            return True

            return False

    def drawPieces(self, display, x, y, i, j):
        if self.board[i][j].idx == -5.0:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'blackRook.png')), (64, 64)), (x, y));
        if self.board[i][j].idx == 5.0:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'whiteRook.png')), (64, 64)), (x, y));
        if self.board[i][j].idx == -3.0:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'blackKnight.png')), (64, 64)), (x, y));
        if self.board[i][j].idx == 3.0:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'whiteKnight.png')), (64, 64)), (x, y));
        if self.board[i][j].idx == -3.25:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'blackBishop.png')), (64, 64)), (x, y));
        if self.board[i][j].idx == 3.25:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'whiteBishop.png')), (64, 64)), (x, y));
        if self.board[i][j].idx == -9.0:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'blackQueen.png')), (64, 64)), (x, y));
        if self.board[i][j].idx == 9:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'whiteQueen.png')), (64, 64)), (x, y));
        if self.board[i][j].idx == -999:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'blackKing.png')), (64, 64)), (x, y));
        if self.board[i][j].idx == 999:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'whiteKing.png')), (64, 64)), (x, y));
        if self.board[i][j].idx == -1:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'blackPawn.png')), (64, 64)), (x, y));
        if self.board[i][j].idx == 1:
            display.blit(pygame.transform.scale(pygame.image.load(os.path.join('pieces', 'whitePawn.png')), (64, 64)), (x, y));

    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                x = col * SIZE
                y = row * SIZE

                if (row + col) % 2 == 0:
                    color = (255, 255, 255)
                else:
                    color = (100, 100, 100)

                pygame.draw.rect(screen, color, pygame.Rect(x, y, SIZE, SIZE))

                # verifica se há uma peça na posição atual
                if self.board[row][col] != 0:
                    # usa o índice da peça para obter a imagem correspondente
                    self.drawPieces(screen, x, y, row, col)

        pygame.display.flip()



    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.draw_board(screen)
        pygame.display.flip()