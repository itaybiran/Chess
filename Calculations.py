from Board import *
from King import *
from Constants import *
from Queen import *
from Rock import *
from Bishop import *
from Knight import *
from Pawn import *
import pygame


def switch(my_object, var1, var2):
    """A function that switches the value of a variable"""
    if my_object == var1:
        return var2
    if my_object == var2:
        return var1


def convert_mouse_to_pos(x_y):
    """A function that gets a X_Y position and returns this specific square on the board"""
    if x_y[Y_VALUE] <= FIX_Y_VALUE or x_y[Y_VALUE] >= BOARD_HEIGHT + FIX_Y_VALUE or x_y[X_VALUE] <= FIX_X_VALUE or x_y[X_VALUE] >= BOARD_WIDTH + FIX_X_VALUE:
        return OUTSIDE_OF_BOARD
    else:
        return (x_y[Y_VALUE] - FIX_Y_VALUE) // SQUARE_SIZE, (x_y[X_VALUE] - FIX_X_VALUE) // SQUARE_SIZE


def is_check(board, color):
    """A function that gets a color and returns True if there is a piece that can check its king,
    else it returns False"""
    king_row, king_column = INITIALIZE, INITIALIZE
    for row in range(FIRST_ROW, LAST_ROW):
        for column in range(FIRST_COLUMN, LAST_COLUMN):
            if type(board.get_piece(row, column)) == King and board.get_piece(row, column).get_color() == color:
                king_row, king_column = row, column
    return check_diagonal_lines(board, color, king_row, king_column) or check_straight_lines(board, color, king_row, king_column) or check_knight_moves(board, color, king_row, king_column) or check_pawn_moves(board, color, king_row, king_column) or check_king_moves(board, color, king_row, king_column)


def check_straight_lines(board, color, king_row, king_column):
    """A function that gets a color and a king's position,
     and returns True if there is a piece that can check this king in the straight lines,
     else it returns False"""
    keep_checking = True
    i = ONE
    while keep_checking:
        if king_row + i <= NUM_COLUMNS_ROWS_INDEX:
            if (type(board.get_piece(king_row + i, king_column)) == Rock or type(board.get_piece(king_row + i, king_column)) == Queen) and board.get_piece(king_row + i, king_column).get_color() != color:
                return True
            elif board.get_piece(king_row + i, king_column) != EMPTY:
                keep_checking = False
        else:
            keep_checking = False
        i += ONE
    keep_checking = True
    i = ONE
    while keep_checking:
        if king_row - i >= FIRST_ROW:
            if (type(board.get_piece(king_row - i, king_column)) == Rock or type(board.get_piece(king_row - i, king_column)) == Queen) and board.get_piece(king_row - i, king_column).get_color() != color:
                return True
            elif board.get_piece(king_row - i, king_column) != EMPTY:
                keep_checking = False
        else:
            keep_checking = False
        i += ONE
    keep_checking = True
    i = ONE
    while keep_checking:
        if king_column + i <= NUM_COLUMNS_ROWS_INDEX:
            if (type(board.get_piece(king_row, king_column + i)) == Rock or type(board.get_piece(king_row, king_column + i)) == Queen) and board.get_piece(king_row, king_column + i).get_color() != color:
                return True
            elif board.get_piece(king_row, king_column + i) != EMPTY:
                keep_checking = False
        else:
            keep_checking = False
        i += ONE
    keep_checking = True
    i = ONE
    while keep_checking:
        if king_column - i >= FIRST_COLUMN:
            if (type(board.get_piece(king_row, king_column - i)) == Rock or type(board.get_piece(king_row, king_column - i)) == Queen) and board.get_piece(king_row, king_column - i).get_color() != color:
                return True
            elif board.get_piece(king_row, king_column - i) != EMPTY:
                keep_checking = False
        else:
            keep_checking = False
        i += ONE
    return False


