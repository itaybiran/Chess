from Time import *
from Calculations import *


class MenuGame(object):
    """A class that represents the chess games with the option to choose the mode for every new game"""
    def __init__(self, screen):
        self.__screen = screen
        while True:
            display_img(MENU_IMAGE, self.__screen)
            self.__mode = RAPID_TEN_MINUTES
            self.__is_play_pressed = False
            self.__xy_mouse = (INITIALIZE, INITIALIZE)
            self.choose_mode()
            time = Time(pygame.time.get_ticks(), CONVERT_MODE_TO_TIME[self.__mode], CONVERT_MODE_TO_ADD_TIME[self.__mode])
            ChessGame.ChessGame(self.__screen, time)

    def choose_mode(self):
        """A function that waits until the user choose a mode, and sets the mode to the one the user chooses"""
        self.__xy_mouse = (INITIALIZE, INITIALIZE)
        self.write_mode_name()
        while not self.__is_play_pressed:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                    self.__xy_mouse = pygame.mouse.get_pos()
                    self.check_which_button_pressed()
                    display_img(MENU_IMAGE, self.__screen)
                    self.write_mode_name()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def write_mode_name(self):
        """A function that writes on the screen the mode name"""
        mode_font = pygame.font.Font(FONT_NAME, MODE_FONT_SIZE)
        text = mode_font.render(self.__mode, True, GREY_MODE_TEXT, MODE_BACKGROUND_COLOR)
        text_rect = text.get_rect()
        text_rect.center = (X_OF_TEXT_MODE, Y_OF_TEXT_MODE)
        self.__screen.blit(text, text_rect)
        pygame.display.flip()

    def check_which_button_pressed(self):
        """A function that checks which mode button pressed and sets the mode to this one"""
        if self.check_if_button_pressed(BULLET_ONE_MINUTE_BUTTON[FIRST_POS], BULLET_ONE_MINUTE_BUTTON[SECOND_POS]):
            pygame.mixer.Sound(CHOSE_MODE_SOUND).play()
            self.__mode = BULLET_ONE_MINUTE
        elif self.check_if_button_pressed(BULLET_ONE_MINUTE_ADD_ONE_BUTTON[FIRST_POS], BULLET_ONE_MINUTE_ADD_ONE_BUTTON[SECOND_POS]):
            pygame.mixer.Sound(CHOSE_MODE_SOUND).play()
            self.__mode = BULLET_ONE_MINUTE_ADD_ONE
        elif self.check_if_button_pressed(BULLET_TWO_MINUTES_ADD_ONE_BUTTON[FIRST_POS], BULLET_TWO_MINUTES_ADD_ONE_BUTTON[SECOND_POS]):
            pygame.mixer.Sound(CHOSE_MODE_SOUND).play()
            self.__mode = BULLET_TWO_MINUTES_ADD_ONE
        elif self.check_if_button_pressed(BLITZ_THREE_MINUTES_BUTTON[FIRST_POS], BLITZ_THREE_MINUTES_BUTTON[SECOND_POS]):
            pygame.mixer.Sound(CHOSE_MODE_SOUND).play()
            self.__mode = BLITZ_THREE_MINUTES
        elif self.check_if_button_pressed(BLITZ_THREE_MINUTES_ADD_TWO_BUTTON[FIRST_POS], BLITZ_THREE_MINUTES_ADD_TWO_BUTTON[SECOND_POS]):
            pygame.mixer.Sound(CHOSE_MODE_SOUND).play()
            self.__mode = BLITZ_THREE_MINUTES_ADD_TWO
        elif self.check_if_button_pressed(BLITZ_FIVE_MINUTES_BUTTON[FIRST_POS], BLITZ_FIVE_MINUTES_BUTTON[SECOND_POS]):
            pygame.mixer.Sound(CHOSE_MODE_SOUND).play()
            self.__mode = BLITZ_FIVE_MINUTES
        elif self.check_if_button_pressed(RAPID_TEN_MINUTES_BUTTON[FIRST_POS], RAPID_TEN_MINUTES_BUTTON[SECOND_POS]):
            pygame.mixer.Sound(CHOSE_MODE_SOUND).play()
            self.__mode = RAPID_TEN_MINUTES
        elif self.check_if_button_pressed(RAPID_TWENTY_MINUTES_BUTTON[FIRST_POS], RAPID_TWENTY_MINUTES_BUTTON[SECOND_POS]):
            pygame.mixer.Sound(CHOSE_MODE_SOUND).play()
            self.__mode = RAPID_TWENTY_MINUTES
        elif self.check_if_button_pressed(RAPID_THIRTY_MINUTES_BUTTON[FIRST_POS], RAPID_THIRTY_MINUTES_BUTTON[SECOND_POS]):
            pygame.mixer.Sound(CHOSE_MODE_SOUND).play()
            self.__mode = RAPID_THIRTY_MINUTES
        elif self.check_if_button_pressed(PLAY_BUTTON[FIRST_POS], PLAY_BUTTON[SECOND_POS]):
            pygame.mixer.Sound(START_GAME_SOUND).play()
            self.__is_play_pressed = True

    def check_if_button_pressed(self, xy1, xy2):
        """A function that gets a position of a button and returns True if the mouse is on this button,
        else it returns False"""
        return xy1[X] <= self.__xy_mouse[X] <= xy2[X] and xy1[Y] <= self.__xy_mouse[Y] <= xy2[Y]
