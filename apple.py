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

    def new_position(self):
        self.position = generate_random_position_on_grid()
