from Constants import *
import ChessGame


class Knight(object):
    """A class that represents the knight chess piece"""
    def __init__(self, color):
        self.__color = color
        self.__color_key = YELLOW
        if color == BLACK:
            self.__img = BLACK_KNIGHT_IMAGE
            self.__eaten_img = BLACK_KNIGHT_EATEN_IMG
        else:
            self.__img = WHITE_KNIGHT_IMAGE
            self.__eaten_img = WHITE_KNIGHT_EATEN_IMG

    def get_possible_moves(self, board, row, column):
        """A function that gets a board and a knight's place and returns a list of all the knight's possible moves"""
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
        """A function that gets a board and a knight's place and returns a list of all the knight's moves"""
        possible_moves = []
        if row + TWO <= NUM_COLUMNS_ROWS_INDEX and column - ONE >= FIRST_COLUMN:
            if board.get_piece(row + TWO, column - ONE) == EMPTY or board.get_piece(row + TWO, column - ONE).get_color() != self.__color:
                possible_moves.append((row + TWO, column - ONE))
        if row - ONE >= FIRST_ROW and column + TWO <= NUM_COLUMNS_ROWS_INDEX:
            if board.get_piece(row - ONE, column + TWO) == EMPTY or board.get_piece(row - ONE, column + TWO).get_color() != self.__color:
                possible_moves.append((row - ONE, column + TWO))
        if row - TWO >= FIRST_ROW and column - ONE >= FIRST_COLUMN:
            if board.get_piece(row - TWO, column - ONE) == EMPTY or board.get_piece(row - TWO, column - ONE).get_color() != self.__color:
                possible_moves.append((row - TWO, column - ONE))
        if row + TWO <= NUM_COLUMNS_ROWS_INDEX and column + ONE <= NUM_COLUMNS_ROWS_INDEX:
            if board.get_piece(row + TWO, column + ONE) == EMPTY or board.get_piece(row + TWO, column + ONE).get_color() != self.__color:
                possible_moves.append((row + TWO, column + ONE))
        if row + ONE <= NUM_COLUMNS_ROWS_INDEX and column + TWO <= NUM_COLUMNS_ROWS_INDEX:
            if board.get_piece(row + ONE, column + TWO) == EMPTY or board.get_piece(row + ONE, column + TWO).get_color() != self.__color:
                possible_moves.append((row + ONE, column + TWO))
        if row - ONE >= FIRST_ROW and column - TWO >= FIRST_COLUMN:
            if board.get_piece(row - ONE, column - TWO) == EMPTY or board.get_piece(row - ONE, column - TWO).get_color() != self.__color:
                possible_moves.append((row - ONE, column - TWO))
        if row + ONE <= NUM_COLUMNS_ROWS_INDEX and column - TWO >= FIRST_COLUMN:
            if board.get_piece(row + ONE, column - TWO) == EMPTY or board.get_piece(row + ONE, column - TWO).get_color() != self.__color:
                possible_moves.append((row + ONE, column - TWO))
        if row - TWO >= FIRST_ROW and column + ONE <= NUM_COLUMNS_ROWS_INDEX:
            if board.get_piece(row - TWO, column + ONE) == EMPTY or board.get_piece(row - TWO, column + ONE).get_color() != self.__color:
                possible_moves.append((row - TWO, column + ONE))
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
