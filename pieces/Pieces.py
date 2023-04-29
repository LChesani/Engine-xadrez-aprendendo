

class PieceType():
    PAWN = 1.0
    ROOK = 5.0
    KNIGHT = 3.0
    BISHOP = 3.25
    QUEEN = 9.0
    KING = 999

class Posicao():
    def __init__(self, _x, _y):
        self.x = _x;
        self.y = _y;

class Piece:
    def __init__(self, color: int, pos : Posicao):
        self.pos = pos
        self.color = color
        self.has_moved = False

    def move(self, _pos : Posicao, board):
        if self.possible(_pos, board):
            self.pos = _pos
        self.has_moved = True


    

class Pawn(Piece):
    def __init__(self, color: int, pos : Posicao):
        super().__init__(color, pos)
        self.has_moved = False
        self.idx = PieceType.PAWN * color


    def possible(self, new : Posicao, board):
        if (abs((new.y - self.pos.y)) == 1) and ((new.x - self.pos.x)*self.color == -1) and ((board.board[new.x][new.y] != 0) and (board.board[new.x][new.y].color != self.color)):                                          
            return True;
        if not self.has_moved: #primeiro movimento
            diff = (new.x - self.pos.x)*self.color
            if (new.y == self.pos.y) and diff >= -2 and diff < 0 and board.board[new.x][new.y] == 0:
                if diff == -2 and board.board[new.x-1][new.y-1] != 0:
                    return False;
                return True;
        else:
            diff = (new.x - self.pos.x)*self.color
            if (new.y == self.pos.y) and (diff == -1) and (board.board[new.x][new.y] == 0):
                return True;
        
        return False;


class Rook(Piece):
    def __init__(self, color: int, pos: Posicao):
        super().__init__(color, pos)
        self.idx = PieceType.ROOK * color

    def possible(self, new: Posicao, board):
        if (board.board[new.x][new.y] == 0) or board.board[new.x][new.y].idx * self.color < 0:
            if new.x == self.pos.x:  # Movimento vertical
                step = 1 if new.y > self.pos.y else -1
                for y in range(self.pos.y + step, new.y, step):
                    if board.board[self.pos.x][y] != 0:
                        return False
                return True
            elif new.y == self.pos.y:  # Movimento horizontal
                step = 1 if new.x > self.pos.x else -1
                for x in range(self.pos.x + step, new.x, step):
                    if board.board[x][self.pos.y] != 0:
                        return False
                return True
        return False






class Knight(Piece):
    def __init__(self, color: int, pos : Posicao):
        super().__init__(color, pos)
        self.idx = PieceType.KNIGHT * color

    def possible(self, new : Posicao, board):
        x, y = self.pos.x, self.pos.y

        if abs(new.x - x) == 2 and abs(new.y - y) == 1:
            return board.board[new.x][new.y] == 0 or board.board[new.x][new.y].idx * self.color < 0
        elif abs(new.x - x) == 1 and abs(new.y - y) == 2:
            return board.board[new.x][new.y] == 0 or board.board[new.x][new.y].idx * self.color < 0
        else:
            return False




class Bishop(Piece):
    def __init__(self, color: int, pos: Posicao):
        super().__init__(color, pos)
        self.idx = PieceType.BISHOP * color
    
    def possible(self, new: Posicao, board):
        if (board.board[new.x][new.y] == 0) or board.board[new.x][new.y].idx * self.color < 0:
            if abs(new.x - self.pos.x) == abs(new.y - self.pos.y):
                incx = 1 if new.x > self.pos.x else -1
                incy = 1 if new.y > self.pos.y else -1
                x = self.pos.x + incx
                y = self.pos.y + incy
                while x != new.x and y != new.y:
                    if board.board[x][y] != 0:
                        return False
                    x += incx
                    y += incy
                return True
        return False



class Queen(Piece):
    def __init__(self, color: int, pos : Posicao):
        super().__init__(color, pos)
        self.idx = PieceType.QUEEN * color


    def possible(self, new: Posicao, board):
        if (board.board[new.x][new.y] == 0) or board.board[new.x][new.y].idx * self.color < 0:
            if new.x == self.pos.x:
                # Movimento horizontal
                if new.y > self.pos.y:
                    for y in range(self.pos.y + 1, new.y):
                        if board.board[self.pos.x][y] != 0:
                            return False
                    return True
                elif new.y < self.pos.y:
                    for y in range(new.y + 1, self.pos.y):
                        if board.board[self.pos.x][y] != 0:
                            return False
                    return True
            elif new.y == self.pos.y:
                # Movimento vertical
                if new.x > self.pos.x:
                    for x in range(self.pos.x + 1, new.x):
                        if board.board[x][self.pos.y] != 0:
                            return False
                    return True
                elif new.x < self.pos.x:
                    for x in range(new.x + 1, self.pos.x):
                        if board.board[x][self.pos.y] != 0:
                            return False
                    return True
            elif abs(new.x - self.pos.x) == abs(new.y - self.pos.y):
                # Movimento diagonal
                x_dir = 1 if new.x > self.pos.x else -1
                y_dir = 1 if new.y > self.pos.y else -1
                x, y = self.pos.x + x_dir, self.pos.y + y_dir
                while x != new.x and y != new.y:
                    if board.board[x][y] != 0:
                        return False
                    x += x_dir
                    y += y_dir
                return True
        return False



class King(Piece):
    def __init__(self, color: int, pos : Posicao):
        super().__init__(color, pos)
        self.idx = PieceType.KING * color


    def possible(self, new : Posicao, board):
        dx = abs(new.x - self.pos.x)
        dy = abs(new.y - self.pos.y)
        
        if (dx == 0 and dy == 1) or (dx == 1 and dy == 0) or (dx == 1 and dy == 1):
            if board.board[new.x][new.y] == 0 or board.board[new.x][new.y].color != self.color:
                return True
        
        return False
