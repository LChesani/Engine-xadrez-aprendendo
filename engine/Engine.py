from board.Board import Board
import random
from functools import lru_cache
import copy
from pieces.Pieces import *


class Minimax:

    def __init__(self, depth):
        self.depth = depth

    def get_best_move(self, board, color):
        best_move = self.minimax(board, self.depth, color, -float('inf'), float('inf'), True)
        if best_move[1] is not None:
            start_pos = best_move[1][0]
            end_pos = best_move[1][1]
            return start_pos, end_pos


    @lru_cache(maxsize=None)
    def evaluate_board(self, board, color):
        score = 0

        for i in range(8):
            for j in range(8):
                piece = board.board[i][j]
                if piece == 0:
                    continue

                bonus = 0
                if abs(piece.idx) < 10:
                    bonus = color*(10-abs(piece.idx))/(abs(piece.pos.x - 3.5)*0.55 + abs(piece.pos.y - 3.5)*0.45)/75
                score += piece.idx + bonus
        return score*color

                
    @lru_cache(maxsize=None)
    def get_all_moves(self, color, board):
        moves = []
        for i in range(8):
            for j in range(8):
                piece = board.board[i][j]
                if isinstance(piece, Piece) and piece.color == color:
                    for i2 in range(8):
                        for j2 in range(8):
                            if piece.possible(Posicao(i2, j2), board):
                                temp_board = board.copy_move(Posicao(i, j), Posicao(i2, j2)) # criando cópia temporária do tabuleiro
                                if not temp_board.is_check(color): # verificando se o rei fica em xeque após o movimento
                                    moves.append((Posicao(i, j), Posicao(i2, j2)))
        return moves


    @lru_cache(maxsize=None)
    def minimax(self, board, depth, color, alpha, beta, maximizing_player):
        if depth == 0:
            return self.evaluate_board(board, color), None

        if maximizing_player:
            best_move = None
            max_eval = -float('inf')
            for piece, move in self.get_all_moves(color, board):
                new_board = board.copy_move(piece, move)
                eval = self.minimax(new_board, depth - 1, color, alpha, beta, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (piece, move)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move

        else:
            best_move = None
            min_eval = float('inf')
            for piece, move in self.get_all_moves(-color, board):
                new_board = board.copy_move(piece, move)
                eval = self.minimax(new_board, depth - 1, color, alpha, beta, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (piece, move)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move
