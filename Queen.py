from Rock import *
from Bishop import *
import ChessGame


class Queen(object):
    """A class that represents the queen chess piece"""
    def __init__(self, color):
        self.__color = color
        self.__color_key = YELLOW
        if color == BLACK:
            self.__img = BLACK_QUEEN_IMAGE
            self.__eaten_img = BLACK_QUEEN_EATEN_IMG
        else:
            self.__img = WHITE_QUEEN_IMAGE
            self.__eaten_img = WHITE_QUEEN_EATEN_IMG

    def get_possible_moves(self, board, row, column):
        """A function that gets a board and a queen's place and returns a list of all the queen's possible moves"""
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
        """A function that gets a board and a queen's place and returns a list of all the queen's moves"""
        possible_moves = []
        board.set_piece(Rock(self.__color), row, column)
        for move in board.get_piece(row, column).get_possible_moves(board, row, column):
            possible_moves.append(move)
        board.set_piece(Bishop(self.__color), row, column)
        for move in board.get_piece(row, column).get_possible_moves(board, row, column):
            possible_moves.append(move)
        board.set_piece(Queen(self.__color), row, column)
        return possible_moves

    def get_img(self):
        """Gets img"""
        return self.__img

    def get_color(self):
        """Gets color"""
        return self.__color

    def get_eaten_img(self):
        """Gets eaten_img"""
        return self.__eaten_img

    def get_color_key(self):
        """Gets color_key"""
        return self.__color_key

    def set_color_key(self, color_key):
        """Sets color_key"""
        self.__color_key = color_key