def check_diagonal_lines(board, color, king_row, king_column):
    """A function that gets a color and a king's position,
     and returns True if there is a piece that can check this king in the diagonal lines,
     else it returns False"""
    keep_checking = True
    i = ONE
    while keep_checking:
        if king_row + i <= NUM_COLUMNS_ROWS_INDEX and king_column + i <= NUM_COLUMNS_ROWS_INDEX:
            if (type(board.get_piece(king_row + i, king_column + i)) == Bishop or type(board.get_piece(king_row + i, king_column + i)) == Queen) and board.get_piece(king_row + i, king_column + i).get_color() != color:
                return True
            elif board.get_piece(king_row + i, king_column + i) != EMPTY:
                keep_checking = False
        else:
            keep_checking = False
        i += ONE
    keep_checking = True
    i = ONE
    while keep_checking:
        if king_row - i >= FIRST_ROW and king_column - i >= FIRST_COLUMN:
            if (type(board.get_piece(king_row - i, king_column - i)) == Bishop or type(board.get_piece(king_row - i, king_column - i)) == Queen) and board.get_piece(king_row - i, king_column - i).get_color() != color:
                return True
            elif board.get_piece(king_row - i, king_column - i) != EMPTY:
                keep_checking = False
        else:
            keep_checking = False
        i += ONE
    keep_checking = True
    i = ONE
    while keep_checking:
        if king_column + i <= NUM_COLUMNS_ROWS_INDEX and king_row - i >= FIRST_ROW:
            if (type(board.get_piece(king_row - i, king_column + i)) == Bishop or type(board.get_piece(king_row - i, king_column + i)) == Queen) and board.get_piece(king_row - i, king_column + i).get_color() != color:
                return True
            elif board.get_piece(king_row - i, king_column + i) != EMPTY:
                keep_checking = False
        else:
            keep_checking = False
        i += ONE
    keep_checking = True
    i = ONE
    while keep_checking:
        if king_column - i >= FIRST_COLUMN and king_row + i <= NUM_COLUMNS_ROWS_INDEX:
            if (type(board.get_piece(king_row + i, king_column - i)) == Bishop or type(board.get_piece(king_row + i, king_column - i)) == Queen) and board.get_piece(king_row + i, king_column - i).get_color() != color:
                return True
            elif board.get_piece(king_row + i, king_column - i) != EMPTY:
                keep_checking = False
        else:
            keep_checking = False
        i += ONE
    return False


def check_knight_moves(board, color, king_row, king_column):
    """A function that gets a color and a king's position,
     and returns True if there is a knight that can check this king,
     else it returns False"""
    if king_row + TWO <= NUM_COLUMNS_ROWS_INDEX and king_column - ONE >= FIRST_COLUMN:
        if type(board.get_piece(king_row + TWO, king_column - ONE)) == Knight and board.get_piece(king_row + TWO, king_column - ONE).get_color() != color:
            return True
    if king_row - ONE >= FIRST_ROW and king_column + TWO <= NUM_COLUMNS_ROWS_INDEX:
        if type(board.get_piece(king_row - ONE, king_column + TWO)) == Knight and board.get_piece(king_row - ONE, king_column + TWO).get_color() != color:
            return True
    if king_row - TWO >= FIRST_ROW and king_column - ONE >= FIRST_COLUMN:
        if type(board.get_piece(king_row - TWO, king_column - ONE)) == Knight and board.get_piece(king_row - TWO, king_column - ONE).get_color() != color:
            return True
    if king_row + TWO <= NUM_COLUMNS_ROWS_INDEX and king_column + ONE <= NUM_COLUMNS_ROWS_INDEX:
        if type(board.get_piece(king_row + TWO, king_column + ONE)) == Knight and board.get_piece(king_row + TWO, king_column + ONE).get_color() != color:
            return True
    if king_row + ONE <= NUM_COLUMNS_ROWS_INDEX and king_column + TWO <= NUM_COLUMNS_ROWS_INDEX:
        if type(board.get_piece(king_row + ONE, king_column + TWO)) == Knight and board.get_piece(king_row + ONE, king_column + TWO).get_color() != color:
            return True
    if king_row - ONE >= FIRST_ROW and king_column - TWO >= FIRST_COLUMN:
        if type(board.get_piece(king_row - ONE, king_column - TWO)) == Knight and board.get_piece(king_row - ONE, king_column - TWO).get_color() != color:
            return True
    if king_row + ONE <= NUM_COLUMNS_ROWS_INDEX and king_column - TWO >= FIRST_COLUMN:
        if type(board.get_piece(king_row + ONE, king_column - TWO)) == Knight and board.get_piece(king_row + ONE, king_column - TWO).get_color() != color:
            return True
    if king_row - TWO >= FIRST_ROW and king_column + ONE <= NUM_COLUMNS_ROWS_INDEX:
        if type(board.get_piece(king_row - TWO, king_column + ONE)) == Knight and board.get_piece(king_row - TWO, king_column + ONE).get_color() != color:
            return True
    return False


