__author__ = 'Itay Biran'
from ChessGame import ChessGame
import pygame
from Constants import *
from Time import Time
from MenuGame import *
from Calculations import *


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption(CAPTION)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # The screen
    display_img(CHESS_IMAGE, screen)
    wait(MILLISECONDS_DELAY_IN_OPENING)
    MenuGame(screen)
    pygame.display.quit()


if __name__ == '__main__':
    main()
