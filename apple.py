import pygame
from random import randint


def generate_random_position_on_grid():
    x = randint(0, 580) // 20 * 20
    y = randint(0, 580) // 20 * 20
    return tuple((x, y))


class Apple:
    DEFAULT_SIZE = (10, 10)

    def __init__(self, size=DEFAULT_SIZE):

        self.position = generate_random_position_on_grid()
        self.surface = pygame.image.load('media/apple.png')
        self.surface = pygame.transform.scale(self.surface, size)

    def new_position(self):
        self.position = generate_random_position_on_grid()
