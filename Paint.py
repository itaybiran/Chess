from Constants import *
from Calculations import *
import pygame


class Paint(object):
    """A class that responsible for drawing things on the screen"""
    def __init__(self, screen):
        self.__screen = screen

    def draw_chess_board(self):
        """A function that draws the chess board on the screen"""
        img_board = pygame.image.load(BOARD_IMAGE).convert()
        self.__screen.blit(img_board, (X_OF_BOARD_IMG, Y_OF_BOARD_IMG))
        pygame.display.flip()

    def draw_chess_pieces(self, board):
        """A function that paints all the chess pieces on the board"""
        for row_on_board in range(FIRST_ROW, LAST_ROW):
            for column_on_board in range(FIRST_COLUMN, LAST_COLUMN):
                if board.get_piece(row_on_board, column_on_board) != EMPTY:
                    piece_img = pygame.image.load(board.get_piece(row_on_board, column_on_board).get_img()).convert()
                    piece_img.set_colorkey(board.get_piece(row_on_board, column_on_board).get_color_key())
                    self.__screen.blit(piece_img, (column_on_board * SQUARE_SIZE + FIX_X_VALUE, row_on_board * SQUARE_SIZE + FIX_Y_VALUE))
                    pygame.display.flip()

    def draw_eaten_pieces(self, eaten_pieces):
        """A function that paints the eaten pieces on the side of the board"""
        value_of_pieces = {Pawn: PAWN_VALUE, Knight: KNIGHT_VALUE, Bishop: BISHOP_VALUE, Rock: ROCK_VALUE, Queen: QUEEN_VALUE}
        add_to_x_white = INITIALIZE
        add_to_x_black = INITIALIZE
        white_score = INITIALIZE
        black_score = INITIALIZE
        queens_counter_white = INITIALIZE
        queens_counter_black = INITIALIZE
        for piece in eaten_pieces:
            if piece.get_color() == WHITE:
                if not type(piece) == Queen:
                    white_score += value_of_pieces[(type(piece))]
                else:
                    queens_counter_white += ONE
                eaten_piece_img = pygame.image.load(piece.get_eaten_img()).convert()
                eaten_piece_img.set_colorkey(piece.get_color_key())
                self.__screen.blit(eaten_piece_img, (X_OF_EATEN_PIECES + add_to_x_white, Y_OF_EATEN_PIECES_WHITE))
                pygame.display.flip()
                add_to_x_white += FIX_X_VALUE_EATEN_PIECES
            else:
                if not type(piece) == Queen:
                    black_score += value_of_pieces[(type(piece))]
                else:
                    queens_counter_black += ONE
                eaten_piece_img = pygame.image.load(piece.get_eaten_img()).convert()
                eaten_piece_img.set_colorkey(piece.get_color_key())
                self.__screen.blit(eaten_piece_img, (X_OF_EATEN_PIECES + add_to_x_black, Y_OF_EATEN_PIECES_BLACK))
                pygame.display.flip()
                add_to_x_black += FIX_X_VALUE_EATEN_PIECES
        if queens_counter_white >= FIRST_QUEEN:
            white_score += (value_of_pieces[Queen] + ((queens_counter_white - FIRST_QUEEN) * value_of_pieces[Pawn]))
        if queens_counter_black >= FIRST_QUEEN:
            black_score += (value_of_pieces[Queen] + ((queens_counter_black - FIRST_QUEEN) * value_of_pieces[Pawn]))
        self.draw_pieces_value(white_score, black_score, X_OF_EATEN_PIECES + add_to_x_white + FIX_X_VALUE_EATEN_PIECES + TWO, X_OF_EATEN_PIECES + add_to_x_black + FIX_X_VALUE_EATEN_PIECES + TWO)

    def draw_pieces_value(self, white_score, black_score, x_of_white, x_of_black):
        """A function that displays the difference between the value of the white's eaten pieces
         and the value of the black's eaten pieces on the side of the board"""
        score_font = pygame.font.Font(FONT_NAME, SCORE_FONT_SIZE)
        score_string = PLUS_SIGN
        if white_score > black_score:
            score_string += str(white_score - black_score)
            text = score_font.render(score_string, True, SCORE_COLOR, BACKGROUND_COLOR)
            text_rect = text.get_rect()
            text_rect.bottomleft = (x_of_white, Y_OF_SCORE_WHITE)
            self.__screen.blit(text, text_rect)
        elif white_score < black_score:
            score_string += str(black_score - white_score)
            text = score_font.render(score_string, True, SCORE_COLOR, BACKGROUND_COLOR)
            text_rect = text.get_rect()
            text_rect.bottomleft = (x_of_black, Y_OF_SCORE_BLACK)
            self.__screen.blit(text, text_rect)

    def draw_color_of_chosen_piece(self, row, column):
        """A function that marks the square of the chosen piece"""
        if (row + column) % TWO == ZOGI:
            color_img = pygame.image.load(WHITE_SQUARE_IMG).convert()
        else:
            color_img = pygame.image.load(GREEN_SQUARE_IMG).convert()
        self.__screen.blit(color_img, (column * SQUARE_SIZE + FIX_X_VALUE, row * SQUARE_SIZE + FIX_Y_VALUE))
        pygame.display.flip()

    def draw_options_to_move(self, options_to_move, board):
        """A function that marks the squares the chosen piece can move to"""
        for option in options_to_move:
            row, column = option[ROW], option[COLUMN]
            if board.get_piece(row, column) == EMPTY:
                if (row + column) % TWO == ZOGI:
                    option_img = pygame.image.load(OPTION_TO_MOVE_WHITE_SQUARE_IMG).convert()
                else:
                    option_img = pygame.image.load(OPTION_TO_MOVE_GREEN_SQUARE_IMG).convert()
            else:
                if (row + column) % TWO == ZOGI:
                    option_img = pygame.image.load(OPTION_TO_MOVE_EAT_WHITE_SQUARE_IMG).convert()
                else:
                    option_img = pygame.image.load(OPTION_TO_MOVE_EAT_GREEN_SQUARE_IMG).convert()
            option_img.set_colorkey(YELLOW)
            self.__screen.blit(option_img, (column * SQUARE_SIZE + FIX_X_VALUE, row * SQUARE_SIZE + FIX_Y_VALUE))
            pygame.display.flip()

    def draw_moves(self, white_moves, black_moves):
        """A function that displays the moves notation on the side of the board"""
        font = pygame.font.Font(FONT_NAME, CHESS_FONT_SIZE)
        moves = NOTHING
        moves_to_display = []
        for i in range(INITIALIZE, len(white_moves)):
            if i == len(white_moves) - ONE:
                if len(white_moves) == len(black_moves):
                    moves += str(i + ONE) + DOT + white_moves[i] + DOUBLE_SPACE + black_moves[i] + DOUBLE_SPACE
                else:
                    moves += str(i + ONE) + DOT + white_moves[i]
            else:
                moves += str(i + ONE) + DOT + white_moves[i] + DOUBLE_SPACE + black_moves[i] + DOUBLE_SPACE
            if len(moves) >= MAX_CHAR_IN_LINE or i == len(white_moves) - ONE:
                moves_to_display.append(moves)
                moves = NOTHING
        for count, line in enumerate(moves_to_display):
            if count + ONE <= MAX_LINES_THAT_CAN_BE_DISPLAYED:
                text = font.render(line, True, GREY, DARK_GREY)
                text_rect = text.get_rect()
                text_rect.bottomleft = (X_OF_TEXT_RECT_MOVES, Y_OF_TEXT_RECT_MOVES + count * SPACE_BETWEEN_LINES)
                self.__screen.blit(text, text_rect)

    def draw_clocks(self, time, color):
        """A function that writes the time on the timers"""
        time_in_display_format_white = TIME_FORMAT.format(fix_string(time.calculate_player_time(WHITE)[MINUTES]), fix_string(time.calculate_player_time(WHITE)[SECONDS]))
        time_in_display_format_black = TIME_FORMAT.format(fix_string(time.calculate_player_time(BLACK)[MINUTES]), fix_string(time.calculate_player_time(BLACK)[SECONDS]))
        if color == BLACK:
            text_color_black = GREEN
            text_color_white = BLACK_COLOR
        else:
            text_color_white = GREEN
            text_color_black = BLACK_COLOR
        font = pygame.font.Font(FONT_NAME, FONT_SIZE)
        text = font.render(time_in_display_format_black, True, text_color_black, WHITE_COLOR)
        text_rect = text.get_rect()
        text_rect.center = (X_OF_CLOCKS, Y_OF_BLACK_CLOCK)
        self.__screen.blit(text,  text_rect)
        text = font.render(time_in_display_format_white, True, text_color_white, WHITE_COLOR)
        text_rect = text.get_rect()
        text_rect.center = (X_OF_CLOCKS, Y_OF_WHITE_CLOCK)
        self.__screen.blit(text,  text_rect)

    def draw_winner(self, winner):
        """A function that paints the end screen when the game ends"""
        if winner == WHITE_PLAYER:
            img_winner = pygame.image.load(WHITE_WON_IMG).convert()
        elif winner == BLACK_PLAYER:
            img_winner = pygame.image.load(BLACK_WON_IMG).convert()
        else:
            img_winner = pygame.image.load(DRAW_IMG).convert()
        img_winner.set_colorkey(YELLOW)
        self.__screen.blit(img_winner, (X_OF_WINNER_SCREEN, Y_OF_WINNER_SCREEN))
        pygame.display.flip()
