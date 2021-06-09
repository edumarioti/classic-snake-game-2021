import pygame
from random import randint


def generate_random_position_on_grid():
    x = randint(0, 580) // 20 * 20
    y = randint(0, 580) // 20 * 20
    return tuple((x, y))


class Apple:
    DEFAULT_SIZE = (20, 20)
    DEFAULT_COLOR = (255, 20, 20)

    def __init__(self, color=DEFAULT_COLOR, size=DEFAULT_SIZE):

        self.position = generate_random_position_on_grid()
        self.surface = pygame.Surface(size)
        self.surface.fill(color)

    def new_position(self, snake_positions):
        possible_position = False

        while not possible_position:

            possible_position = True

            new_position = generate_random_position_on_grid()

            for current_segment_position in snake_positions:
                if new_position == current_segment_position:
                    print('Maçã iria aparecer no meio!!!')
                    possible_position = False
        
        self.position = new_position
