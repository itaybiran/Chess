from Constants import *
import ChessGame


class Pawn(object):
    """A class that represents the pawn chess piece"""
    def __init__(self, color):
        self.__color = color
        self.__color_key = YELLOW
        self.__is_moved = False
        if color == BLACK:
            self.__img = BLACK_PAWN_IMAGE
            self.__eaten_img = BLACK_PAWN_EATEN_IMG
        else:
            self.__img = WHITE_PAWN_IMAGE
            self.__eaten_img = WHITE_PAWN_EATEN_IMG

    def get_possible_moves(self, board, row, column):
        """A function that gets a board and a pawn's place and returns a list of all the pawn's possible moves"""
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
        """A function that gets a board and a pawn's place and returns a list of all the pawn's moves"""
        possible_moves = []
        if self.__color == WHITE:
            if self.__is_moved:
                if row - ONE >= FIRST_ROW:
                    if board.get_piece(row - ONE, column) == EMPTY:
                        possible_moves.append((row - ONE, column))
            else:
                if row - TWO >= FIRST_ROW:
                    if board.get_piece(row - TWO, column) == EMPTY and board.get_piece(row - ONE, column) == EMPTY:
                        possible_moves.append((row - TWO, column))
                if row - ONE >= FIRST_ROW:
                    if board.get_piece(row - ONE, column) == EMPTY:
                        possible_moves.append((row - ONE, column))
            if row - ONE >= FIRST_ROW:
                if column - ONE >= FIRST_COLUMN:
                    if board.get_piece(row - ONE, column - ONE) != EMPTY and board.get_piece(row - ONE, column - ONE).get_color() != self.__color:
                        possible_moves.append((row - ONE, column - ONE))
                if column + ONE <= NUM_COLUMNS_ROWS_INDEX:
                    if board.get_piece(row - ONE, column + ONE) != EMPTY and board.get_piece(row - ONE, column + ONE).get_color() != self.__color:
                        possible_moves.append((row - ONE, column + ONE))
        else:
            if self.__is_moved:
                if row + ONE <= NUM_COLUMNS_ROWS_INDEX:
                    if board.get_piece(row + ONE, column) == EMPTY:
                        possible_moves.append((row + ONE, column))
            else:
                if row + TWO <= NUM_COLUMNS_ROWS_INDEX:
                    if board.get_piece(row + TWO, column) == EMPTY and board.get_piece(row + ONE, column) == EMPTY:
                        possible_moves.append((row + TWO, column))
                if row + ONE <= NUM_COLUMNS_ROWS_INDEX:
                    if board.get_piece(row + ONE, column) == EMPTY:
                        possible_moves.append((row + ONE, column))
            if row + ONE <= NUM_COLUMNS_ROWS_INDEX:
                if column - ONE >= FIRST_COLUMN:
                    if board.get_piece(row + ONE, column - ONE) != EMPTY and board.get_piece(row + ONE, column - ONE).get_color() != self.__color:
                        possible_moves.append((row + ONE, column - ONE))
                if column + ONE <= NUM_COLUMNS_ROWS_INDEX:
                    if board.get_piece(row + ONE, column + ONE) != EMPTY and board.get_piece(row + ONE, column + ONE).get_color() != self.__color:
                        possible_moves.append((row + ONE, column + ONE))
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

    def set_is_moved(self, is_moved):
        """Sets is_moved"""
        self.__is_moved = is_moved
