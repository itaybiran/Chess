import pygame
from Board import *
from King import *
from Paint import *
from Constants import *
from Calculations import *


class ChessGame(object):
    """A class that represents one chess game"""
    def __init__(self, screen, time):
        self.__time = time
        self.__board = Board()
        self.__paint = Paint(screen)
        self.__mouse_pos_list = []
        self.__eaten_pieces = []
        self.__white_moves = []
        self.__black_moves = []
        self.__player_turn_color = WHITE
        self.__winner = NOBODY
        self.__paint.draw_chess_board()
        self.__paint.draw_chess_pieces(self.__board)
        ticks = self.__time.get_current_time()

        while self.__winner == NOBODY:
            self.__paint.draw_clocks(self.__time, self.__player_turn_color)
            time_passed = pygame.time.get_ticks() - ticks
            ticks = pygame.time.get_ticks()
            self.__time.update_timer(self.__player_turn_color, time_passed)
            self.check_winner_by_time_over()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                    if convert_mouse_to_pos(pygame.mouse.get_pos()) != OUTSIDE_OF_BOARD:
                        self.__mouse_pos_list.append(convert_mouse_to_pos(pygame.mouse.get_pos()))
                        self.handle_input()
            self.__paint.draw_chess_pieces(self.__board)
        self.__paint.draw_winner(self.__winner)
        check_x_pressed()

    def handle_input(self):
        """A function that handles all the mouse's clicks on the board"""
        if len(self.__mouse_pos_list) == ONE_PRESS:
            if self.__board.get_piece(self.__mouse_pos_list[FIRST_PRESS][ROW], self.__mouse_pos_list[FIRST_PRESS][COLUMN]) != EMPTY and self.__board.get_piece(self.__mouse_pos_list[FIRST_PRESS][ROW], self.__mouse_pos_list[FIRST_PRESS][COLUMN]).get_color() is self.__player_turn_color:
                self.__paint.draw_color_of_chosen_piece(self.__mouse_pos_list[FIRST_PRESS][ROW], self.__mouse_pos_list[FIRST_PRESS][COLUMN])
                possible_moves = self.__board.get_piece(self.__mouse_pos_list[FIRST_PRESS][ROW], self.__mouse_pos_list[FIRST_PRESS][COLUMN]).get_possible_moves(self.__board, self.__mouse_pos_list[FIRST_PRESS][ROW], self.__mouse_pos_list[FIRST_PRESS][COLUMN])
                self.__paint.draw_options_to_move(possible_moves, self.__board)
            else:
                self.__mouse_pos_list.clear()
        elif len(self.__mouse_pos_list) == TWO_PRESS:
            possible_moves = self.__board.get_piece(self.__mouse_pos_list[FIRST_PRESS][ROW], self.__mouse_pos_list[FIRST_PRESS][COLUMN]).get_possible_moves(self.__board, self.__mouse_pos_list[FIRST_PRESS][ROW], self.__mouse_pos_list[FIRST_PRESS][COLUMN])
            if self.__mouse_pos_list[SECOND_PRESS] in possible_moves:
                if not self.is_castle(self.__mouse_pos_list[FIRST_PRESS][ROW], self.__mouse_pos_list[FIRST_PRESS][COLUMN], self.__mouse_pos_list[SECOND_PRESS][ROW], self.__mouse_pos_list[SECOND_PRESS][COLUMN]):
                    if self.__board.get_piece(self.__mouse_pos_list[SECOND_PRESS][ROW], self.__mouse_pos_list[SECOND_PRESS][COLUMN]) != EMPTY:
                        self.__eaten_pieces.append(self.__board.get_piece(self.__mouse_pos_list[SECOND_PRESS][ROW], self.__mouse_pos_list[SECOND_PRESS][COLUMN]))
                        self.__eaten_pieces.sort(key=lambda x: sort_eaten_pieces_list(x))
                        sound = PIECE_EAT_SOUND
                    else:
                        sound = PIECE_MOVED_SOUND
                    self.add_move_to_list_moves(self.__board.move_piece(self.__mouse_pos_list[FIRST_PRESS][ROW], self.__mouse_pos_list[FIRST_PRESS][COLUMN], self.__mouse_pos_list[SECOND_PRESS][ROW], self.__mouse_pos_list[SECOND_PRESS][COLUMN]))
                    self.update_piece_status(self.__mouse_pos_list[SECOND_PRESS][ROW], self.__mouse_pos_list[SECOND_PRESS][COLUMN])
                else:
                    sound = PIECE_MOVED_SOUND
                    self.perform_castle(self.__mouse_pos_list[FIRST_PRESS][ROW], self.__mouse_pos_list[FIRST_PRESS][COLUMN], self.__mouse_pos_list[SECOND_PRESS][ROW], self.__mouse_pos_list[SECOND_PRESS][COLUMN])
                self.__mouse_pos_list.clear()
                self.__paint.draw_chess_board()
                self.__paint.draw_chess_pieces(self.__board)
                self.__paint.draw_eaten_pieces(self.__eaten_pieces)
                pygame.mixer.Sound(sound).play()
                self.__time.add_time_to_timer(self.__player_turn_color)
                self.__player_turn_color = switch(self.__player_turn_color, WHITE, BLACK)
                self.check_the_winner()
                self.__paint.draw_moves(self.__white_moves, self.__black_moves)
            else:
                self.__mouse_pos_list.clear()
                self.__paint.draw_chess_board()
                self.__paint.draw_eaten_pieces(self.__eaten_pieces)
                self.__paint.draw_moves(self.__white_moves, self.__black_moves)

    def update_piece_status(self, row, column):
        """A function that gets a piece and updates its status if it is needed"""
        if type(self.__board.get_piece(row, column)) == Pawn:
            self.__board.get_piece(row, column).set_is_moved(True)
            if self.__board.get_piece(row, column).get_color() == WHITE and row == FIRST_ROW_INDEX:
                self.__board.set_piece(Queen(WHITE), row, column)
                self.__white_moves[len(self.__white_moves) - ONE] += PAWN_PROMOTION_SIGN
                if is_check(self.__board, switch(self.__player_turn_color, BLACK, WHITE)):
                    self.__white_moves[len(self.__white_moves) - ONE] += CHECK_SIGN
            if self.__board.get_piece(row, column).get_color() == BLACK and row == LAST_ROW_INDEX:
                self.__board.set_piece(Queen(BLACK), row, column)
                self.__black_moves[len(self.__black_moves) - ONE] += PAWN_PROMOTION_SIGN
                if is_check(self.__board, switch(self.__player_turn_color, BLACK, WHITE)):
                    self.__black_moves[len(self.__black_moves) - ONE] += CHECK_SIGN
        if type(self.__board.get_piece(row, column)) == King:
            self.__board.get_piece(row, column).moved()

    def is_castle(self, row1, column1, row2, column2):
        """A function that gets a move and returns True if it is castle, else it returns False"""
        if column2 == TWO:
            if self.__board.get_piece(row2, column2) == EMPTY:
                if self.__board.get_piece(row1, column1) != EMPTY and self.__board.get_piece(row2, column2 - TWO) != EMPTY:
                    if self.__board.get_piece(row1, column1).get_color() == self.__board.get_piece(row2, column2 - TWO).get_color():
                        if type(self.__board.get_piece(row1, column1)) == King and type(self.__board.get_piece(row2, column2 - TWO)) == Rock:
                            if not self.__board.get_piece(row1, column1).get_is_moved():
                                return True
        if column2 == NUM_COLUMNS_ROWS_INDEX - ONE:
            if self.__board.get_piece(row2, column2) == EMPTY:
                if self.__board.get_piece(row1, column1) != EMPTY and self.__board.get_piece(row2, column2 + ONE) != EMPTY:
                    if self.__board.get_piece(row1, column1).get_color() == self.__board.get_piece(row2, column2 + ONE).get_color():
                        if type(self.__board.get_piece(row1, column1)) == King and type(self.__board.get_piece(row2, column2 + ONE)) == Rock:
                            if not self.__board.get_piece(row1, column1).get_is_moved():
                                return True
        return False

    def perform_castle(self, row1, column1, row2, column2):
        """A function that performs castle"""
        if column2 == TWO:
            self.__board.move_piece(row1, column1, row1, column1 - TWO)
            self.__board.move_piece(row2, column2 - TWO, row2, column2 + ONE)
            self.update_piece_status(row1, column1 - TWO)
            self.add_move_to_list_moves(CASTLING_QUEEN_SIDE)
        elif column2 == LAST_COLUMN_INDEX - ONE:
            self.__board.move_piece(row1, column1, row1, column1 + TWO)
            self.__board.move_piece(row2, column2 + ONE, row2, column2 - ONE)
            self.update_piece_status(row1, column1 + TWO)
            self.add_move_to_list_moves(CASTLING_KING_SIDE)

    def check_draw_by_dead_position(self):
        """A function that returns True if there is a draw by a dead position, else it returns False"""
        white_pieces = []
        black_pieces = []
        for row in range(INITIALIZE, LAST_ROW):
            for column in range(INITIALIZE, LAST_COLUMN):
                if self.__board.get_piece(row, column) != EMPTY:
                    if self.__board.get_piece(row, column).get_color() == WHITE:
                        white_pieces.append(type(self.__board.get_piece(row, column)))
                    else:
                        black_pieces.append(type(self.__board.get_piece(row, column)))
        if (len(white_pieces) == ONE or len(white_pieces) == TWO) and (len(black_pieces) == ONE or len(black_pieces) == TWO):
            if (Bishop in white_pieces or len(white_pieces) == ONE) and (Bishop in black_pieces or len(black_pieces) == ONE):
                return True
        return False

    def check_draw_by_threefold_repetition(self):
        """A function that returns True if there is a draw by a threefold repetition, else it returns False"""
        white_moves = self.__white_moves.copy()
        black_moves = self.__black_moves.copy()
        if len(white_moves) >= MIN_OF_MOVES_TO_CAUSE_THREEFOLD_REPETITION and len(black_moves) >= MIN_OF_MOVES_TO_CAUSE_THREEFOLD_REPETITION:
            if white_moves[len(white_moves) - ONE].replace(EAT_SIGN, NOTHING) == white_moves[len(white_moves) - THREE].replace(EAT_SIGN, NOTHING) and white_moves[len(white_moves) - THREE].replace(EAT_SIGN, NOTHING) == white_moves[len(white_moves) - FIVE].replace(EAT_SIGN, NOTHING):
                if white_moves[len(white_moves) - TWO].replace(EAT_SIGN, NOTHING) == white_moves[len(white_moves) - FOUR].replace(EAT_SIGN, NOTHING):
                    if black_moves[len(black_moves) - ONE].replace(EAT_SIGN, NOTHING) == black_moves[len(black_moves) - THREE].replace(EAT_SIGN, NOTHING) and black_moves[len(black_moves) - THREE].replace(EAT_SIGN, NOTHING) == black_moves[len(black_moves) - FIVE].replace(EAT_SIGN, NOTHING):
                        if black_moves[len(black_moves) - TWO].replace(EAT_SIGN, NOTHING) == black_moves[len(black_moves) - FOUR].replace(EAT_SIGN, NOTHING):
                            return True
        return False

    def check_the_winner(self):
        """A function that sets the winner if someone won or if there was a draw"""
        if is_checkmate(self.__board, self.__player_turn_color):
            if self.__player_turn_color == BLACK:
                self.__winner = WHITE_PLAYER
                self.__white_moves[len(self.__white_moves) - ONE] = self.__white_moves[len(self.__white_moves) - ONE][:len(self.__white_moves[len(self.__white_moves) - ONE]) - ONE] + END_GAME_SIGN + DOUBLE_SPACE + WHITE_WON_SIGN
            else:
                self.__winner = BLACK_PLAYER
                self.__black_moves[len(self.__black_moves) - ONE] = self.__black_moves[len(self.__black_moves) - ONE][:len(self.__black_moves[len(self.__black_moves) - ONE]) - ONE] + END_GAME_SIGN + DOUBLE_SPACE + BLACK_WON_SIGN
        elif (not can_move(self.__board, self.__player_turn_color)) or self.check_draw_by_dead_position() or self.check_draw_by_threefold_repetition():
            self.__winner = DRAW
            if self.__player_turn_color == WHITE:
                self.__black_moves[len(self.__black_moves) - ONE] += END_GAME_SIGN + DOUBLE_SPACE + DRAW_SIGN
            else:
                self.__white_moves[len(self.__white_moves) - ONE] += END_GAME_SIGN + DOUBLE_SPACE + DRAW_SIGN

    def check_winner_by_time_over(self):
        """A function that sets the winner if someone lost when he has no more time"""
        if self.__time.get_black_timer() <= ZERO:
            self.__winner = WHITE_PLAYER
        if self.__time.get_white_timer() <= ZERO:
            self.__winner = BLACK_PLAYER

    def add_move_to_list_moves(self, move):
        """A function that gets a move and adds it to the moves list"""
        if self.__player_turn_color == BLACK:
            self.__black_moves.append(move)
        else:
            self.__white_moves.append(move)


def check_x_pressed():
    """A function that waits until the user press the x button at the end of the game"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                xy_mouse = pygame.mouse.get_pos()
                if XY_X_BUTTON1[X] <= xy_mouse[X] <= XY_X_BUTTON2[X] and XY_X_BUTTON1[Y] <= xy_mouse[Y] <= XY_X_BUTTON2[Y]:
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
