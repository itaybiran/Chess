from Constants import *
import ChessGame


class Bishop(object):
    """A class that represents the bishop chess piece"""
    def __init__(self, color):
        self.__color = color
        self.__color_key = YELLOW
        if color == BLACK:
            self.__img = BLACK_BISHOP_IMAGE
            self.__eaten_img = BLACK_BISHOP_EATEN_IMG
        else:
            self.__img = WHITE_BISHOP_IMAGE
            self.__eaten_img = WHITE_BISHOP_EATEN_IMG

    def get_possible_moves(self, board, row, column):
        """A function that gets a board and a bishop's place and returns a list of all the bishop's possible moves"""
        possible_moves = []
        for move in self.get_moves(board, row, column):
            p1 = board.get_piece(row, column)
            p2 = board.get_piece(move[ROW], move[COLUMN])
            board.move_piece(row, column, move[ROW], move[COLUMN])
            if not ChessGame.is_check(board, self.__color):
                possible_moves.append(move)
            board.set_piece(p1, row, column)
            board.set_piece(p2, move[ROW], move[COLUMN])
        return possible_moves

    def get_moves(self, board, row, column):
        """A function that gets a board and a bishop's place and returns a list of all the bishop's moves"""
        possible_moves = []
        keep_checking = True
        i = ONE
        while keep_checking:
            if row + i <= NUM_COLUMNS_ROWS_INDEX and column + i <= NUM_COLUMNS_ROWS_INDEX:
                if board.get_piece(row + i, column + i) == EMPTY:
                    possible_moves.append((row + i, column + i))
                elif board.get_piece(row + i, column + i).get_color() != self.__color:
                    possible_moves.append((row + i, column + i))
                    keep_checking = False
                else:
                    keep_checking = False
            else:
                keep_checking = False
            i += ONE
        keep_checking = True
        i = ONE
        while keep_checking:
            if row - i >= FIRST_ROW and column - i >= FIRST_COLUMN:
                if board.get_piece(row - i, column - i) == EMPTY:
                    possible_moves.append((row - i, column - i))
                elif board.get_piece(row - i, column - i).get_color() != self.__color:
                    possible_moves.append((row - i, column - i))
                    keep_checking = False
                else:
                    keep_checking = False
            else:
                keep_checking = False
            i += ONE
        keep_checking = True
        i = ONE
        while keep_checking:
            if column + i <= NUM_COLUMNS_ROWS_INDEX and row - i >= FIRST_ROW:
                if board.get_piece(row - i, column + i) == EMPTY:
                    possible_moves.append((row - i, column + i))
                elif board.get_piece(row - i, column + i).get_color() != self.__color:
                    possible_moves.append((row - i, column + i))
                    keep_checking = False
                else:
                    keep_checking = False
            else:
                keep_checking = False
            i += ONE
        keep_checking = True
        i = ONE
        while keep_checking:
            if column - i >= FIRST_COLUMN and row + i <= NUM_COLUMNS_ROWS_INDEX:
                if board.get_piece(row + i, column - i) == EMPTY:
                    possible_moves.append((row + i, column - i))
                elif board.get_piece(row + i, column - i).get_color() != self.__color:
                    possible_moves.append((row + i, column - i))
                    keep_checking = False
                else:
                    keep_checking = False
            else:
                keep_checking = False
            i += ONE
        return possible_moves

    def get_color(self):
        """Gets color"""
        return self.__color

    def get_img(self):
        """Gets img"""
        return self.__img

    def get_eaten_img(self):
        """Gets eaten_img"""
        return self.__eaten_img

    def get_color_key(self):
        """Gets color_key"""
        return self.__color_key

    def set_color_key(self, color_key):
        """Sets color_key"""
        self.__color_key = color_key

