from random import randint

import pygame


class Snake:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    STOPED = 4
    DEFAULT_COLOR = (17, 243, 255)
    DEFAULT_SIZE = (20, 20)

    def __init__(self, color=DEFAULT_COLOR, direction=LEFT, size=DEFAULT_SIZE):
        self.__size_reference = size[0]
        self.__alive = True
        self.__positions = [(200, 200), (220, 200), (240, 200)]
        self.__direction = direction
        self.__score = 3
        self.surface = pygame.Surface(size)
        self.surface.fill(color)

    @property
    def score(self):
        return self.__score

    @property
    def positions(self):
        return self.__positions[:]

    def death(self):
        self.__alive = False

    def sleep(self):
        self.__alive = False

    def wake_up(self):
        self.__alive = True

    def new_direction(self, direction):
        if self.__validate_new_direction(direction):
            self.__direction = direction

    def __validate_new_direction(self, direction):

        new_first_position = self.__return_new_position_according_to_direction(direction)
        second_segment_position = self.__positions[1]
        opposite_direction_actual = new_first_position == second_segment_position

        return not opposite_direction_actual

    def move(self):
        if self.__alive:
            self.__positions[0] = self.__return_new_position_according_to_direction(self.__direction)

    def __return_new_position_according_to_direction(self, direction):

        if direction == Snake.UP:
            new_position_x = self.__positions[0][0]
            new_position_y = self.__positions[0][1] - self.__size_reference

        elif direction == Snake.RIGHT:
            new_position_x = self.__positions[0][0] + self.__size_reference
            new_position_y = self.__positions[0][1]

        elif direction == Snake.DOWN:
            new_position_x = self.__positions[0][0]
            new_position_y = self.__positions[0][1] + self.__size_reference

        if direction == Snake.LEFT:
            new_position_x = self.__positions[0][0] - self.__size_reference
            new_position_y = self.__positions[0][1]

        return tuple((new_position_x, new_position_y))

    def update_positions(self):
        if self.__alive:
            last_position = len(self.__positions) - 1

            for position in range(last_position, 0, -1):
                next_position = (self.__positions[position - 1][0], self.__positions[position - 1][1])

                self.__positions[position] = next_position

    def ate_apple(self):
        self.__positions.append((700, 700))
        self.__score = len(self.__positions)

    def bonus_mixed_color(self):
        color = (randint(20, 255), randint(20, 255), randint(20, 255))
        self.surface.fill(color)
