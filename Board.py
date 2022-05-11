from Constants import *
from Pawn import *
from Knight import *
from Bishop import *
from Rock import *
from Queen import *
from King import *
from Calculations import is_check, switch


class Board(object):
    """A class that represents the chess board"""
    def __init__(self):
        self.__board = [
            [Rock(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK), King(BLACK), Bishop(BLACK), Knight(BLACK), Rock(BLACK)],
            [Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)],
            [Rock(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE), King(WHITE), Bishop(WHITE), Knight(WHITE), Rock(WHITE)]]

    def get_piece(self, row, column):
        """A function that gets a row and a column and returns this piece"""
        return self.__board[row][column]

    def set_piece(self, piece, row, column):
        """A function that gets a row, a column and a piece and puts the piece in that place"""
        self.__board[row][column] = piece

    def get_string_of_move(self, row1, column1, row2, column2):
        """A function that gets a move and returns its chess notation"""
        abbreviations_for_each_piece = {King: KING_ABBREVIATION, Queen: QUEEN_ABBREVIATION, Bishop: BISHOP_ABBREVIATION,
                                        Knight: KNIGHT_ABBREVIATION, Rock: ROCK_ABBREVIATION, Pawn: PAWN_ABBREVIATION}
        square = chr(column2 + ord(FIRST_COLUMN_LETTER)) + str(LAST_ROW - row2)
        piece_abbreviation = abbreviations_for_each_piece[type(self.get_piece(row1, column1))]
        if type(self.get_piece(row2, column2)) != type(EMPTY):
            move = piece_abbreviation + self.get_removing_ambiguity_char(row1, column1, row2, column2) + EAT_SIGN + square
            if type(self.get_piece(row1, column1)) == Pawn:
                move = chr(column1 + ord(FIRST_COLUMN_LETTER)) + move
        else:
            move = piece_abbreviation + self.get_removing_ambiguity_char(row1, column1, row2, column2) + square
        return move

    def get_removing_ambiguity_char(self, row1, column1, row2, column2):
        """A function that returns a char to remove ambiguity in the move notation"""
        column_char = False
        row_char = False
        final_char = NOTHING
        if type(self.get_piece(row1, column1)) == Pawn:
            return NOTHING
        for row in range(INITIALIZE, LAST_ROW):
            for column in range(INITIALIZE, LAST_COLUMN):
                if not (row1 == row and column1 == column):
                    if type(self.get_piece(row, column)) == type(self.get_piece(row1, column1)) and self.get_piece(row1, column1).get_color() == self.get_piece(row, column).get_color():
                        if (row2, column2) in self.get_piece(row, column).get_moves(self, row, column):
                            if row1 == row:
                                column_char = True
                            if column1 == column:
                                row_char = True
        if column_char:
            final_char += chr(column1 + ord(FIRST_COLUMN_LETTER))
        if row_char:
            final_char += str(LAST_ROW - row1)
        return final_char

    def move_piece(self, row1, column1, row2, column2):
        """A function that moves a piece and returns the move notation"""
        color_of_piece = self.get_piece(row1, column1).get_color()
        move_in_string_format = self.get_string_of_move(row1, column1, row2, column2)
        self.set_piece(self.get_piece(row1, column1), row2, column2)
        self.__board[row1][column1] = EMPTY
        if is_check(self, switch(color_of_piece, WHITE, BLACK)):
            move_in_string_format += CHECK_SIGN
        return move_in_string_format

    def turn(self):
        """A function that turns the board"""
        self.__board.reverse()