def check_pawn_moves(board, color, king_row, king_column):
    """A function that gets a color and a king's position,
     and returns True if there is a pawn that can check this king,
     else it returns False"""
    if color == BLACK:
        if king_row + ONE <= NUM_COLUMNS_ROWS_INDEX and king_column - ONE >= FIRST_COLUMN:
            if type(board.get_piece(king_row + ONE, king_column - ONE)) == Pawn and board.get_piece(king_row + ONE, king_column - ONE).get_color() == WHITE:
                return True
        if king_row + ONE <= NUM_COLUMNS_ROWS_INDEX and king_column + ONE <= NUM_COLUMNS_ROWS_INDEX:
            if type(board.get_piece(king_row + ONE, king_column + ONE)) == Pawn and board.get_piece(king_row + ONE, king_column + ONE).get_color() == WHITE:
                return True
    else:
        if king_row - ONE >= FIRST_ROW and king_column - ONE >= FIRST_COLUMN:
            if type(board.get_piece(king_row - ONE, king_column - ONE)) == Pawn and board.get_piece(king_row - ONE, king_column - ONE).get_color() == BLACK:
                return True
        if king_row - ONE >= FIRST_ROW and king_column + ONE <= NUM_COLUMNS_ROWS_INDEX:
            if type(board.get_piece(king_row - ONE, king_column + ONE)) == Pawn and board.get_piece(king_row - ONE, king_column + ONE).get_color() == BLACK:
                return True
    return False


def check_king_moves(board, color, king_row, king_column):
    """A function that gets a color and a king's position,
     and returns True if the other king can check this king,
     else it returns False"""
    if king_row - ONE >= FIRST_ROW and king_column - ONE >= FIRST_COLUMN:
        if type(board.get_piece(king_row - ONE, king_column - ONE)) == King and board.get_piece(king_row - ONE, king_column - ONE).get_color() != color:
            return True
    if king_row - ONE >= FIRST_ROW:
        if type(board.get_piece(king_row - ONE, king_column)) == King and board.get_piece(king_row - ONE, king_column).get_color() != color:
            return True
    if king_row - ONE >= FIRST_ROW and king_column + ONE <= NUM_COLUMNS_ROWS_INDEX:
        if type(board.get_piece(king_row - ONE, king_column + ONE)) == King and board.get_piece(king_row - ONE, king_column + ONE).get_color() != color:
            return True
    if king_column - ONE >= FIRST_COLUMN:
        if type(board.get_piece(king_row, king_column - ONE)) == King and board.get_piece(king_row, king_column - ONE).get_color() != color:
            return True
    if king_column + ONE <= NUM_COLUMNS_ROWS_INDEX:
        if type(board.get_piece(king_row, king_column + ONE)) == King and board.get_piece(king_row, king_column + ONE).get_color() != color:
            return True
    if king_row + ONE <= NUM_COLUMNS_ROWS_INDEX and king_column - ONE >= FIRST_COLUMN:
        if type(board.get_piece(king_row + ONE, king_column - ONE)) == King and board.get_piece(king_row + ONE, king_column - ONE).get_color() != color:
            return True
    if king_row + ONE <= NUM_COLUMNS_ROWS_INDEX:
        if type(board.get_piece(king_row + ONE, king_column)) == King and board.get_piece(king_row + ONE, king_column).get_color() != color:
            return True
    if king_row + ONE <= NUM_COLUMNS_ROWS_INDEX and king_column + ONE <= NUM_COLUMNS_ROWS_INDEX:
        if type(board.get_piece(king_row + ONE, king_column + ONE)) == King and board.get_piece(king_row + ONE, king_column + ONE).get_color() != color:
            return True
    return False


def can_move(board, color):
    """A function that gets a color and returns True if it has any possible move, else it returns False"""
    for row in range(FIRST_ROW, LAST_ROW):
        for column in range(FIRST_COLUMN, LAST_COLUMN):
            if board.get_piece(row, column) != EMPTY and board.get_piece(row, column).get_color() == color:
                if len(board.get_piece(row, column).get_possible_moves(board, row, column)) != ZERO:
                    return True
    return False


def is_checkmate(board, color):
    """A function that gets a color and returns True if it lost the game, else it returns False"""
    return is_check(board, color) and not can_move(board, color)


def sort_eaten_pieces_list(eaten_piece):
    """A function that gets a piece and returns its place in the eaten pieces list"""
    if type(eaten_piece) == Pawn:
        return 1
    if type(eaten_piece) == Knight:
        return 2
    if type(eaten_piece) == Bishop:
        return 3
    if type(eaten_piece) == Rock:
        return 4
    if type(eaten_piece) == Queen:
        return 5


def fix_string(num):
    """A function that fix the timer to ##:## format"""
    if num < TEN:
        num = str(ZERO) + str(num)
    return num


def wait(time):
    """A function that gets time and waits this amount of time"""
    counter = INITIALIZE
    while counter <= time:
        pygame.time.delay(ONE_MILLISECOND)
        counter += ONE_MILLISECOND
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


def display_img(image, screen):
    """A function that gets an image and displays it on the screen"""
    img = pygame.image.load(image).convert()
    screen.blit(img, (TOP_LEFT_CORNER, TOP_LEFT_CORNER))
    pygame.display.flip()
