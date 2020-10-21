import pygame


class Snake:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    STOPED = 4
    DEFAULT_COLOR = (17, 243, 255)
    DEFAULT_SIZE = (10, 10)

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

    def new_direction(self, direction):
        if self.__validate_new_direction(direction):
            self.__direction = direction

    def death(self):
        self.__alive = False

    def __validate_new_direction(self, direction):
        opposite_direction = abs(self.__direction - direction) == 2
        return not opposite_direction

    def move(self):
        if self.__alive:
            if self.__direction == Snake.UP:
                new_position_x = self.__positions[0][0]
                new_position_y = self.__positions[0][1] - self.__size_reference

            if self.__direction == Snake.RIGHT:
                new_position_x = self.__positions[0][0] + self.__size_reference
                new_position_y = self.__positions[0][1]

            if self.__direction == Snake.DOWN:
                new_position_x = self.__positions[0][0]
                new_position_y = self.__positions[0][1] + self.__size_reference

            if self.__direction == Snake.LEFT:
                new_position_x = self.__positions[0][0] - self.__size_reference
                new_position_y = self.__positions[0][1]

            self.__positions[0] = (new_position_x, new_position_y)

    def update_positions(self):
        if self.__alive:
            last_position = len(self.__positions) - 1

            for position in range(last_position, 0, -1):
                next_position = (self.__positions[position - 1][0], self.__positions[position - 1][1])

                self.__positions[position] = next_position

    def ate_apple(self):
        self.__positions.append((700, 700))
        self.__score = len(self.__positions)
