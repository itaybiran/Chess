from Calculations import *
import pygame


class Time(object):
    """A class that responsible for the time in the game"""
    def __init__(self, current_time, timer, add_to_timer):
        self.__clock = pygame.time.Clock()
        self.__current_time = current_time
        self.__white_timer = timer
        self.__black_timer = timer
        self.__add_to_timer = add_to_timer

    def update_timer(self, color, time_passed):
        """A function that updates the timers"""
        if color == BLACK:
            self.__black_timer -= time_passed
        if color == WHITE:
            self.__white_timer -= time_passed

    def calculate_player_time(self, color):
        """A function that calculates the minutes and the seconds that the player has"""
        if color == WHITE:
            minutes = self.__white_timer // THOUSAND // SECONDS_IN_MINUTES
            seconds = self.__white_timer // THOUSAND - minutes * SECONDS_IN_MINUTES
        else:
            minutes = self.__black_timer // THOUSAND // SECONDS_IN_MINUTES
            seconds = self.__black_timer // THOUSAND - minutes * SECONDS_IN_MINUTES
        return minutes, seconds

    def add_time_to_timer(self, color):
        """A function that adds time to the timers
        (depends on the mode the user chooses)"""
        if color == WHITE:
            self.__white_timer += self.__add_to_timer
        else:
            self.__black_timer += self.__add_to_timer

    def get_clock(self):
        """Gets clock"""
        return self.__clock

    def get_current_time(self):
        """Gets current_time"""
        return self.__current_time

    def get_white_timer(self):
        """Gets white_timer"""
        return self.__white_timer

    def get_black_timer(self):
        """Gets black_timer"""
        return self.__black_timer
