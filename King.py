from Constants import *
import ChessGame
from Rock import *


class King(object):
    """A class that represents the king chess piece"""
    def __init__(self, color):
        self.__color = color
        self.__color_key = YELLOW
        self.__is_moved = False
        if color == BLACK:
            self.__img = BLACK_KING_IMAGE
        else:
            self.__img = WHITE_KING_IMAGE

    def get_possible_moves(self, board, row, column):
        """A function that gets a board and a king's place and returns a list of all the king's possible moves"""
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
        """A function that gets a board and a king's place and returns a list of all the king's moves"""
        possible_moves = []
        if row - ONE >= FIRST_ROW and column - ONE >= FIRST_COLUMN:
            if board.get_piece(row - ONE, column - ONE) == EMPTY or board.get_piece(row - ONE, column - ONE).get_color() != self.__color:
                possible_moves.append((row - ONE, column - ONE))
        if row - ONE >= FIRST_ROW:
            if board.get_piece(row - ONE, column) == EMPTY or board.get_piece(row - ONE, column).get_color() != self.__color:
                possible_moves.append((row - ONE, column))
        if row - ONE >= FIRST_ROW and column + ONE <= NUM_COLUMNS_ROWS_INDEX:
            if board.get_piece(row - ONE, column + ONE) == EMPTY or board.get_piece(row - ONE, column + ONE).get_color() != self.__color:
                possible_moves.append((row - ONE, column + ONE))
        if column - ONE >= FIRST_COLUMN:
            if board.get_piece(row, column - ONE) == EMPTY or board.get_piece(row, column - ONE).get_color() != self.__color:
                possible_moves.append((row, column - ONE))
        if column + ONE <= NUM_COLUMNS_ROWS_INDEX:
            if board.get_piece(row, column + ONE) == EMPTY or board.get_piece(row, column + ONE).get_color() != self.__color:
                possible_moves.append((row, column + ONE))
        if row + ONE <= NUM_COLUMNS_ROWS_INDEX and column - ONE >= FIRST_COLUMN:
            if board.get_piece(row + ONE, column - ONE) == EMPTY or board.get_piece(row + ONE, column - ONE).get_color() != self.__color:
                possible_moves.append((row + ONE, column - ONE))
        if row + ONE <= NUM_COLUMNS_ROWS_INDEX:
            if board.get_piece(row + ONE, column) == EMPTY or board.get_piece(row + ONE, column).get_color() != self.__color:
                possible_moves.append((row + ONE, column))
        if row + ONE <= NUM_COLUMNS_ROWS_INDEX and column + ONE <= NUM_COLUMNS_ROWS_INDEX:
            if board.get_piece(row + ONE, column + ONE) == EMPTY or board.get_piece(row + ONE, column + ONE).get_color() != self.__color:
                possible_moves.append((row + ONE, column + ONE))
        if self.big_castle(board, row, column):
            possible_moves.append((row, TWO))
        if self.small_castle(board, row, column):
            possible_moves.append((row, LAST_COLUMN_INDEX - ONE))
        return possible_moves

    def big_castle(self, board, row, column):
        """A function that returns True if a big castle can be made, else it returns False"""
        if not self.__is_moved:
            if type(board.get_piece(row, FIRST_COLUMN)) == Rock and board.get_piece(row, FIRST_COLUMN).get_color() == self.__color:
                for i in range(ONE, PLACES_BIG_CASTLE):
                    if board.get_piece(row, column - i) != EMPTY or ChessGame.check_diagonal_lines(board, self.__color, row, column - i) or ChessGame.check_straight_lines(board, self.__color, row, column - i) or ChessGame.check_knight_moves(board, self.__color, row, column - i) or ChessGame.check_pawn_moves(board, self.__color, row, column - i):
                        return False
                if ChessGame.check_diagonal_lines(board, self.__color, row, column) or ChessGame.check_straight_lines(board, self.__color, row, column) or ChessGame.check_knight_moves(board, self.__color, row, column) or ChessGame.check_pawn_moves(board, self.__color, row, column):
                    return False
            else:
                return False
        else:
            return False
        return True

    def small_castle(self, board, row, column):
        """A function that returns True if a small castle can be made, else it returns False"""
        if not self.__is_moved:
            if type(board.get_piece(row, LAST_COLUMN_INDEX)) == Rock and board.get_piece(row, LAST_COLUMN_INDEX).get_color() == self.__color:
                for i in range(ONE, PLACES_SMALL_CASTLE):
                    if board.get_piece(row, column + i) != EMPTY or ChessGame.check_diagonal_lines(board, self.__color, row, column + i) or ChessGame.check_straight_lines(board, self.__color, row, column + i) or ChessGame.check_knight_moves(board, self.__color, row, column + i) or ChessGame.check_pawn_moves(board, self.__color, row, column + i):
                        return False
                if ChessGame.check_diagonal_lines(board, self.__color, row, column) or ChessGame.check_straight_lines(board, self.__color, row, column) or ChessGame.check_knight_moves(board, self.__color, row, column) or ChessGame.check_pawn_moves(board, self.__color, row, column):
                    return False
            else:
                return False
        else:
            return False
        return True

    def get_color(self):
        """Gets color"""
        return self.__color

    def get_img(self):
        """Gets img"""
        return self.__img

    def get_is_moved(self):
        """Gets is_moved"""
        return self.__is_moved

    def get_color_key(self):
        """Gets color_key"""
        return self.__color_key

    def set_color_key(self, color_key):
        """Sets color_key"""
        self.__color_key = color_key

    def moved(self):
        """Sets is_moved to True"""
        self.__is_moved = True
